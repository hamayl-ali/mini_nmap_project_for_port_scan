import socket

target=input("Enter your IP address please").strip()
print (f"Scanning{target}ports(1-100)")

for port in range(1,100):
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.settimeout(0.5)#normal timeout to prevent hang
    re=s.connect_ex((target,port))

    if re==0:
        print(f"Port {port} is Open")

    print("scan complete")

