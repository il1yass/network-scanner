# Network Scanner

A simple Python-based network scanner using the Scapy library.

## Installation

1. Install the required dependencies by running:

    ```
    pip install -r requirements.txt
    ```

2. Run the scanner using the command:

    ```
    python main.py
    ```

## Usage

1. Upon running the scanner, input the range of IP addresses you want to scan.
2. The scanner will perform the scan and output a list of discovered devices with their IP addresses and MAC addresses.

## Example

```
Enter the IP address range to scan (e.g., 192.168.1.1/24): 192.168.1.1/24
IP Address       MAC Address
--------------------------------
192.168.1.1      00:11:22:33:44:55
192.168.1.2      66:77:88:99:AA:BB
...

```

## Notes

- Ensure that your device has permission to scan the network.
- Depending on the network configuration and security settings, the scanner may not detect certain devices.

