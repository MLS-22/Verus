cpu_info=$(lscpu | grep "Model name")

# Function to download ccminer based on CPU model
download_ccminer() {
    wget "$1"
}

# Check CPU model and download ccminer accordingly
if [[ $cpu_info == *"Cortex-A53"* && $cpu_info == *"Cortex-A72"* ]]; then
    download_ccminer "https://github.com/MLS-22/Verus/blob/main/a72-a53.json"

elif [[ $cpu_info == *"Cortex-A53"* ]]; then
    download_ccminer "https://raw.githubusercontent.com/Darktron/pre-compiled/a53/ccminer"

elif [[ $cpu_info == *"Cortex-A75"* && $cpu_info == *"Cortex-A55"* ]]; then
    download_ccminer "https://github.com/MLS-22/Verus/blob/main/a73-a53.json"

else
    echo "Unsupported CPU model"
fi