import subprocess

# Run the "iwconfig" command to get wireless interface information
wireless_info = subprocess.check_output(["iwconfig"]).decode()

# Parse the wireless interface information to get the SSID and encryption type
ssid = ""
encryption = ""
for line in wireless_info.split("\n"):
    if "ESSID:" in line:
        ssid = line.split(":")[1].strip().strip('"')
    elif "Encryption key:" in line:
        encryption = line.split(":")[1].strip()

# Print the SSID and encryption type
print(f"SSID: {ssid}")
print(f"Encryption: {encryption}")

# Check if encryption is enabled
if encryption == "off":
    print("Warning: Encryption is disabled! Your WiFi connection is not secure.")
else:
    print("Your WiFi connection is secure.")
    