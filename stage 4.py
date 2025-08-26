import socket
import time
from concurrent.futures import ThreadPoolExecutor

# Store results
tcp = []
udp = []

# Function for TCP scan
def scan_tcp(tar, p, timeout=0.5):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(timeout)
        result = s.connect_ex((tar, p))

        if result == 0:
            print(f"open TCP Port {p}")
            tcp.append(p)

    except Exception as w:
        print(f"error TCP Port {p}: {w}")

# Function for UDP scan
def scan_udp(tar, p, timeout=1):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.settimeout(timeout)
        try:
            s.sendto(b"hello", (tar, p))
            data, addr = s.recvfrom(1024)
            print(f"open UDP Port {p}")
            udp.append(p)
        except socket.timeout:
            # could be open or filtered
            print(f" UDP Port {p} (no response)")
       
    except Exception as e:
        print(f"[Error] UDP Port {p}: {e}")

def banner():
    print("=" * 35)
    print("         Simple Port Scanner")
    print("=" * 35)

def main():
    banner()

    # Ask for target
    target = input("\nEnter IP or hostname: \n").strip()
    try:
        target_ip = socket.gethostbyname(target)
        print(f"Target resolved: {target_ip}")
    except socket.gaierror:
        print("Invalid host given. Exiting.")
        return

    # Ask scan type
    print("\nChoose scan type:")
    print("1) TCP")
    print("2) UDP")
    print("3) Both")
    choice = input("Enter choice (1/2/3): ").strip()

    if choice not in ("1","2","3"):
        print("invalid option mate")
        return
    try:
        #askin for port range
        start=int(input("stat port (default 1: ") or 1)
        end=int(input("end port (default 1024): ") or 1024)
    except ValueError:
        print ("port must be a number...boy")
        return
    
    #checking the port range
    if start>end or end>65535:
        print("invalid port range")
        return
    
    try:
        threads = int(input("Threads (default 50, max 200): ") or 50)
        if threads > 200: 
            threads = 200
    except ValueError:
        print("Threads must be a number.")
        return

    print(f"\nStarting scan on {target_ip}")
    print(f"Ports: {start}-{end}")
    print(f"Threads: {threads}\n")

    start_time =time.time()

    with ThreadPoolExecutor(max_workers=threads) as executor:
        for p in range (start,end+1):
            if choice in["1","3"]:
                executor.submit(scan_tcp,target_ip,p)
            if choice in ["2","3"]:
                executor .submit(scan_udp,target_ip,p)
    end_time=time.time() 

    if tcp:
        print("open TCP ports", sorted(tcp))
        with open("open_tcp.txt","w") as f:
            for p in sorted(tcp):
                f.write(str(p)+"\n")
    
    if udp:
        print("open UDP ports:",sorted(udp))
        with open("open_udp.txt","w") as r:
            for p in sorted(udp):
                r.write(str(p)+"\n")
    if not tcp and not udp :
        print("no open ports are available .... im sorry little boy ")


if __name__=="__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("scan stopped")
