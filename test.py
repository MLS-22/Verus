#!/usr/bin/env python3
import subprocess

# Function to download ccminer
def download_ccminer(url):
    subprocess.run(["wget", url])

# Get CPU model information
cpu_info = subprocess.check_output(["lscpu"]).decode("utf-8")

# Check CPU model and download ccminer accordingly
if "Cortex-A53" in cpu_info and "Cortex-A72" in cpu_info:
    download_ccminer("https://raw.githubusercontent.com/Darktron/pre-compiled/a73-a53/ccminer")

elif "Cortex-A53" in cpu_info and "Cortex-A73" in cpu_info:
    download_ccminer("https://raw.githubusercontent.com/Darktron/pre-compiled/a73-a53/ccminer")

elif "Cortex-A55" in cpu_info and "Cortex-A75" in cpu_info:
    download_ccminer("https://raw.githubusercontent.com/Darktron/pre-compiled/a75-a55/ccminer")

elif "Cortex-A53" in cpu_info:
    download_ccminer("https://raw.githubusercontent.com/Darktron/pre-compiled/a53/ccminer")

else:
    print("Unsupported CPU model detected:", cpu_info)
    choice = input("Do you want to download the generic ccminer? (y/n): ").lower()
    if choice == 'y':
        download_ccminer("https://raw.githubusercontent.com/Darktron/pre-compiled/generic/ccminer")
    elif choice == 'n':
        print("No action taken. Exiting.")
    else:
        print("Invalid choice. Exiting.")
