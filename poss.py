import click
import os
import sys
sys.path.insert(1, 'pindex/install.py')
sys.path.insert(1, 'pindex/update.py')
sys.path.insert(1, 'pindex/upgrade.py')
sys.path.insert(1, 'pindex/uninstall.py')
sys.path.insert(1, 'pindex/run.py')
import pindex.install as installpkg # type: ignore
import pindex.update as updatepkg # type: ignore
import pindex.upgrade as upgradepkg # type: ignore
import pindex.uninstall as uninstallpkg # type: ignore
import pindex.run as runpkg # type: ignore
@click.group()
def cli():
    pass 

@cli.command()
@click.argument('package')
def install(package):
    print("updating the package index")
    os.system("cd /usr/bin/poss/Poss-v2/pindex && sudo git pull")
    print("installing the package") 
    installpkg.install(package)
    return 0


@cli.command()
@click.argument('package')
def run(package):
    runpkg.run(package)
    return 0
    
  

@cli.command()
@click.argument('package')
def uninstall(package):
    if package == "poss":
        print("Uninstalling poss")
        os.system("sudo rm -rf /usr/bin/poss")
        print("Uninstalled poss")
    else:
        uninstallpkg.uninstall(package)
    
        
@cli.command()
def version():
    print("Version 0.7.0")

@cli.command
@click.argument('package')
def update(package):
    print("updating the package index")
    os.system("cd /usr/bin/poss/Poss-v2/pindex && sudo git pull") 
    print("updating package")
    if package == "poss":
        os.system("cd /usr/bin/poss/Poss-v2 && sudo git fetch")
        print("Run `poss upgrade poss` to finish updating poss")
    else:
        updatepkg.update(package)
    
  
@cli.command
@click.argument("package")
def upgrade(package): 
    print("upgrading package")
    if package == "poss":
        os.system("cd /usr/bin/poss/Poss-v2 && sudo git merge")
        print("Upgraded poss to new version")
    else:
        upgradepkg.upgrade(package)
        
#TODO make command, "list"

@cli.command()
def list():
    print("Listing...")
    os.system("cd /usr/bin/poss/installed-pkgs")
    os.system("ls")