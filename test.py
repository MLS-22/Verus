#!/usr/bin/env python3
import subprocess
import requests

# Function to download ccminer
def download_ccminer(url):
    subprocess.run(["wget", url])

# Get CPU model information
# cpu_info = subprocess.check_output(["lscpu"]).decode("utf-8")
# cpu_model_line = [line for line in cpu_info.split('\n') if "Model name" in line]
cpu_model_line = ['Model name:          Cortex-A53', 'Model name:          Cortex-A72']
cpu_numbers = [line.split()[-1].split('-')[1].lower() for line in cpu_model_line]
print(f"Your CPU: {cpu_numbers}", end="\n\n\n")
      
if len(cpu_numbers) > 0:
    ccminer_url = f"https://raw.githubusercontent.com/Darktron/pre-compiled/{cpu_numbers[1]}-{cpu_numbers[0]}/ccminer"
    response = requests.head(ccminer_url)
    if response.status_code == 200:
        print("ccminer URL exists. Downloading...")
        download_ccminer(ccminer_url)
    else:
        read = input("File not find, do you want to download default file ?")
        if read == 'y':
            ccminer_url = f"https://raw.githubusercontent.com/Darktron/pre-compiled/default/ccminer"
            response = requests.head(ccminer_url)

        print("ccminer URL does not exist.")
else:
    print("Error: Could not find CPU model information.")
