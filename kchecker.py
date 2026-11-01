#!/usr/bin/env python3
import sys
import json

try:
    import requests
except ImportError:
    print("[!] Missing module 'requests'. Run: pip install requests")
    sys.exit(1)

# ANSI escape codes for colors
RED = "\033[91m"
RESET = "\033[0m"

BANNER = RED + r"""
██╗  ██╗ ██████╗██╗  ██╗███████╗ ██████╗██╗  ██╗███████╗██████╗ 
██║ ██╔╝██╔════╝██║  ██║██╔════╝██╔════╝██║ ██╔╝██╔════╝██╔══██╗
█████╔╝ ██║     ███████║█████╗  ██║     █████╔╝ █████╗  ██████╔╝
██╔═██╗ ██║     ██╔══██║██╔══╝  ██║     ██╔═██╗ ██╔══╝  ██╔══██╗
██║  ██╗╚██████╗██║  ██║███████╗╚██████╗██║  ██╗███████╗██║  ██║
╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚══════╝ ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝
""" + RESET

def check_breach(email):
    url = f"https://api.xposedornot.com/v1/check-email/{email}"
    headers = {"User-Agent": "Mozilla/5.0"}

    print(f"[*] Checking databases for: {email}...")
    
    try:
        response = requests.get(url, headers=headers, timeout=10)
        
        if response.status_code == 200:
            data = response.json()
            if "breaches" in data:
                breaches = data["breaches"][0]
                print(f"\n[!] BREACH FOUND. {email} was exposed in {len(breaches)} breaches:")
                for b in breaches:
                    print(f"    [-] {b}")
            else:
                print(f"\n[+] {email} was not found in any known breaches.")
                
        elif response.status_code == 404:
            print(f"\n[+] {email} was not found in any known breaches.")
        else:
            print(f"\n[!] API returned status code: {response.status_code}")
            
    except requests.exceptions.RequestException as e:
        print(f"\n[!] Network error: {e}")
    except json.JSONDecodeError:
        print("\n[!] Failed to parse API response.")

if __name__ == "__main__":
    print(BANNER)
    print("        KCHECKER - Breach Lookup Tool\n")
    
    if len(sys.argv) != 2:
        print("Usage: kchecker <email>")
        print("Example: kchecker test@example.com")
    else:
        check_breach(sys.argv[1])
