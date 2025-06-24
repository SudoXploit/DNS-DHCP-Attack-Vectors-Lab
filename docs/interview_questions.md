# 🧠 DNS & DHCP – Interview Questions & Answers

These questions are designed to test foundational and offensive knowledge of DNS/DHCP concepts as they relate to cybersecurity, red teaming, and infrastructure hardening.

---

### 1. **What is DNS Spoofing?**
DNS spoofing (or cache poisoning) is an attack where false DNS responses are injected to redirect users to malicious IPs instead of legitimate ones.

---

### 2. **How does DHCP Starvation work?**
The attacker floods the DHCP server with fake IP lease requests until the pool is exhausted. This prevents legitimate devices from getting an IP.

---

### 3. **What’s the difference between a Rogue DHCP server and a legitimate one?**
A rogue DHCP server is unauthorized and often malicious. It issues IP configurations to clients, redirecting them to attacker-controlled gateways or DNS servers.

---

### 4. **Why are DNS and DHCP considered high-value attack surfaces?**
Because they’re trust-based, unauthenticated protocols by design. Exploiting them allows for traffic interception, MITM attacks, and endpoint manipulation.

---

### 5. **Name a tool for DNS spoofing and describe its usage.**
`DnsChef` is a DNS proxy tool used to respond with spoofed records. It's useful in lab environments to redirect victim DNS queries for phishing or MITM testing.

---

### 6. **What is the impact of DHCP spoofing on a corporate network?**
It can result in man-in-the-middle attacks, DNS hijacking, internet disconnection, and even internal traffic rerouting.

---

### 7. **What mitigations exist for DHCP-based attacks?**
- Use DHCP snooping
- Enable port security on switches
- Monitor for MAC/IP anomalies
- Limit DHCP responses to trusted ports

---

### 8. **What is DNSSEC and does it defend against DNS spoofing?**
Yes. DNSSEC signs DNS responses cryptographically. Clients verify the signatures, preventing attackers from injecting forged responses.

---

### 9. **Can you describe a real-world incident involving DNS or DHCP abuse?**
[Customize this to a known attack or test incident.]

Example: In 2018, attackers used rogue DHCP servers to push malicious DNS settings in a phishing campaign, redirecting users to credential-stealing portals.

---

### 10. **How can Wireshark help in DNS/DHCP attack detection?**
Wireshark can capture and visualize DHCP DISCOVER floods, rogue OFFERs, or suspicious DNS responses — helping identify misbehaving clients or rogue servers.

---

### 11. **What’s the TTL value in DNS responses? Why does it matter in attacks?**
TTL (Time To Live) controls how long a DNS entry is cached. Attackers often use low TTLs to enforce frequent resolution — useful in dynamic redirections or short-lived phishing.

---

### 12. **What are some signs of DNS tunneling on a network?**
- High volume of small DNS requests
- Long domain/subdomain strings
- Use of uncommon TLDs
- DNS over non-standard ports

---

### 13. **What is a DHCP lease and how is it manipulated in an attack?**
A lease is a temporary IP assignment. In attacks like starvation or spoofing, attackers disrupt or override lease negotiations to hijack traffic or block service.

---

### 14. **Explain how to detect rogue DHCP servers in a network.**
- Use tools like `dhcp_probe`, `Yersinia`, or custom Nmap scripts
- Monitor unexpected DHCP OFFER messages
- Check for multiple responses to DISCOVER packets

---

### 15. **What’s the risk of allowing DHCP and DNS traffic across VLANs?**
VLAN hopping combined with misconfigured DHCP relays can allow attackers to serve rogue configs across trusted zones — a classic lateral movement vector.

---
