import requests
import time
import matplotlib.pyplot as plt
from datetime import datetime
from threading import Thread
from tkinter import Tk, messagebox
from colorama import init, Fore, Style

init(autoreset=True)  # Enable colorama

# ------------------------------
# Banner Function and Attribution
# ------------------------------
def show_banner():
    banner = f"""{Fore.CYAN}
  ███╗   ██╗ ██████╗  ██╗███╗   ██╗██╗  ██╗     ███████╗ ██████╗ ██████╗ ███████╗███╗   ██╗ ██████╗ 
  ████╗  ██║██╔═══██╗███║████╗  ██║██║ ██╔╝     ██╔════╝██╔═══██╗██╔══██╗██╔════╝████╗  ██║██╔═══██╗
  ██╔██╗ ██║██║   ██║╚██║██╔██╗ ██║█████╔╝█████╗█████╗  ██║   ██║██║  ██║█████╗  ██╔██╗ ██║██║   ██║
  ██║╚██╗██║██║   ██║ ██║██║╚██╗██║██╔═██╗╚════╝██╔══╝  ██║   ██║██║  ██║██╔══╝  ██║╚██╗██║██║   ██║
  ██║ ╚████║╚██████╔╝ ██║██║ ╚████║██║  ██╗     ██║     ╚██████╔╝██████╔╝███████╗██║ ╚████║╚██████╔╝
  ╚═╝  ╚═══╝ ╚═════╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝     ╚═╝      ╚═════╝ ╚═════╝ ╚══════╝╚═╝  ╚═══╝ ╚═════╝ 
                                    {Fore.YELLOW}by Rahat Jan Project
"""
    print(banner)


# Global variables
attack_logs = []
sensitive_endpoints = []
error_logs = []
session = requests.Session()

common_endpoints = [
    '/', '/login', '/search', '/api/v1', '/admin', '/dashboard', '/user', '/upload',
    '/register', '/profile', '/products', '/cart', '/checkout',
    '/api/v1/login', '/api/v1/register', '/api/v1/upload', '/api/v1/search', '/auth', '/settings'
]


def fetch_nginx_status(url):
    try:
        response = session.get(url, timeout=5)
        if response.status_code == 200:
            return response.text
    except Exception as e:
        error_logs.append(f"{Fore.RED}Error fetching Nginx status: {e}")
    return None


def parse_status_data(data):
    lines = data.strip().split('\n')
    active_connections = int(lines[0].split(': ')[1])
    accepts, handled, requests_count = map(int, lines[2].split())
    reading = int(lines[3].split()[1])
    writing = int(lines[3].split()[3])
    waiting = int(lines[3].split()[5])
    return {
        'active_connections': active_connections,
        'accepts': accepts,
        'handled': handled,
        'requests': requests_count,
        'reading': reading,
        'writing': writing,
        'waiting': waiting
    }


def save_error_logs():
    with open('error_logs.txt', 'w') as f:
        for log in error_logs:
            f.write(log + '\n')
    print(f"{Fore.MAGENTA}Error logs saved to 'error_logs.txt'")


def monitor_nginx_status(url, interval=5, duration=300):
    logs = []
    start_time = time.time()
    while time.time() - start_time < duration:
        data = fetch_nginx_status(url)
        if data:
            status = parse_status_data(data)
            timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            logs.append((timestamp, status))

            print(f"{Fore.GREEN}[{timestamp}] Active: {status['active_connections']} | Reading: {status['reading']} | Writing: {status['writing']} | Waiting: {status['waiting']}")

            if status['active_connections'] > 20 or status['waiting'] > 15:
                show_alert("⚠ Possible Overload Detected!")

        time.sleep(interval)

    plot_logs(logs)
    save_error_logs()
    return logs


def plot_logs(logs):
    timestamps = [log[0] for log in logs]
    active_connections = [log[1]['active_connections'] for log in logs]
    writing = [log[1]['writing'] for log in logs]
    waiting = [log[1]['waiting'] for log in logs]

    plt.figure(figsize=(10, 6))
    plt.plot(timestamps, active_connections, label='Active Connections')
    plt.plot(timestamps, writing, label='Writing')
    plt.plot(timestamps, waiting, label='Waiting')
    plt.xlabel('Time')
    plt.ylabel('Count')
    plt.title('Nginx Status Monitoring Over Time')
    plt.legend()
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()


def test_endpoints(target_url):
    print(f"\n{Fore.YELLOW}[*] Scanning for common sensitive endpoints...\n")
    for endpoint in common_endpoints:
        try:
            full_url = f"{target_url.rstrip('/')}{endpoint}"
            response = session.get(full_url, timeout=5)
            status_code = response.status_code
            if status_code in [200, 401, 403]:
                print(f"{Fore.CYAN}[+] Found: {full_url} (Status: {status_code})")
                sensitive_endpoints.append(full_url)
        except Exception as e:
            error_logs.append(f"[!] Error checking endpoint {endpoint}: {e}")


def save_sensitive_endpoints():
    with open('sensitive_endpoints.txt', 'w') as f:
        for endpoint in sensitive_endpoints:
            f.write(f"{endpoint}\n")
    print(f"{Fore.MAGENTA}\nSensitive endpoints saved to 'sensitive_endpoints.txt'")


def show_alert(message):
    root = Tk()
    root.withdraw()
    messagebox.showinfo("Alert", message)
    root.destroy()


if __name__ == "__main__":
    show_banner()

    url = input(f"{Fore.YELLOW}Enter the Nginx status URL (e.g., https://target.com/nginx_status): ").strip()
    target_url = input(f"{Fore.YELLOW}Enter the Target Base URL (e.g., https://target.com): ").strip()
    interval = int(input(f"{Fore.YELLOW}Enter the monitoring interval (in seconds): "))
    duration = int(input(f"{Fore.YELLOW}Enter the monitoring duration (in seconds): "))

    monitoring_thread = Thread(target=monitor_nginx_status, args=(url, interval, duration))
    monitoring_thread.start()

    test_endpoints(target_url)
    save_sensitive_endpoints()