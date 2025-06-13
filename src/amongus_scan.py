import random

def scan_network():
    sus_hosts = ["10.0.0.14", "192.168.1.6", "172.16.42.69"]
    print(" Starting SussyScan™...")
    for host in sus_hosts:
        print(f" Found sus activity on {host} (Role: {random.choice(['Impostor', 'Crewmate'])})")
    print(" Scan complete. Report sent to HQ on Skeld.")

if __name__ == "__main__":
    scan_network()
