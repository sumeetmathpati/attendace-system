import subprocess as sub
import time
# import nmap

# p = sub.Popen(['arp'],stdout=sub.PIPE,stderr=sub.PIPE)
# output, errors = p.communicate()
# row=output.split("                  ")
# print row
# print errors

# nm = nmap.PortScanner()
# nm.scan('192.168.0.0/24', arguments='-sP')
# for h in nm.all_hosts():
#     if 'mac' in nm[h]['addresses']:
#         print(nm[h]['addresses'], nm[h]['vendor'])

import sys
from datetime import datetime

from scapy.all import srp,Ether,ARP,conf

def scan_ips(interface='wlp3s0', ips='192.168.0.1/24'):
	"""a simple ARP scan with Scapy"""
	try:
		print('[*] Start to scan')
		conf.verb = 0 # hide all verbose of scapy
		ether = Ether(dst="ff:ff:ff:ff:ff:ff")
		arp = ARP(pdst = ips)
		answer, unanswered = srp(ether/arp, timeout = 2, iface = interface, inter = 0.1)

		for sent, received in answer:
			print(received.summary())

	except KeyboardInterrupt:
		print('[*] User requested Shutdown')
		print('[*] Quitting...')
		sys.exit(1) 

scan_ips()