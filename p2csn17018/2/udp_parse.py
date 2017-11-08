import sys
import socket
import binascii
import hashlib
checksum_data = sys.argv[1]
source_ip = sys.argv[2]
dest_ip =  sys.argv[3]
split_string = lambda x, n: [x[i:i+n] for i in range(0, len(x), n)]
checksum_data = sys.argv[1]
source_ip = sys.argv[2]
dest_ip =  sys.argv[3]
source = binascii.hexlify(socket.inet_aton(source_ip)).upper()
dest = binascii.hexlify(socket.inet_aton(dest_ip)).upper()
s_port = checksum_data[:4]
d_port = checksum_data[4:8]
length = checksum_data[8:12]
checksuma = checksum_data[12:16]
#print checksuma
data = checksum_data[16:]
#print data
len_data = (len(data)*4/8)+8
len_data = binascii.hexlify(socket.inet_aton(str(len_data))).lower()
#if length == len_data[4:]:
#    print length
data1=data
x= len(data)%4
if x>0:
    for i in range(0,4-x):
        data=data+'0'
#print source,s_port,dest,d_port,data,length
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
new_sp2 = int(p,16)
sum3 =  new_sp2
dp = d_port
        #new_dp1 = int(dp[:4],16)
new_dp2 = int(dp,16)
sum4 =  new_dp2
sum1=sum1+sum2+sum3+sum4
#print sum1
datalist=split_string(data,4)
sumk=0
for i in datalist:
    sumk+=int(i,16)
final_sum= sum1+sumk+int(length,16)+int(length,16)+17
#print final_sum
k=format(final_sum,'016b')
o=len(k)-16
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
#print final_csum,s_port,d_port,data
#print final_csum[4:].lower(),checksum
if final_csum[4:].lower() == checksuma and length == len_data[4:]:
    print new_sp2
    print new_dp2
    print int(length,16)
    print final_cs
    a=str(data1)
    #print a
    a=a.decode("HEX")
    hash_object = hashlib.sha256(a)
    hex_dig = hash_object.hexdigest()
    print(hex_dig)
else:
    print "Invalid UDP segment"
