echo Installing dependencies

sudo apt update
sudo apt upgrade -y
sudo apt install pip -y
sudo apt install git -y
pip install setuptools
pip install setuptools --break-system-packages #this is for some machines
pip install click==7.1.2
pip install click==7.1.2 --break-system-pacakges #this is for some machines


echo Setting up files and directorys

cd /usr/bin/
sudo mkdir poss
cd poss
sudo mkdir installed-pkgs
cd ~

echo Cloning the repository


cd /usr/bin/poss/
git clone -b working https://git.bitsyncdev.com/bit-sync/Poss-v2
cd /usr/bin/poss/Poss-v2
git clone https://pindex.bitsyncdev.com/poss-package-index/pindex.git

echo Installing Poss-v2

cd /usr/bin/poss/Poss-v2
sudo python3 setup.py develop

echo Poss verifying poss is installed

poss version