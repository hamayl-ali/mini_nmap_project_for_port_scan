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
  
# contribution
this is only for educational purpose but feel free to suggest any changes via issues and pull requests
