import nmap

def simple_scanner():
    nm = nmap.PortScanner()
    target = input("Enter the IP address to scan (e.g., 127.0.0.1): ")
    print(f"\nScanning is starting on target: {target}...\n")
    
    nm.scan(target, '21-80', '-sV -Pn --unprivileged')
    
    for host in nm.all_hosts():
        print(f"Host: {host} ({nm[host].hostname()})")
        print(f"State: {nm[host].state()}")
        for proto in nm[host].all_protocols():
            print(f"Protocol: {proto}")
            ports = nm[host][proto].keys()
            for port in ports:
                state = nm[host][proto][port]['state']
                name = nm[host][proto][port]['name']
                version = nm[host][proto][port]['version']
                print(f"Port: {port}\t State: {state}\t Service: {name}\t Version: {version}")

if __name__ == "__main__":
    simple_scanner()
