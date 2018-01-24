#prime number or not

m=input("Enter a number : ")
flag=0
if m<0:
	print "Prime Numbers should be +ve"
	exit(0)
if m>1000000 :
	print "Out of limit exeeded 10^5"
	exit(0)
if m==1 or m==0 :
	print m,"is niether prime nor  Composite" 
	exit(0)
for i in range(2,(m/2)+1):
   if m%i==0:
      flag=1
      break
if flag==0:
	print m,"is a prime number"
else:
	print m,"is not a prime number"
		 
