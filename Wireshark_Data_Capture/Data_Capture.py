import csv
import pyshark

# Define the Telegram port number
TELEGRAM_PORT = 443

# Define the CSV filename
CSV_FILENAME = 'Data_Capture.csv'

# Capture packets on the network interface
capture = pyshark.LiveCapture(interface='wlan0', bpf_filter=f'port {TELEGRAM_PORT}')

# Open the CSV file for writing
with open(CSV_FILENAME, 'w', newline='') as csv_file:
    # Create a CSV writer object
    writer = csv.writer(csv_file)
    # Write the CSV header row
    writer.writerow(['Source IP', 'Destination IP', 'Source Port', 'Destination Port', 'Source MAC', 'Destination MAC', 'Encrypted Message', 'Packet Message'])
    # Iterate over the captured packets and write each row to the CSV file
    for packet in capture.sniff_continuously():
        ip_src = packet.ip.src
        ip_dst = packet.ip.dst
        port_src = packet.tcp.srcport
        port_dst = packet.tcp.dstport
        mac_src = packet.eth.src
        mac_dst = packet.eth.dst
        if hasattr(packet, 'tls'):
            if hasattr(packet.tls, 'application_data'):
                encrypted_data = packet.tls.application_data
                packet_message = packet.tcp.payload
                writer.writerow([ip_src, ip_dst, port_src, port_dst, mac_src, mac_dst, encrypted_data, packet_message])
