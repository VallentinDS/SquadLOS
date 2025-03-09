import os
import re

# Folder containing log files
log_folder = "logs"

# Regular expression to match IP addresses
ip_regex = re.compile(r"\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b")

# Set to store unique IP addresses
unique_ips = set()

# Iterate through all log files
for filename in os.listdir(log_folder):
    file_path = os.path.join(log_folder, filename)

    # Read the file line by line
    with open(file_path, "r", encoding="utf-8") as f:
        for line in f:
            match = ip_regex.search(line)
            if match:
                unique_ips.add(match.group())

# Exclude IPs that start with 64.
filtered_ips = [ip for ip in unique_ips if not ip.startswith("64.")]
print(filtered_ips)
