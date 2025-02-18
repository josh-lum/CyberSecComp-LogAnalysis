from scapy.all import *

# Get packets
data_packets = [
    "User loaded into the game",
    "User elected new game",
    "Interaction skipped by player",
    "User selected girl",
    "User selected the name A",
    "Right two steps",
    "Dialog",
    "Left 2 steps",
    "Forward 1 step",
    "Enters door",
    "Two steps forward, dialog",
    "Walk 5 steps",
    "Enters door",
    "Two steps right",
    "Click clock",
    "Set clock",
    "Exit clock",
    "Dialogue",
    "Two steps left",
    "Goes through door",
    "4 steps right",
    "1 step down",
    "Dialogue",
    "5 steps left",
    "3 steps down",
    "Exit house",
    "9 steps left",
    "1 step forward",
    "Dialogue",
    "6 steps up",
    "Enter door",
    "4 steps left",
    "1 step down",
    "Dialogue",
    "1 step up",
    "4 steps right",
    "1 step up",
    "Exit door",
    "5 steps down",
    "Exit door",
    "4 steps right",
    "7 steps up",
    "2 steps right",
    "1 step up",
    "Dialogue",
    "2 steps up",
    "Dialogue",
    "4 steps left",
    "1 step up",
    "Wild zigzagoon",
    "pound tackle pound tackle",
    "zigzagoon fainted",
    "Dialogue",
    "Get pokemon treecko",
    "Name treecko",
    "7 steps down",
    "Exit door",
    "3 steps right",
    "22 steps up",
    "3 steps left",
    "1 step up",
    "4 steps left",
    "Dialogue after interact",
    "10 steps right/left",
    "Wild poochyena",
    "pound tackle pound tackle",
    "8 steps left",
    "1 step down",
    "3 steps right",
    "14 steps down",
    "5 steps left",
    "1 step up",
    "Enter house",
    "5 steps up",
    "5 steps down, exit house",
    "5 steps right",
    "15 steps up",
    "3 steps left",
    "3 steps up",
    "7 steps right",
    "Wild poochyena here",
    "pound crit tackle pound",
    "Treecko learned absorb",
    "3 steps right",
    "5 steps up",
    "2 steps left",
    "Wild wurmple appears",
    "pound stringshot pound stringshot pound",
    "Wurmple fainted",
    "3 steps left",
    "8 steps up",
    "5 steps left",
    "1 step up",
    "Enter pokemon center",
    "4 steps up",
    "Talk to nurse joy",
    "Dialog",
    "4 steps down",
    "Exit building",
    "3 steps right",
    "10 steps up",
    "5 steps right",
    "1 step up",
    "Enter pokemon mart",
    "4 steps up",
    "Dialogue",
    "4 steps down",
    "Exit door",
    "3 steps left",
    "14 steps up",
    "3 steps right",
    "5 steps up",
    "6 steps right",
    "15 steps left",
    "Encounter zigzagoon",
    "pound growl absorb tackle absorb",
    "Zigzagoon faint",
    "Treecko now lvl 7",
    "3 steps up",
    "4 steps right",
    "dialogue rival",
    "Torchic",
    "pound growl pound scratch pound growl pound scratch pound scratch pound",
    "torchic faints",
    "33 steps down",
    "Dialogue",
    "16 steps down",
    "1 step right",
    "20 steps down",
    "3 steps left",
    "Enter door",
    "3 steps up",
    "Dialogue",
    "3 steps down",
    "Exit door",
    "8 steps up",
    "1 step right",
    "8 steps up",
    "3 steps left",
    "10 steps up",
    "4 steps right",
    "6 steps up",
    "10 steps left",
    "3 steps up",
    "12 steps right",
    "2 steps down",
    "6 right",
    "1 step down",
    "6 right",
    "5 steps down",
    "7 steps left",
    "Younger Clyde appears"
]

# Function to create a UDP packet with structured data
def create_packet(data, src_ip, dst_ip, src_port, dst_port):
    type_byte = b'\x55'  # Example type value (change as needed)
    length = len(data).to_bytes(2, 'big')  # Convert length to 2-byte big-endian

    payload = type_byte + length + data.encode()  # Correct structure for Lua dissector
    return IP(src=src_ip, dst=dst_ip) / UDP(sport=src_port, dport=dst_port) / Raw(load=payload)

# Function to generate the pcap
def generate_pcap():
    # Set IP addresses and ports to match Wireshark capture
    src_ip = "46.28.207.53"
    dst_ip = "192.168.0.23"
    src_port = 800  # As seen in Wireshark
    dst_port = 57551  # As seen in Wireshark

    # Create a list to store the packets
    packets = []
    
    # Iterate through the data packets and create corresponding network packets
    for data in data_packets:
        packet = create_packet(data, src_ip, dst_ip, src_port, dst_port)
        packets.append(packet)

    # Save the packets to a pcap file
    wrpcap("pokemon_emerald.pcap", packets)
    print("pcap file 'pokemon_emerald.pcap' created successfully.")

# Generate the pcap
generate_pcap()
