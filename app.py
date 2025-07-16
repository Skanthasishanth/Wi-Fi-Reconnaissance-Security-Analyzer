from flask import Flask, render_template, request, send_file
import subprocess
import re
import csv
import io

app = Flask(__name__)
last_scan_results = []

def scan_wifi():
    try:
        output = subprocess.check_output(
            ['netsh', 'wlan', 'show', 'networks', 'mode=Bssid'],
            shell=True
        ).decode('utf-8', errors='ignore')

        ssids = re.findall(r'SSID \d+ : (.+)', output)
        signal_strengths = re.findall(r'Signal\s+: (\d+)%', output)
        securities = re.findall(r'Authentication\s+: (.+)', output)

        networks = []
        for i in range(min(len(ssids), len(signal_strengths), len(securities))):
            ssid = ssids[i].strip() or "(Hidden Network)"
            percent = int(signal_strengths[i])
            security = securities[i].strip()

            if percent > 80:
                bars = "📶📶📶📶"
            elif percent > 60:
                bars = "📶📶📶"
            elif percent > 40:
                bars = "📶📶"
            else:
                bars = "📶"

            networks.append({
                'ssid': ssid,
                'signal': f"{percent}%",
                'bars': bars,
                'security': security,
                'insecure': security in ['Open', 'WEP']
            })

        return networks

    except Exception as e:
        print("Error scanning:", e)
        return []

@app.route('/', methods=['GET', 'POST'])
def index():
    global last_scan_results
    networks = []
    if request.method == 'POST':
        networks = scan_wifi()
        last_scan_results = networks
    return render_template('index.html', networks=last_scan_results)

@app.route('/download')
def download_csv():
    global last_scan_results
    if not last_scan_results:
        return "No data to export."

    output = io.StringIO()
    writer = csv.writer(output)
    writer.writerow(['SSID', 'Signal', 'Bars', 'Security'])

    for net in last_scan_results:
        writer.writerow([net['ssid'], net['signal'], net['bars'], net['security']])

    output.seek(0)
    return send_file(io.BytesIO(output.getvalue().encode()), mimetype='text/csv',
                     as_attachment=True, download_name='wifi_report.csv')

if __name__ == '__main__':
    app.run(debug=True)
