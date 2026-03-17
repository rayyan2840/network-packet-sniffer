from scapy.all import sniff, IP

def process_packet(packet):

    if packet.haslayer(IP):

        source_ip = packet[IP].src
        destination_ip = packet[IP].dst
        protocol = packet[IP].proto

        print("Source:", source_ip, "-> Destination:", destination_ip, "| Protocol:", protocol)

print("Packet Sniffer Running...")

sniff(prn=process_packet, store=False)