# 🛡️ NGINX Scanner

**Author:** Rahat Jan  
**Project:** Real-time NGINX Monitor & Endpoint Scanner  
**Category:** Web Reconnaissance / Load Monitoring / OSINT Automation  

---

## 📌 Overview

`NGINX Scanner` is a Python-based tool designed to:

- Monitor live server metrics from `/nginx_status`
- Automatically detect sensitive endpoints and directories
- Trigger alerts based on traffic anomalies
- Visualize connection data over time using interactive plots

This is especially useful for blue teams conducting web service audits, bug bounty hunters, red teams identifying attack surfaces, or site reliability engineers (SREs) keeping watch on NGINX load metrics.

---

## ✨ Features

- ✅ **Live NGINX Status Parsing** — Tracks active, writing, and waiting connections
- 🔎 **Automated Endpoint Discovery** — Scans common paths like `/login`, `/api/v1`, `/admin`, etc.
- 🚨 **Overload Detection Alerts** — GUI popups when thresholds are exceeded
- 📊 **Graphical Monitoring** — Interactive matplotlib visualization of connection stats
- 📝 **Log Management** — Automatically stores error and endpoint logs to file
- 🎨 **Colorized Output** — Clean, styled terminal experience with ASCII banner

---

## 🖥️ Demo Screenshot
![image](https://github.com/user-attachments/assets/133bf572-3693-428b-a915-47719eac8738)
![image](https://github.com/user-attachments/assets/3b192aa1-9364-464f-b295-a436f062a5c1)

![matrix](https://github.com/user-attachments/assets/8d0759a2-25e5-469e-bbcb-4b8eddda7e92)



> _Real-time colored output with matplotlib graph at the end_  
> _(Example only – image not embedded here)_  
> You can expect something like:

```bash
[2025-04-03 14:25:11] Active: 17 | Reading: 2 | Writing: 10 | Waiting: 5
[+] Found: https://target.com/login (Status: 200)
[+] Found: https://target.com/api/v1 (Status: 403)
