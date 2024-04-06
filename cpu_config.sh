#!/bin/bash

# Get CPU model information
cpu_info=$(lscpu | grep "Model name")
echo $echo

# Function to download ccminer based on URL
download_ccminer() {
    wget "$1"
}

# Check CPU model and download ccminer accordingly
if [[ $cpu_info == *"Cortex-A53"* && $cpu_info == *"Cortex-A72"* ]]; then
    download_ccminer "https://raw.githubusercontent.com/Darktron/pre-compiled/a73-a53/ccminer"

elif [[ $cpu_info == *"Cortex-A53"* && $cpu_info == *"Cortex-A73"* ]]; then
    download_ccminer "https://raw.githubusercontent.com/Darktron/pre-compiled/a73-a53/ccminer"

elif [[ $cpu_info == *"Cortex-A55"* && $cpu_info == *"Cortex-A75"* ]]; then
    download_ccminer "https://raw.githubusercontent.com/Darktron/pre-compiled/a75-a55/ccminer"

elif [[ $cpu_info == *"Cortex-A53"* ]]; then
    download_ccminer "https://raw.githubusercontent.com/Darktron/pre-compiled/a53/ccminer"

else
    echo "Unsupported CPU model detected: $cpu_info"
    read -p "Do you want to download the generic ccminer? (y/n): " choice
    case "$choice" in 
        y|Y) 
            download_ccminer "https://raw.githubusercontent.com/Darktron/pre-compiled/generic/ccminer"
            ;;
        n|N)
            echo "No action taken. Exiting."
            ;;
        *)
            echo "Invalid choice. Exiting."
            ;;
    esac
fi
