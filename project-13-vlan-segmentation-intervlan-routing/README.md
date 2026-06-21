# Project 13 — VLAN Segmentation & Inter-VLAN Routing (Enterprise Network)

![Status](https://img.shields.io/badge/Status-Completed-brightgreen)
![Type](https://img.shields.io/badge/Type-Networking%20%26%20Security%20Hardening-blue)
![Tools](https://img.shields.io/badge/Tools-Cisco%20Packet%20Tracer-orange)

---

## Objective
Built a complete enterprise network with VLAN segmentation, VTP synchronization across two switches, Inter-VLAN routing via router subinterfaces, DHCP automation, SSH remote management, port security, BPDU Guard, and ACL-based traffic filtering between VLANs.

---

## Full Documentation
This project's full write-up — all 21 steps, every CLI command, the troubleshooting table, and 21 screenshots — lives in my networking repo, not duplicated here:

👉 **[Full lab documentation: cisco-networking-lab-portfolio](https://github.com/malaika-azhar/cisco-networking-lab-portfolio/tree/main/01-networking/enterprise-network-vlan-intervlan-routing)**

---

## Quick Summary
- **VLANs:** Sales (10), IT (20), Management (99) — synced across two switches via VTP
- **Inter-VLAN Routing:** Configured via router subinterfaces with 802.1Q encapsulation
- **DHCP:** Automatic IP assignment per VLAN, verified via lease bindings
- **Security:** Port security with sticky MAC, BPDU Guard, SSH v2 management access, and ACL rules blocking specific inter-VLAN traffic while permitting the rest
- **Verified:** Tested both DHCP assignment and ACL enforcement directly — confirmed blocked traffic actually timed out and permitted traffic actually passed, not just configured and assumed working

---

## Why It's Here
This project lives in a separate repo (`cisco-networking-lab-portfolio`) alongside my other Cisco labs, but it's listed here too so it's visible alongside my SOC/Blue Team work without requiring a visit to a second repo.
