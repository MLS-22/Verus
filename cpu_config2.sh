#!/bin/bash

echo "Script started."

# Check if wget is installed
if ! command -v wget &> /dev/null; then
    echo "Error: wget is not installed. Please install it and try again."
    exit 1
fi

echo "wget command found."

# Check if lscpu command is available
if ! command -v lscpu &> /dev/null; then
    echo "Error: lscpu command not found. This script requires lscpu to detect CPU model."
    exit 1
fi

echo "lscpu command found."

# Get CPU model information
cpu_info=$(lscpu | grep "Model name")

echo "CPU model information retrieved: $cpu_info"

# Function to download ccminer based on URL
download_ccminer() {
    echo "Downloading ccminer from: $1"
    wget "$1"
}

# Check CPU model and download ccminer accordingly
case "$cpu_info" in
    *"Cortex-A53"*)
        if [[ $cpu_info == *"Cortex-A72"* ]]; then
            echo "Downloading ccminer for Cortex-A72."
            download_ccminer "https://raw.githubusercontent.com/Darktron/pre-compiled/a73-a53/ccminer"
        elif [[ $cpu_info == *"Cortex-A73"* ]]; then
            echo "Downloading ccminer for Cortex-A73."
            download_ccminer "https://raw.githubusercontent.com/Darktron/pre-compiled/a73-a53/ccminer"
        else
            echo "Downloading ccminer for Cortex-A53."
            download_ccminer "https://raw.githubusercontent.com/Darktron/pre-compiled/a53/ccminer"
        fi
        ;;
    *"Cortex-A55"*)
        if [[ $cpu_info == *"Cortex-A75"* ]]; then
            echo "Downloading ccminer for Cortex-A75."
            download_ccminer "https://raw.githubusercontent.com/Darktron/pre-compiled/a75-a55/ccminer"
        else
            echo "Unsupported CPU model detected: $cpu_info"
            read -p "Do you want to download the generic ccminer? (y/n): " choice
            case "$choice" in 
                y|Y) 
                    echo "Downloading generic ccminer."
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
        ;;
    *)
        echo "Unsupported CPU model detected: $cpu_info"
        read -p "Do you want to download the generic ccminer? (y/n): " choice
        case "$choice" in 
            y|Y) 
                echo "Downloading generic ccminer."
                download_ccminer "https://raw.githubusercontent.com/Darktron/pre-compiled/generic/ccminer"
                ;;
            n|N)
                echo "No action taken. Exiting."
                ;;
            *)
                echo "Invalid choice. Exiting."
                ;;
        esac
        ;;
esac

echo "Script completed."
