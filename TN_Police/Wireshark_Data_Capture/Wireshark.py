import pyshark
import csv

# create capture object
capture = pyshark.LiveCapture(interface='any')

# open CSV file for writing
with open('wireshark_packets.csv', 'w', newline='') as csvfile:
    # create CSV writer object
    writer = csv.writer(csvfile)

    # write header row
    writer.writerow(['No.', 'Time', 'Source IP', 'Source Port', 'Destination IP', 'Destination Port', 'Protocol', 'Length'])

    # capture packets
    for packet in capture.sniff_continuously():
        # get packet details
        pkt_no = packet.number
        pkt_time = packet.sniff_time
        # pkt_src_ip = packet.ip.src
        # pkt_dst_ip = packet.ip.dst
        pkt_proto = packet.transport_layer
        if pkt_proto is not None:
            pkt_src_port = packet[pkt_proto].srcport
            pkt_dst_port = packet[pkt_proto].dstport
        else:
            pkt_src_port = "N/A"
            pkt_dst_port = "N/A"
        pkt_len = packet.length

        # write packet details to CSV file
        writer.writerow([pkt_no, pkt_time, pkt_src_port, pkt_dst_port, pkt_proto, pkt_len])
