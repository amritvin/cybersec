s=raw_input()
s=s.lower()
s=s.translate(None, "aeioyu")
sy="."
print "."+sy.join(s)
