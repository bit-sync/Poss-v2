### Installing dependencies

sudo apt update
sudo apt upgrade -y
sudo apt install pip -y
sudo apt install git -y
pip install setuptools
pip install setuptools --break-system-packages #this is for some machines
pip install click==7.1.2
pip install click==7.1.2 --break-system-pacakges #this is for some machines


### Setting up files and directorys

cd /usr/bin/
sudo mkdir poss
cd poss
sudo mkdir installed-pkgs
cd ~
### Cloning the repository


cd /usr/bin/poss/
git clone https://git.bitsyncdev.com/bit-sync/Poss-v2

### Installing Poss-v2

cd Poss-v2
sudo python3 setup.py develop

### Poss verifying poss is installed

poss version