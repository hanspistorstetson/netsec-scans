import sys
import re

ips = set()

with open('scans/tcpsyn.scan') as f:
    current_ip = None
    for line in f.readlines():
        if 'Nmap scan report for ' in line:
            current_ip = re.findall(r'([0-9]+\.[0-9]+\.[0-9]+\.[0-9]+)', line)[0]
        else:
            test = re.findall(r'[\d]+', line)
            if len(test) == 1:
                port = int(test[0])
                if (port > 1023):
                    ips.add(current_ip)


for ip in ips:
    print(ip)
