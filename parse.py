import sys
import re
import pprint
from collections import defaultdict
from collections import OrderedDict

ips = set()
port_ip = defaultdict(lambda: [])

with open('scans/tcpsyn.scan') as f:
    current_ip = None
    for line in f.readlines():
        if 'Nmap scan report for ' in line:
            current_ip = re.findall(r'([0-9]+\.[0-9]+\.[0-9]+\.[0-9]+)', line)[0]
        else:
            test = re.findall(r'[\d]+', line)
            if len(test) == 1:
                port = int(test[0])
                port_ip[port].append(current_ip)
                if (port > 1023):
                    ips.add(current_ip)



wiki_code = ""
for port in sorted(port_ip.keys()):
    wiki_code += '<div class="tocolours mw-collapsible mw-collapsed">\n'
    wiki_code += 'Port ' + str(port) + '\n<div class="mw-collapsible-content">\n'
    for ip in port_ip[port]:
        wiki_code += str(ip) + "\n"
    wiki_code += "</div>\n</div>\n"

print(wiki_code)