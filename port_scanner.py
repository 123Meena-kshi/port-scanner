import socket
import threading

target = input("Enter target IP or website: ")
target_ip = socket.gethostbyname(target)

print("\nScanning target:", target_ip)
print("Scanning started...\n")

def scan_port(port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(2)

        result = s.connect_ex((target_ip, port))
        if result == 0:
            print(f"Port {port} is OPEN")

        s.close()

    except:
        pass


threads = []

for port in range(1, 1025):
    thread = threading.Thread(target=scan_port, args=(port,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

print("\nScanning completed.")