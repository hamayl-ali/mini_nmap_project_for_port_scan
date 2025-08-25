import socket

def udp(tar,p):
    try:
        s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
        s.settimeout(1)
        #sending ** hello **
        s.sendto(b" hello",(tar,p))
        data,add=s.recvfrom(1024)
        print(f"udp port{p} is open")
    except socket.timeout:
        print(f"udp port {p} is open/filtered(no response)")
    except Exception as w:
        print (f"error whiel scanning udp port {p} : {w}")

if __name__=="__main__":
    print("**** UDP port scanner ****")
    tar=input("enter your host name or IP")
    try:
        start=int(input("enter the start"))
        end = int(input("enter the end"))

    except ValueError:
        print(f"invalid port number")

    print(f"Scanning UDp ports {start}---{end} on target {tar}")

    for p in range (start,end+1):
        udp(tar,p)
                  