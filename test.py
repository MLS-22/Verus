#!/usr/bin/env python3
import subprocess
import requests

# Function to download ccminer
def download_ccminer(url):
    subprocess.run(["wget", url])

# Get CPU model information
cpu_info = subprocess.check_output(["lscpu"]).decode("utf-8")
cpu_model_line = [line for line in cpu_info.split('\n') if "Model name" in line]

if cpu_model_line:
    cpu_model = cpu_model_line[0].split(":")[1].strip()

    # Extract CPU numbers from the model
    cpu_numbers = [part.split('-')[1].strip() for part in cpu_model.split('Cortex-')]

    # Generate ccminer URL
    ccminer_url = f"https://raw.githubusercontent.com/Darktron/pre-compiled/{cpu_numbers[0]}-{cpu_numbers[1]}/ccminer"

    # Check if ccminer URL exists
    response = requests.head(ccminer_url)
    if response.status_code == 200:
        print("ccminer URL exists. Downloading...")
        download_ccminer(ccminer_url)
    else:
        print("ccminer URL does not exist.")
else:
    print("Error: Could not find CPU model information.")
