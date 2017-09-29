s=raw_input()
lis=list(s.split("+"))
lis.sort();

for n in lis:
    print n,"+",
    if n==lis[-1]:
        print n,
