from scapy.all import ARP, send, IP, TCP, Ether

# Define the IP addresses and MAC addresses of the two servers
server1_ip = "10.10.1.1"
server1_mac = "0c:42:a1:8b:2f:88"
server2_ip = "10.10.1.2"
server2_mac = "0c:42:a1:8c:dc:24"

# Function to send ARP packets
def send_arp_packets():
    # Create an ARP request packet from server1 to server2
    arp_request = ARP(pdst=server2_ip, hwsrc=server1_mac, psrc=server1_ip)
    
    # Create an ARP reply packet from server2 to server1
    arp_reply = ARP(op=2, pdst=server1_ip, hwdst=server1_mac, psrc=server2_ip, hwsrc=server2_mac)
    
    # Send the ARP request
    print("Sending ARP request")
    send(arp_request, verbose=1, count=10)
    
    # Send the ARP reply
    print("Sending ARP reply")
    send(arp_reply, verbose=1, count=10)

# Function to send TCP packets
def send_tcp_packets():
    # Create an IP packet
    ip = IP(src=server1_ip, dst=server2_ip)
    
    # Create a TCP SYN packet
    tcp_syn = TCP(sport=12345, dport=80, flags="S", seq=100)
    
    # Create the full packet
    tcp_syn_packet = ip/tcp_syn
    
    # Send the TCP SYN packet
    print("Sending TCP SYN packet")
    send(tcp_syn_packet, verbose=1, count=10)
    
    # Create a TCP ACK packet in response to the SYN-ACK (assuming we received one with seq=101, ack=101)
    tcp_ack = TCP(sport=12345, dport=80, flags="A", seq=101, ack=101)
    tcp_ack_packet = ip/tcp_ack
    
    # Send the TCP ACK packet
    print("Sending TCP ACK packet")
    send(tcp_ack_packet, verbose=1, count=10)

# Send ARP packets
send_arp_packets()

# Send TCP packets
send_tcp_packets()

