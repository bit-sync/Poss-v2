import os

# fgxcli package start
def install_FusionGamesXCLI():
    os.system("git clone -b poss https://gitlab.com/fusiongames1/Fusion-Games-X-CLI.git")
def run_FusionGamesXCLI():
    os.system("python3 Fusion-Games-X-CLI/FusionGamesXCLI.py")
# fgxcli package end

# pycal package start
def install_pyCalculate():
    os.system("git clone -b main https://gitlab.com/zjones.092912/pycalculate.git")
def run_pyCalculate():
    os.system("python3 pycalculate/main.py")
# pycal package end

# gitpy package start
def install_gitpython():
    os.system("git clone -b main https://gitlab.com/zjones.092912/git-python.git")
def run_gitpython():
    os.system("python3 git-python/git-python.py")
# gitpy package end
