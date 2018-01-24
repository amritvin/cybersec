#gcd
m=int(input("Enter first  number :"))
n=input("Enter Second number :")
x=m
y=n

r=1
gcd=1
if m>n:
	a=n
	b=m
else :
	b=n
	a=m
if a==0:
	gcd=b
	print "gcd=",gcd
	exit(0) 
while r!=0:
	q=b/a
	r=b%a
	gcd=a
	b=a
	a=r

print "\ngcd(%d,%d)= %d"%(x,y,gcd)
