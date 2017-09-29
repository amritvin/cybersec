#sum and product

def sm():
    s=0
    for i in range(1,1001):
	if i%3==0 or i%5==0 :
		s+=i
	
    return s
def pd():
    s=1
    for i in range(1,1001):
        if i%3==0 or i%5==0 :
                s*=i

    return s

print "sum= ",sm()
print "\nproduct= ",pd()
