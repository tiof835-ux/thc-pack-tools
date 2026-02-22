#!/usr/bin/env python3
# ==========================================
# THC-TOOLS
# Author: TU_NOMBRE
# Version: 1.0
# Compatible: Termux / Linux
# ==========================================

import os
import sys
import socket
import requests
import platform
import time
from datetime import datetime


# ===============================
# UTILIDADES
# ===============================

def clear():
    os.system("clear" if os.name == "posix" else "cls")


def pause():
    input("\nPress Enter to continue...")


def banner():
    print(r"""
████████╗██╗  ██╗ ██████╗
╚══██╔══╝██║  ██║██╔════╝
   ██║   ███████║██║     
   ██║   ██╔══██║██║     
   ██║   ██║  ██║╚██████╗
   ╚═╝   ╚═╝  ╚═╝ ╚═════╝

        THC TOOLS v1.0
    Python Terminal Toolkit
""")


# ===============================
# 1. INFO DEL SISTEMA
# ===============================

def system_info():
    clear()
    print("=== SYSTEM INFORMATION ===\n")
    print("OS:", platform.system())
    print("Release:", platform.release())
    print("Version:", platform.version())
    print("Machine:", platform.machine())
    print("Processor:", platform.processor())
    print("Hostname:", socket.gethostname())
    print("Time:", datetime.now())
    pause()


# ===============================
# 2. PORT SCANNER BÁSICO
# ===============================

def port_scanner():
    clear()
    print("=== BASIC PORT SCANNER ===\n")
    target = input("Enter target IP or host: ")

    try:
        target_ip = socket.gethostbyname(target)
    except:
        print("Invalid host.")
        pause()
        return

    print(f"\nScanning {target_ip}...\n")

    for port in range(1, 1025):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.5)
        result = s.connect_ex((target_ip, port))
        if result == 0:
            print(f"[OPEN] Port {port}")
        s.close()

    pause()


# ===============================
# 3. HTTP HEADERS CHECKER
# ===============================

def http_headers():
    clear()
    print("=== HTTP HEADER CHECKER ===\n")
    url = input("Enter URL (https://example.com): ")

    try:
        response = requests.get(url)
        print("\n--- HEADERS ---\n")
        for key, value in response.headers.items():
            print(f"{key}: {value}")
    except:
        print("Error connecting to URL.")

    pause()


# ===============================
# 4. DNS LOOKUP
# ===============================

def dns_lookup():
    clear()
    print("=== DNS LOOKUP ===\n")
    host = input("Enter domain: ")

    try:
        ip = socket.gethostbyname(host)
        print(f"\nIP Address: {ip}")
    except:
        print("Domain not found.")

    pause()


# ===============================
# 5. WHOIS LOOKUP (API SIMPLE)
# ===============================

def whois_lookup():
    clear()
    print("=== WHOIS LOOKUP ===\n")
    domain = input("Enter domain: ")

    try:
        response = requests.get(f"https://api.hackertarget.com/whois/?q={domain}")
        print("\n", response.text)
    except:
        print("Error retrieving WHOIS data.")

    pause()


# ===============================
# MENÚ PRINCIPAL
# ===============================

def main_menu():
    while True:
        clear()
        banner()
        print("""
1) System Information
2) Basic Port Scanner (1-1024)
3) HTTP Header Checker
4) DNS Lookup
5) Whois Lookup
0) Exit
""")

        choice = input("Select option > ")

        if choice == "1":
            system_info()
        elif choice == "2":
            port_scanner()
        elif choice == "3":
            http_headers()
        elif choice == "4":
            dns_lookup()
        elif choice == "5":
            whois_lookup()
        elif choice == "0":
            print("Goodbye.")
            sys.exit()
        else:
            print("Invalid option.")
            time.sleep(1)


# ===============================
# ENTRY
# ===============================

if __name__ == "__main__":
    main_menu()
