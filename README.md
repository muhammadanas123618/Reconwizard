**ReconWizard** is a modular, Python-based reconnaissance tool designed for use in offensive security engagements and red team simulations. It automates key passive and active information gathering steps and produces both HTML and TXT reports.

---

## 🔧 Features

### 🕵️ Passive Reconnaissance
- WHOIS Lookup
- DNS Enumeration (A, MX, TXT, NS records)
- Subdomain Enumeration (via crt.sh)

### 🚪 Active Reconnaissance
- Port Scanning (select common ports)
- Banner Grabbing (includes TLS/SSL detection)
- Technology Detection (via WhatWeb)

### 🧾 Reporting
- Generates `.txt` and `.html` reports
- Includes timestamp and resolved IP address

---

## 📦 Installation

### Clone and set up the virtual environment:
```bash
git clone https://github.com/muhammadanas123618/Reconwizard.git
cd Reconwizard
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
pip install -e .
```

> Make sure [WhatWeb](https://github.com/urbanadventurer/WhatWeb) is installed:
```bash
sudo apt install whatweb
```

---

## 🚀 Usage

After installation, you can run:
```bash
reconwizard <domain> [OPTIONS]
```

### Example:
```bash
reconwizard example.com --whois --dns --subdomains --scan --banner --tech --verbose
```

### Options:
- `--whois`       → Run WHOIS lookup
- `--dns`         → Perform DNS enumeration
- `--subdomains`  → Enumerate subdomains
- `--scan`        → Scan ports (common)
- `--banner`      → Grab service banners
- `--tech`        → Detect technologies using WhatWeb
- `--verbose`     → Enable debug logging

---

## 📁 Directory Structure
```
reconwizard/
├── cli.py               # Main CLI entry
├── whois_lookup.py      # WHOIS functionality
├── dns_enum.py          # DNS enumeration
├── subdomain_enum.py    # Subdomain finder
├── port_scanner.py      # TCP port scanner
├── banner_grabber.py    # Service banner grabber
├── tech_detect.py       # WhatWeb wrapper
├── report_generator.py  # HTML report via Jinja2
```

---

## 🧠 Credits
Created for offensive security internship training purposes.

> Inspired by best practices in modular recon tooling and red team automation.

---

## 📜 License
MIT License
