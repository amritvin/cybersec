NAME: Amritanand C
username: P2csn17003

COMPILE:
gcc netcat_part.c -o netcat

Execute:
./netcat <options><port><ip>
	eg:	./netcat -p 80  0.0.0.0 //it will connect to localhost port 80
for -n
./netcat -n <bytes> <ip><filename>
	eg : netcat -n 100 0.0.0.0
