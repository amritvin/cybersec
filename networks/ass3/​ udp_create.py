import binascii
import socket
import sys
def compute():
    src=str(sys.argv[1])
    dest=str(sys.argv[3])
    p1=int(sys.argv[2])
    p2=int(sys.argv[4])
    d3=str(sys.argv[5])
    uproto="0x0011"
    udl=8+((len(d3)*4)/8)
    hxudl=hex(udl)
    #print src,p1,dest,p2,d3,hxudl,len(d3)
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
    #print "data adjust:",d3
    length=4
    chunksum=0000
    chunks=list((d3[0+i:length+i] for i in range(0, len(d3), length)))
    #print "DATA AND SRCESD:",chunks,srcdestsum
    for e in chunks:
        #print e
        chunksum=chunksum+int(e,16)
    #print "data chunksum",hex(chunksum),srcdestsum,portsum
    parsum=hex(int(srcdestsum,16)+int(portsum,16)+int(hex(chunksum),16)+int(hxudl,16)+int(hxudl,16)+int(uproto,16))
    #print "PARTIAL ",parsum
    #if len(parsum)%4!=0:
        #cp=8-len(parsum)
    parsum=parsum[2:]
    parsum=parsum[::-1]
    #for i in range(1,cp):
    parsum=parsum+"000"
    parsum=parsum[::-1]
    #print "p",parsum
    su=hex(int(parsum[4:],16)+int(parsum[:4],16))
    #print "sum ", su
    cs=int(su,16)^0xFFFF
    #print "checksum",hex(cs)
    hxudl=format(int(hxudl,16),'04x')
    print hex(p1)[2:]+hex(p2)[2:]+hxudl+hex(cs)[2:]+d3
compute()
