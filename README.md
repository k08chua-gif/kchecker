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
   First, grant execution permissions to the script:
   ```bash
   chmod +x kchecker.py
   ```
   For Termux (Android):
   Copy the executable to Termux's local bin directory.
   ```bash
   cp kchecker.py $PREFIX/bin/kchecker
   ```
   For Debian-based Linux (Kali, Ubuntu) and macOS:
   Copy the executable to the system's local binary directory.
   ```bash
   sudo cp kchecker.py /usr/local/bin/kchecker
   ```

Usage

Once installed, run the tool from anywhere in your terminal by passing the target email address as an argument:

```bash
kchecker target@example.com
```

Disclaimer

This tool is intended for educational purposes and authorized OSINT research only.

```
