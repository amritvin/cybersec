import sys
import socket
import binascii
source_ip = sys.argv[1]
source_port =  sys.argv[2]
dest_ip = sys.argv[3]
dest_port = sys.argv[4]
data = sys.argv[5]
data1 = sys.argv[5]
split_string = lambda x, n: [x[i:i+n] for i in range(0, len(x), n)]



def read_inputs():
    source_ip = sys.argv[1]
    source_port =  sys.argv[2]
    dest_ip = sys.argv[3]
    dest_port = sys.argv[4]
    data = sys.argv[5]
    source = binascii.hexlify(socket.inet_aton(source_ip)).upper()
    dest = binascii.hexlify(socket.inet_aton(dest_ip)).upper()
    s_port = binascii.hexlify(socket.inet_aton(source_port)).upper()
    d_port = binascii.hexlify(socket.inet_aton(dest_port)).upper()
    lengt = len(data)
    lengt = ((lengt*4)/8)+8
    #print lengt
    length = binascii.hexlify(socket.inet_aton(str(lengt))).upper()

    #print length

    #print source,s_port,dest,d_port

    #print type(source)
    #print suma

    #sbin =bin(int(source, 16))[2:]
    #print sbin
    x= len(data)%4
    if x>0:
        for i in range(0,4-x):
            data=data+'0'


    #print data
    compute(source,s_port,dest,d_port,data,length)
    #print data
    #for i in source:
    #    sa=sa+hexa[i]
    #print sa
def compute(source,s_port,dest,d_port,data,length):
    s = source
    #print s
    new_s = int(s[:4],16)

    new_s2 = int(s[4:],16)
    sum1 = new_s + new_s2
    #print new_s2
    d = dest
    new_d = int(d[:4],16)
    new_d2 = int(d[4:],16)
    sum2 = new_d + new_d2
    p = s_port
    #new_sp1 = int(p[:4],16)
    new_sp2 = int(p[4:],16)
    sum3 =  new_sp2
    dp = d_port
    #new_dp1 = int(dp[:4],16)
    new_dp2 = int(dp[4:],16)
    sum4 =  new_dp2
    sum1=sum1+sum2+sum3+sum4
    #print sum1
    datalist=split_string(data,4)
    sumk=0
    for i in datalist:
        #print int(i,16)
        sumk+=int(i,16)


    final_sum= sum1+sumk+int(length,16)+int(length,16)+17
    #print final_sum
    #print hex(final_sum)

    k=format(final_sum,'016b')
    #print k
    o=len(k)-16
    #print o
    x=k[:o]
    r=int(x,2)
    y=k[o:]
    s=int(y,2)
    ak=r+s
    binc= hex(ak)
    #print binc
    checksum=int(binc,16)^0xFFFF
    final_cs=hex(checksum)
    final_csum=binascii.hexlify(socket.inet_aton(str(final_cs))).upper()
    #print final_csum
    print s_port[4:].lower()+d_port[4:].lower()+length[4:].lower()+final_csum[4:].lower()+data1.lower()
    #print hex(sum1),hex(sum2),hex(sum3),hex(sum4)

read_inputs()
