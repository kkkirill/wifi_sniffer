# Program for checking new device connections to local networks

### How it works:
This script will print any new device detected into your local networks (like Wi-Fi).
Of course to check concrete Wi-Fi your computer should be connected to that Wi-Fi.

### Installation:

1. Install _any_ python 3 version:
   ```bash
    sudo apt-get install python3.6
   ```
2. Clone repository:
    ```bash
     git clone git@github.com:kkkirill/wifi_sniffer.git
   ```
3. Run script for creating virtual environment inside project:
   ```bash
    chmod u+x setup.sh && ./setup.sh
   ```
4. Shell into venv:
   ```bash
    source ./venv/bin/activate 
   ```
5. Run script:
   ```bash
    python main.py
   ```
