import scapy.all as scapy

def scan(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast / arp_request
    answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]

    results = []

    for element in answered_list:
        result = {"ip": element[1].psrc, "mac": element[1].hwsrc}
        results.append(result)

    return results

def display_results(results):
    print("IP Address\t\tMAC Address")
    print("-----------------------------------------")
    for result in results:
        print(result["ip"] + "\t\t" + result["mac"])

def main():
    target_ip = input("Enter the IP address range to scan (e.g., 192.168.1.1/24): ")
    scan_results = scan(target_ip)

    if not scan_results:
        print("No devices found in the given IP range.")
    else:
        display_results(scan_results)

if __name__ == "__main__":
    main()
