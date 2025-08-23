import socket
import threading

def scan(tar,p):
    try:#simply making a fun. to scan
        soc=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        soc.settimeout(0.5)
        re=soc.connect_ex((tar,p))
        if re==0:
            print(f"Port{p}->Open")
        # i wanted to show you the errors if any of these ever occur
    except socket.timeout:
        print("port connection timeout")
    except socket.error as t:
        print(f"socket error->{t}")
    except Exception as t:
        print(f"error occured->{t}")

# generating the main fun. of the program
try :
    tar1=input("enter the IP address")
    socket.gethostbyname(tar1)#we must know weather the host name ok or not
    start=int(input("enter the starting port"))
    end=int(input("enter the ending port"))
    print(f"Scanning port {start}---{end}")

    #using threading to complete scanning in less time
    threads=[]
    for port in range (start,end+1):
        #thread scans port in parallel 
        t=threading.Thread(target=scan,args=(tar1,port))
        threads.append(t)
        t.start()
    for t in threads:
        t.join()

    print("well the scan is completed mate")

except socket.gaierror:
    print("invalid  host name")
except ValueError:
    print("port number must be integer")
except KeyboardInterrupt:
    print("scan is stopped")
except Exception as w:
    print("error happened")

