import sys
import re

with open('scans/tcpsyn.scan') as f:
    current_ip = None
    for line in f.readlines():
        if 'Nmap scan report for ' in line:
            current_ip = re.findall(r'([0-9]+\.[0-9]+\.[0-9]+\.[0-9]+)', line)[0]
        if '23/tcp' in line and 'open' in line:
            print(current_ip)
