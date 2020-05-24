sudo apt-get install -y python3-venv libpcap-dev

if [ ! -d "venv" ]; then
  python3 -m venv ./venv
fi

source ./venv/bin/activate

sudo setcap cap_net_raw=eip $(readlink -f $(which python3))
sudo setcap cap_net_raw=eip $(which tcpdump)

python3 -m pip install -r requirements.txt
python3 -m pip install -e lanscan-0.9.5/
