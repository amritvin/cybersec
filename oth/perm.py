from itertools import permutations
perms = [''.join(p) for p in permutations('aaaiiklmmrsu')]
i=0
for ele in perms:
	print ">>",ele
	if ele=="aumsrikalima":
		print "<<< found",ele,"@",i
		break
	i+=1
