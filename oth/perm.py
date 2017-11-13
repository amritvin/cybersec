from itertools import permutations
perms = [''.join(p) for p in permutations('sooraj')]
i=0
for ele in perms:
	print ">>",ele
	#if ele=="arm":
		#print "<<< found",ele,"@",i
	
	i+=1
print i
