import socket
from datetime import datetime


ports_to_scan = {
    21: "FTP",
    22: "SSH",
    23: "Telnet",
    25: "SMTP",
    53: "DNS",
    80: "HTTP",
    110: "POP3",
    143: "IMAP",
    443: "HTTPS",
    3306: "MySQL",
    3389: "RDP"
}


def scan_ports(host):
    print(f"\nStarting Security Scan on {host}...\n")
    open_ports = []

    for port, service in ports_to_scan.items():
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(1)
            result = s.connect_ex((host, port))

            if result == 0:
                print(f"Port {port} ({service}) is OPEN")
                open_ports.append((port, service))
            else:
                print(f"Port {port} ({service}) is closed")

            s.close()

        except Exception:
            print(f"Error scanning port {port}")

    return open_ports


def calculate_risk(open_ports):
    high_risk_ports = [21, 23, 3306, 3389]

    for port, _ in open_ports:
        if port in high_risk_ports:
            return "HIGH"

    if len(open_ports) > 3:
        return "MEDIUM"

    if len(open_ports) > 0:
        return "LOW-MEDIUM"

    return "LOW"


def generate_report(host, open_ports, risk_level):
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open("security_scan_report.txt", "w") as file:
        file.write("===== INFRASTRUCTURE SECURITY SCAN REPORT =====\n")
        file.write("Scan Time: " + now + "\n")
        file.write("Target Host: " + host + "\n\n")

        if open_ports:
            file.write("Open Ports Detected:\n")
            for port, service in open_ports:
                file.write(f"- Port {port} ({service})\n")
        else:
            file.write("No open ports detected.\n")

        file.write("\nOverall Risk Level: " + risk_level + "\n")

    print("\nReport saved as 'security_scan_report.txt'")


def main():
    print("==== Local Infrastructure Security Scanner ====\n")

    host = input("Enter target host (default: 127.0.0.1): ")

    if host.strip() == "":
        host = "127.0.0.1"

    open_ports = scan_ports(host)
    risk_level = calculate_risk(open_ports)
    generate_report(host, open_ports, risk_level)

    print("\nScan Completed")
    print("Risk Level:", risk_level)


if __name__ == "__main__":
    main()
