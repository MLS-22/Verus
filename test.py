#!/usr/bin/env python3
import subprocess

# Function to download ccminer
def download_ccminer(url):
    subprocess.run(["wget", url])

# Get CPU model information
cpu_info = subprocess.check_output(["lscpu"]).decode("utf-8")
cpu_model_line = [line for line in cpu_info.split('\n') if "Model name" in line]

if cpu_model_line:
    cpu_model = cpu_model_line[0].split(":")[1].strip()

    # Check CPU model and download ccminer accordingly
    if "Cortex-A53" in cpu_model and "Cortex-A72" in cpu_model:
        download_ccminer("https://raw.githubusercontent.com/Darktron/pre-compiled/a73-a53/ccminer")

    elif "Cortex-A53" in cpu_model and "Cortex-A73" in cpu_model:
        download_ccminer("https://raw.githubusercontent.com/Darktron/pre-compiled/a73-a53/ccminer")

    elif "Cortex-A55" in cpu_model and "Cortex-A75" in cpu_model:
        download_ccminer("https://raw.githubusercontent.com/Darktron/pre-compiled/a75-a55/ccminer")

    elif "Cortex-A53" in cpu_model:
        download_ccminer("https://raw.githubusercontent.com/Darktron/pre-compiled/a53/ccminer")

    else:
        print("Unsupported CPU model detected:", cpu_model)
        choice = input("Do you want to download the generic ccminer? (y/n): ").lower()
        if choice == 'y':
            download_ccminer("https://raw.githubusercontent.com/Darktron/pre-compiled/generic/ccminer")
        elif choice == 'n':
            print("No action taken. Exiting.")
        else:
            print("Invalid choice. Exiting.")
else:
    print("Error: Could not find CPU model information.")
