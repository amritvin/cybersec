
i=raw_input()
while(True):
    year=i
    year = str(int(year)+1)
    if(len(set(year))==len(year)):
        print year
        break
