# mini_nmap_project_for_port_scan

a bigginer friendly port scanner project that will be updated frequently utill it is like a "mini nmap"

# stage 1 
-scans the small range (1-100) of TCP ports

---detects which ports are open and which are closed

---biggener-friendly 

# requirements for stage 1
python 3 and socket library

# stage 2 
-I have added the stage 2 port scanner with following updates

----It uses exception handling about 

1-timeout...2-invalid host name...3-socket error...4-stop scanning

----I have also used threading for the conveniance of time,as if we scan a 100 ports all should be processed 

parallel as the timeout is 0.5 ... if e dont use it it would take 50 secs to scan that is a bit long...

# how threading works
Normally, a port scanner checks ports one by one.

It tries port 1, waits for a response.

Then port 2, waits again.

This makes scanning slow, because each check takes time.

With threading, multiple ports are scanned at the same time.

Each thread runs the scan() function on a different port.

While one thread is waiting for a response, others are still working.

This makes the scan much faster

# requirements for stage 2
  python3,socket library and threading library.

# Stage 3 
i have added stage in the project and it is ascanner to scan UDP ports only 

it only scans udp ports and give you simple information that which port is open and which is not 

its not that advance from stage 2 but in this stage we understand that how to scan a udp port only 

it gives us a simple understanding that how the scan of udp is different from TCP

# difference between TCP and UDP scan

TCP === TCP is connection-oriented.

A TCP scan usually tries to establish a connection with the target port using the three-way handshake (SYN → SYN/ACK → ACK).

If the port responds with SYN/ACK, it’s open.

If it responds with RST, it’s closed.

If there’s no response, it might be filtered (firewall blocking).

UDP=== UDP is connectionless (no handshake).

A UDP scan just sends a UDP packet to a port.

If it gets a response (like a proper application reply), the port is open.

If it gets an ICMP “Port Unreachable” message, the port is closed.

If there’s no response, it might be open, or filtered (uncertain).

# requirements

python3, socket library
  
# contribution
this is only for educational purpose but feel free to suggest any changes via issues and pull requests
