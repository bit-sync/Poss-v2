# This script installs Poss v2


# Installing dependencies

sudo apt install pip -y
sudo apt install git -y


pip install setuptools
pip install setuptools --break-system-packages
pip install setuptools --upgrade

pip install click==7.1.2
pip install click==7.1.2 --break-system-packages


git clone https://git.bitsyncdev.com/bit-sync/Poss-v2.git

cd Poss-v2

sudo python3 setup.py develop

## Poss has now been installed!