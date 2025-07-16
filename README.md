# 🔍 Wi-Fi Reconnaissance & Security Analyzer

A web-based Wi-Fi scanning and security analysis tool built using **Flask** and the `netsh` command for Windows systems. This project helps you visualize nearby Wi-Fi networks, identify insecure access points (like WEP or open networks), view signal strength, and download reports in `.csv` format.

---

## 📌 Features

✅ Scans all nearby Wi-Fi networks using `netsh wlan show networks`  
✅ Displays SSID, signal strength, and security protocol  
✅ Signal strength visualized with 📶 bars  
✅ Insecure networks (WEP/Open) are highlighted in red  
✅ Detects hidden networks and labels them as "(Hidden Network)"  
✅ Download scanned results as `.csv` file  
✅ Clean and responsive web interface using HTML & CSS  
✅ Works fully offline – no internet or external API needed  
✅ Ethical and safe – passive scan only, no hacking tools used

---

## 🛠️ Technologies Used

- Python 3
- Flask (Web Framework)
- HTML5 + CSS3
- `netsh wlan` (Windows-only)

---

## ⚙️ How to Run the Project

1. Make sure you’re on **Windows** and have **Python 3** installed.

2. Install required dependencies:

```
pip install flask
```

3. Run the App

```
python app.py
```

4. Open in Browser
   
```
Visit http://127.0.0.1:5000 in your browser.
```

## 📥 Download Report

After scanning, click ⬇️ Download Report to export the results as a .csv file for analysis or record keeping.

## 🖼️ UI Screenshots

<img width="1920" height="958" alt="aaa" src="https://github.com/user-attachments/assets/0ff434d6-5055-425a-86f2-0d033898404e" />

<img width="1920" height="960" alt="bbb" src="https://github.com/user-attachments/assets/3fdd78fc-8798-4e4a-b736-53a70bfb41cf" />



## 📌 Notes

This project works only on Windows because it uses the netsh wlan show networks command.

The app does not attempt to connect, deauthenticate, or sniff packets — it's strictly for ethical and educational purposes.

Insecure networks = Open or WEP authentication methods

## 👨‍💻 Developed By

#### S Kantha Sishanth
