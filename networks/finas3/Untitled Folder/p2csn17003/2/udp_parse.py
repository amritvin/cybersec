import sys
import binascii
import hashlib
import socket
udpcheck=str(sys.argv[1])
src=str(sys.argv[2])
dest=str(sys.argv[3])
p1=int(udpcheck[:4],16)
p2=int(udpcheck[4:8],16)

udl=int(udpcheck[8:12],16)
csum=udpcheck[12:16]
l=len(udpcheck)
data= udpcheck[16:l]
def compute(src,dest,p1,p2,d3):
    """src=str(sys.argv[1])
    dest=str(sys.argv[3])
    p1=int(sys.argv[2])
    p2=int(sys.argv[4])
    d3=str(sys.argv[5])"""
    uproto="0x0011"
    udl=8+((len(d3)*4)/8)
    hxudl=hex(udl)
    hxsrc=binascii.hexlify(socket.inet_pton(socket.AF_INET,src))
    hxdest=binascii.hexlify(socket.inet_pton(socket.AF_INET,dest))
    hxp1=(hex(p1))
    hxp2=(hex(p2))
    srcdestsum=hex(int(hxsrc[4:],16)+int(hxsrc[:4],16)+int(hxdest[4:],16)+int(hxdest[:4],16))
    portsum=hex(p1+p2)
    #hex(int(hxp1,16)+int(hxp2,16))
    chk=len(d3)%4
    if(chk!=0):
        for i in range (0,4-chk):
            d3=d3+'0'
    length=4
    chunksum=0000
    chunks=list((d3[0+i:length+i] for i in range(0, len(d3), length)))
    for e in chunks:
        chunksum=chunksum+int(e,16)
    parsum=hex(int(srcdestsum,16)+int(portsum,16)+int(hex(chunksum),16)+int(hxudl,16)+int(hxudl,16)+int(uproto,16))

    #if len(parsum)%4!=0:
        #cp=8-len(parsum)
    parsum=parsum[2:]
    parsum=parsum[::-1]
    #for i in range(1,cp):
    parsum=parsum+"000"
    parsum=parsum[::-1]
    su=hex(int(parsum[4:],16)+int(parsum[:4],16))
    cs=int(su,16)^0xFFFF
    hxudl=format(int(hxudl,16),'04x')
    #print hex(p1)[2:]+hex(p2)[2:]+hxudl+hex(cs)[2:]+d3
    return hex(cs)
ch=compute(src,dest,p1,p2,data)
s=""
if(ch[2:]==csum):
    print p1
    print p2
    print udl
    print ch
    if len(data)%2==0:
        data=data+"0"
    frags=list((data[0+i:2+i] for i in range(0, len(data),2)))
    for e in frags:
        t=int(e,16)
        s=s+chr(t)
    s = (s.strip('\0'))
    sys.stdout.write(hashlib.sha256(str(s)).hexdigest())
else:
    print "Invalid UDP Segment"
