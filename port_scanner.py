#import python modules
import sys
import socket
import os
from datetime import datetime

#define output folder
output_folder = "scan_reports"
os.makedirs(output_folder, exist_ok=True)

#define a target and translate hostname to ipv4
if len(sys.argv) == 2:
    target = socket.gethostbyname(sys.argv[1])
else:
    print("Please add a target hostname or IP address")
    sys.exit()

#create unique filename
timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
filename = f"{output_folder}/scan_{target}_{timestamp}.txt"

#open file for writing
try:
    with open(filename, "w") as f:
        f.write("=" * 45 + "\n")
        f.write(f"Scan Target: {target}\n")
        f.write("Scanning started: " + str(datetime.now()) + "\n")
        f.write("=" * 45 + "\n")

        for port in range(1,1024):
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            socket.setdefaulttimeout(0.001)

            result = s.connect_ex((target,port))
            if result == 0:
                result_line = f"Port number {port} is open\n"
                print(result_line.strip())
                f.write(result_line)
                
            s.close()

except KeyboardInterrupt:
    print("\nScan halted by user")
    with open(filename, "a") as f:
        f.write("\nScan halted by user\n")
    sys.exit()

#show scan info
print(f"\nScan completed. Results saved to {filename}")
print("=" * 45)
print("Scan Target: " + target)
print("Scanning started: " + str(datetime.now()))
print("=" * 45)
