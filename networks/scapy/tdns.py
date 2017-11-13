"""import scapy.all as scapy
scapy.conf.iface = "lo"
scapy.conf.L3socket = scapy.L3RawSocket
tcp_syn_packet = scapy.TCP(sport=10000, dport=7000, seq=1234567890, flags="S")
ip_syn_packet = scapy.IP(src="127.0.0.1", dst="127.0.0.1")/tcp_syn_packet
ip_syn_ack_packet = scapy.sr1(ip_syn_packet)
print(repr(ip_syn_ack_packet.getlayer(scapy.TCP)))
"""
import scapy.all as scapy
import random
import hashlib
scapy.conf.iface = "lo"
scapy.conf.L3socket = scapy.L3RawSocket
sport = random.randint(1024,65535)
# SYN
ip=scapy.IP(src='127.0.0.1',dst='127.0.0.1')
SYN=scapy.TCP(sport=sport,dport=8000,flags='S',seq=1000)
SYNACK=scapy.sr1(ip/SYN)
print(repr(SYNACK.getlayer(scapy.TCP)))
# SYN-ACK
ACK=scapy.TCP(sport=sport, dport=8000, flags='A', seq=SYNACK.ack + 1, ack=SYNACK.seq + 1)
data=scapy.sr1(ip/ACK)
#print (repr(data.getlayer(scapy.TCP)))
l = data.getlayer(scapy.Raw).load
l=l.strip()
hashed=hashlib.sha256(l.encode('ascii')).hexdigest()
print hashed
#
<<<<<<< HEAD

print "sending hash . . . . . . . . . . . "
a =scapy.IP(dst='127.0.0.1') / scapy.TCP() / scapy.Raw(load=hashed)
=======
a =scapy.IP(src='127.0.0.1', dst='127.0.0.1') / scapy.TCP(sport=sport, dport=8000, flags='A', seq=SYNACK.ack, ack=SYNACK.seq + len(l)) / scapy.Raw(load=hashed)
>>>>>>> a7bf91220d8f184244065004f6a7d35938295454
scapy.sendp(a)
#
print"Recieving FIN . . . . . . . . . . . . "
FIN=ip/scapy.TCP(sport=sport, dport=8000, flags="FA", seq=SYNACK.ack, ack=SYNACK.seq + 1)
FINACK=scapy.sr1(FIN)
FINACK.show()
print"sending ACK . . . . . . . . . . . . . . "
LASTACK=ip/scapy.TCP(sport=sport, dport=8000, flags="A", seq=FINACK.ack, ack=FINACK.seq + 1)
scapy.send(LASTACK)
LASTACK.show()
