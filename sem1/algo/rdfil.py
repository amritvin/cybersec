f = open ( 'input.txt' , 'r')
l = [ map(int,line.split(' ')) for line in f ]
print l
