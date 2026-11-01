# Kchecker

A lightweight, command-line OSINT tool written in Python to check if an email address has been exposed in known data breaches.

## Features
- Fast, API-driven lookup (uses XposedOrNot).
- No API keys required.
- Clean, colorized terminal output.

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/YOUR_USERNAME/kchecker.git
   cd kchecker

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt

3. Make the script executable and install it to your system path.

   **For Termux (Android):**
   Use the `$PREFIX` environment variable to place the executable in Termux's local bin directory.
   ```bash
   chmod +x kchecker.py
   cp kchecker.py $PREFIX/bin/kchecker
   
   **For Debian-based Linux (Kali, Ubuntu) and macOS:**
   chmod +x kchecker.py
   sudo cp kchecker.py /usr/local/bin/kchecker	

