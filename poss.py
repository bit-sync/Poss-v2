import click
import os
import sys
sys.path.insert(1, 'pindex/install.py')
sys.path.insert(1, 'pindex/update.py')
sys.path.insert(1, 'pindex/upgrade.py')
import pindex.install as installpkg
import pindex.update as updatepkg
import pindex.upgrade as upgradepkg
@click.group()
def cli():
    pass 

@cli.command()
@click.argument('package')
def install(package):
    installpkg.install(package)
    return 0


#TODO you need to make it so it goes to the package index folder for the function instead of it being defined here!
@cli.command()
@click.argument('package')
def run(package):
    if package == 'pycalculate':
        os.system("cd /usr/bin/poss/Poss-v2/pindex/pycalculate")
        os.system("sudo bash run.sh")
    else:
        print("Package not found")
  
#TODO you need to make it so it goes to the package index folder for the function instead of it being defined here!        
@cli.command()
@click.argument('package')
def uninstall(package):
    if package == 'pycalculate':
        os.system("sudo bash /usr/bin/poss/Poss-v2/pindex/pycalculate/remove.sh")
    else:
        print("Package not found")
        
@cli.command()
def version():
    print("Version 0.6.0")
    
#TODO Test this and fix any bugs!
@cli.command
@click.option('--poss', is_flag=True)
@click.argument('package')
def update(package, poss): 
    if poss:
        os.system("git fetch")
        print("Run `poss upgrade --poss` to upgrade your installation.")
        return 0
    installpkg.install(package)
    
    
#TODO you need to make it so it goes to the package index folder for the function instead of it being defined here!
  
@cli.command
@click.option("-p", "--package", "package")
@click.option('--poss', is_flag=True)
def upgrade(poss, package):
    if poss:
        os.system("git merge")
        return 0
    upgradepkg.upgrade(package)

    

    

    

    
