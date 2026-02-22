#!/usr/bin/env python3
# ==========================================
# THC PACK TOOLS
# Author: THCTeam
# Version: 2.0
# Team: THCTeam
# Compatible: Termux / Linux
# ==========================================

import os
import sys
import socket
import platform
import time
from datetime import datetime

# ===============================
# COLORES
# ===============================

RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
CYAN = "\033[96m"
WHITE = "\033[97m"
RESET = "\033[0m"

# ===============================
# UTILIDADES
# ===============================

def clear():
    os.system("clear" if os.name == "posix" else "cls")

def pause():
    input(f"\n{YELLOW}Press Enter to continue...{RESET}")

def banner():
    print(f"""{RED}
████████╗██╗  ██╗ ██████╗
╚══██╔══╝██║  ██║██╔════╝
   ██║   ███████║██║     
   ██║   ██╔══██║██║     
   ██║   ██║  ██║╚██████╗
   ╚═╝   ╚═╝  ╚═╝ ╚═════╝
{RESET}
{CYAN}        THC PACK TOOLS v2.0{RESET}
{GREEN}            by THCTeam{RESET}
""")

# ===============================
# 1. SYSTEM INFO
# ===============================

def system_info():
    clear()
    print(f"{CYAN}=== SYSTEM INFORMATION ==={RESET}\n")
    print(f"{GREEN}OS:{RESET}", platform.system())
    print(f"{GREEN}Release:{RESET}", platform.release())
    print(f"{GREEN}Machine:{RESET}", platform.machine())
    print(f"{GREEN}Processor:{RESET}", platform.processor())
    print(f"{GREEN}Hostname:{RESET}", socket.gethostname())
    print(f"{GREEN}Time:{RESET}", datetime.now())
    pause()

# ===============================
# 2. PORT SCANNER
# ===============================

def port_scanner():
    clear()
    print(f"{CYAN}=== BASIC PORT SCANNER (1-1024) ==={RESET}\n")
    target = input("Enter target IP or host: ")

    try:
        target_ip = socket.gethostbyname(target)
    except socket.gaierror:
        print(f"{RED}Invalid host.{RESET}")
        pause()
        return

    print(f"\n{YELLOW}Scanning {target_ip} ...{RESET}\n")

    open_ports = []

    for port in range(1, 1025):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.3)
        result = sock.connect_ex((target_ip, port))
        if result == 0:
            open_ports.append(port)
        sock.close()

    if open_ports:
        print(f"{GREEN}Open Ports Found:{RESET}")
        for port in open_ports:
            print(f"{GREEN}Port {port} OPEN{RESET}")
    else:
        print(f"{RED}No open ports found.{RESET}")

    pause()

# ===============================
# 3. DNS LOOKUP
# ===============================

def dns_lookup():
    clear()
    print(f"{CYAN}=== DNS LOOKUP ==={RESET}\n")
    host = input("Enter domain: ")

    try:
        ip = socket.gethostbyname(host)
        print(f"\n{GREEN}IP Address:{RESET} {ip}")
    except socket.gaierror:
        print(f"{RED}Domain not found.{RESET}")

    pause()

# ===============================
# 4. PING (ICMP SYSTEM CALL)
# ===============================

def ping_host():
    clear()
    print(f"{CYAN}=== PING TOOL ==={RESET}\n")
    host = input("Enter host: ")

    print()
    os.system(f"ping -c 4 {host}")
    pause()

# ===============================
# ABOUT / CREDITS
# ===============================

def about():
    clear()
    print(f"""{CYAN}
THC PACK TOOLS
Version: 2.0

Developed by: THCTeam
Platform: Termux / Linux
Language: Python 3

Educational & Utility Toolkit
{RESET}
""")
    pause()

# ===============================
# MENÚ PRINCIPAL
# ===============================

def main_menu():
    while True:
        clear()
        banner()
        print(f"""
{GREEN}[1]{RESET} System Information
{GREEN}[2]{RESET} Port Scanner
{GREEN}[3]{RESET} DNS Lookup
{GREEN}[4]{RESET} Ping Host
{GREEN}[5]{RESET} About / Credits
{RED}[0]{RESET} Exit
""")

        choice = input("Select option > ")

        if choice == "1":
            system_info()
        elif choice == "2":
            port_scanner()
        elif choice == "3":
            dns_lookup()
        elif choice == "4":
            ping_host()
        elif choice == "5":
            about()
        elif choice == "0":
            print(f"{YELLOW}Exiting...{RESET}")
            time.sleep(1)
            sys.exit()
        else:
            print(f"{RED}Invalid option.{RESET}")
            time.sleep(1)

# ===============================
# ENTRY
# ===============================

if __name__ == "__main__":
    main_menu()
