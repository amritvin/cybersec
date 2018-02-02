import binascii
import socket
import sys
split_string = lambda x, n: [x[i:i+n] for i in range(0, len(x), n)]
def compute():
    src=str(sys.argv[1])
    dest=str(sys.argv[3])
    p1=int(sys.argv[2])
    p2=int(sys.argv[4])
    d3=str(sys.argv[5])
    d4=d3
    uproto="0x0011"
    udl=8+((len(d3)*4)/8)
    hxudl=hex(udl)
    #print src,p1,dest,p2,d3,hxudl,len(d3)
    hxsrc=binascii.hexlify(socket.inet_pton(socket.AF_INET,src))
    hxdest=binascii.hexlify(socket.inet_pton(socket.AF_INET,dest))
    hxp1=(hex(p1))
    hxp2=(hex(p2))
    srcdestsum=hex(int(hxsrc[4:],16)+int(hxsrc[:4],16)+int(hxdest[4:],16)+int(hxdest[:4],16))
    #print int(srcdestsum,16)
    portsum=hex(p1+p2)
    #print int(portsum,16)
    #hex(int(hxp1,16)+int(hxp2,16))
    chk=len(d3)%4
    if(chk!=0):
        for i in range (0,4-chk):
            d3=d3+'0'
    #print "data adjust:",d3
    chunks =split_string(d3,4)
    sumchunks=0
    for i in chunks:
        #print int(i,16)
        sumchunks+=int(i,16)

    """length=4
    chunksum=0000
    chunks=list((d3[0+i:length+i] for i in range(0, len(d3), length)))
    #print "DATA AND SRCESD:",chunks,srcdestsum
    for e in chunks:
        #print e
        chunksum=chunksum+int(e,16)"""

    #print "data chunksum",hex(chunksum),srcdestsum,portsum
    parsum=hex(int(srcdestsum,16)+int(portsum,16)+int(hex(sumchunks),16)+int(hxudl,16)+int(hxudl,16)+int(uproto,16))
    #print int(parsum,16)
    #print "PARTIAL ",parsum
    #if len(parsum)%4!=0:
        #cp=8-len(parsum)
    #print parsum
    binaa = int(parsum,16)
    bina = format(binaa,'016b')
    #print bina
    n=len(bina)-16
    carry = bina[:n]
    rest = bina[n:]
    suma= hex(int(carry,2)+int(rest,2))
    #print suma
    #print suma
    """parsum=parsum[2:]
    parsum=parsum[::-1]
    #for i in range(1,cp):
    parsum=parsum+"000"
    parsum=parsum[::-1]
    #print "p",parsum"""
    #su=hex(int(parsum[4:],16)+int(parsum[:4],16))
    #print "sum ", su
    cs=int(suma,16)^0xFFFF
    chechex= hex(cs)
    cheksum=binascii.hexlify(socket.inet_aton(str(chechex))).upper()
    sport=binascii.hexlify(socket.inet_aton(str(p1))).upper()
    #print sport
    dport=binascii.hexlify(socket.inet_aton(str(p2))).upper()
    #print dport
    udplength=binascii.hexlify(socket.inet_aton(str(udl))).upper()
    #print cheksum
    #print "checksum",hex(cs)
    hxudl=format(int(hxudl,16),'04x')
    print sport[4:].lower()+dport[4:].lower()+hxudl+cheksum[4:].lower()+d4
compute()
