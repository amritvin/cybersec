import scapy.all as scapy
import random
import hashlib
import sys
sorc=sys.argv[1]
desti=sys.argv[2]
port=int(sys.argv[3])
scapy.conf.iface = "lo"
scapy.conf.L3socket = scapy.L3RawSocket
sport = random.randint(1024,65535)
# SYN
ip=scapy.IP(src=sorc,dst=desti)
SYN=scapy.TCP(sport=sport,dport=port,flags='S',seq=random.randint(200,600))
SYNACK=scapy.sr1(ip/SYN)

ACK=scapy.TCP(sport=sport, dport=port, flags='A', seq=SYNACK.ack, ack=SYNACK.seq + 1)
data=scapy.sr1(ip/ACK)

ACK=scapy.TCP(sport=sport, dport=port, flags='A', seq=data.ack, ack=data.seq + 1)
ff=scapy.send(ip/ACK)

l = data[scapy.Raw].load
l1=l.strip()
hashed=hashlib.sha256(l1.encode('ascii')).hexdigest()
#
a =scapy.TCP(sport=sport, dport=port, flags='A', seq=data.ack, ack=data.seq+len(l))
sha=scapy.Raw(load=hashed)
ack1=scapy.sr1(ip/a/sha)
#ack1.show()
#LASTACK=scapy.TCP(sport=sport, dport=8000, flags="A",seq=ack1.ack, ack=ack1.seq +len(sha))

ffin=scapy.sniff(iface = "lo",filter="tcp", count=1)
#
FIN=scapy.TCP(sport=sport, dport=port, flags="FA",seq=ffin[0][0].ack, ack=ffin[0][0].seq + 1)
FINACK=scapy.sr1(ip/FIN)
#FINACK.show()
