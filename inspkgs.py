import os


# fgxcli package start
def install_FusionGamesXCLI():
    os.system("sudo git clone -b poss https://gitlab.com/fusiongames1/Fusion-Games-X-CLI.git")
    os.system("sudo mv Fusion-Games-X-CLI /usr/lib/poss-installed-pkgs/")
def run_FusionGamesXCLI():
    os.system("cd /usr/lib/poss-installed-pkgs/Fusion-Games-X-CLI")
    os.system("sudo python3 FusionGamesXCLI.py/")
# fgxcli package end

# pycal package start
def install_pyCalculate():
    os.system("sudo git clone -b main https://gitlab.com/zjones.092912/pycalculate.git")
    os.system("sudo mv pycalculate /usr/lib/poss-installed-pkgs/")
def run_pyCalculate():
    os.system("cd /usr/lib/poss-installed-pkgs/")
    os.system("sudo python3 main.py/")
# pycal package end

# gitpy package start
def install_gitpython():
    os.system("sudo git clone -b main https://gitlab.com/zjones.092912/git-python.git")
    os.system("sudo mv git-python /usr/lib/poss-installed-pkgs/")
def run_gitpython():
    os.system("cd /usr/lib/poss-installed-pkgs/git-python")
    os.system("sudo python3 git-python.py/")
# gitpy package end
