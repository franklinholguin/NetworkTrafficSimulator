from scapy.all import IP, TCP, UDP, send
import time

def simulate_traffic():
    src_ip = "192.168.1.100"
    dst_ip = "192.168.1.200"
    
    # Simulate HTTP traffic
    packet1 = IP(src=src_ip, dst=dst_ip)/TCP(sport=12345, dport=80)
    print("Sending HTTP packet...")
    send(packet1, verbose=0)
    
    # Simulate SSH traffic
    packet2 = IP(src=src_ip, dst=dst_ip)/TCP(sport=12346, dport=22)
    print("Sending SSH packet...")
    send(packet2, verbose=0)
    
    time.sleep(1)

if __name__ == "__main__":
    print("Simulating network traffic (run as root if on Linux)...")
    simulate_traffic()