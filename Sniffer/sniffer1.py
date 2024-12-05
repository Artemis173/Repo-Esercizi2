from scapy.all import *
from scapy.layers.http import HTTPRequest 
from scapy.layers.http import HTTPResponse

iPkt = 0

def process_packet(packet):
        global iPkt 
        iPkt += 1
        iPkt += 1
        print("Ho letto un pacchetto sulla tua macchina " + str(iPkt))
                #print("Ho ricevuto un pkt")
        if not packet.haslayer(IP):
                return
        
        ip_layer = "IP_SRC:" + packet[IP].src + "IP_DST" + packet[IP].dst + " " + str(packet[IP].proto) + " " + str(packet[IP].len);
        print(ip_layer)
        print("Ho ricevuto un pacchetto IP")

        if packet[IP].proto == 6:
                print("TCP_SRC_PORT: " + str(packet[TCP].sport) + "TCP_DST_PORT: " + str(packet[TCP].dport))
                if packet[TCP].sport==80 or packet[TCP].dport==80:
                        print("Ho ricevuto un pacchetto HTTP")
                #if (str(packet[TCP].sport) or str(packet[TCP].dport)) == "443":
                #        print("Ho ricevuto un pacchetto TLS")
                if str(packet[TCP].sport) == "80":
                        print("HttpResponse")
                        if packet.haslayer(HTTPResponse):
                                print(packet[HTTPResponse].show())
                if str(packet[TCP].dport) == "80":
                        print("HttpRequest")
                        if packet.haslayer(HTTPRequest):
                                print(packet[HTTPRequest].show())

sniff(iface="enp4s0",filter="tcp", prn=process_packet)