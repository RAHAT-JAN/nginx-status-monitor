# 🛡️ NGINX Scanner

**Author:** Rahat Jan  
**Project:** Real-time NGINX Monitor & Endpoint Scanner  
**Category:** Web Reconnaissance / Load Monitoring / OSINT Automation  


## Description

**NGINX Scanner** is a Python-based tool designed to **monitor a server's real-time NGINX status** and **automatically detect potentially sensitive endpoints**.

This tool provides:

- Live visualization of server load (active, writing, and waiting connections)
- Automatic scanning of common web application endpoints
- Alert popups for potential overload situations
- Logging of discovered endpoints and errors
This is especially useful for blue teams conducting web service audits, bug bounty hunters, red teams identifying attack surfaces, or site reliability engineers (SREs) keeping watch on NGINX load metrics.



## Features

- **Live NGINX Status Parsing** — Tracks active, writing, and waiting connections
- **Automated Endpoint Discovery** — Scans common paths like `/login`, `/api/v1`, `/admin`, etc.
- **Overload Detection Alerts** — GUI popups when thresholds are exceeded
- **Graphical Monitoring** — Interactive matplotlib visualization of connection stats
- **Log Management** — Automatically stores error and endpoint logs to file
- **Colorized Output** — Clean, styled terminal experience with ASCII banner


## Prerequisites

Make sure you have Python 3 installed. Then install the required libraries:

```bash
pip install requests matplotlib colorama
pip install python 
```
## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/nginx-scanner.git
cd nginx-scanner
```
## 🖥️ Demo Screenshot
![image](https://github.com/user-attachments/assets/133bf572-3693-428b-a915-47719eac8738)

![matrix](https://github.com/user-attachments/assets/8d0759a2-25e5-469e-bbcb-4b8eddda7e92)



> _Real-time colored output with matplotlib graph at the end_  
> _(Example only – image not embedded here)_  
> You can expect something like:

```bash
[2025-04-03 14:25:11] Active: 17 | Reading: 2 | Writing: 10 | Waiting: 5
[+] Found: https://target.com/login (Status: 200)
[+] Found: https://target.com/api/v1 (Status: 403)
