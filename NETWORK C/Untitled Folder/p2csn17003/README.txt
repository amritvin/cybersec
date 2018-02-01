NAME: Amritanand C
username: P2csn17003

COMPILE:
gcc netcat_part.c -o netcat

Execute:
-----------------------------------------------------------------------------------------------------------------------------------------------------
As client:
============================================
./netcat <options><port><ip>
	eg:	./netcat -p 80  0.0.0.0
it will connect to localhost port 80
-----------------------------------------------------------------------------------------------------------------------------------------------------
for -n
./netcat -n <bytes> <ip><filename>
	eg : netcat -n 100 0.0.0.0 read.txt
-----------------------------------------------------------------------------------------------------------------------------------------------------	
for -o:
It reads a file from the offset to specified or endof the file and send to client.
	./netcat -o<offset> -n <bytes> [-p]:port <ip><filename>
	eg : netcat -o 256 -n 100 0.0.0.0 read.txt
-----------------------------------------------------------------------------------------------------------------------------------------------------
As Server	
=============================================
for -l 
listen to all ips
	netcat <-p> port -l <filename> 
	eg : netcat -l out.txt
and recieve file and write them into the file specified, default port is 9090
---------------------------------------------------------------------------------------------------------------------------------------------------- 

