import scapy.all as scapy
from scapy_http import http
def listen_packet(interface):

    scapy.sniff(iface=interface,store=False,prn=analyze_packets)
    #prn= callback function

def analyze_packets(packet):
    packet.show()
listen_packet("eth0")