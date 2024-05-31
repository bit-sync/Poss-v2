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
    installpkg.install(package)
    return 0


#TODO Test this and fix any bugs!
@cli.command()
@click.argument('package')
def run(package):
    runpkg.run(package)
    return 0
    
  
#TODO Test this and fix any bugs!
@cli.command()
@click.argument('package')
def uninstall(package):
    if poss:
        os.system("sudo bash /usr/bin/poss/Poss-v2/pindex/pycalculate/remove.sh")
        return 0
    
        
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
    
    
#TODO Test this and fix any bugs!
  
@cli.command
@click.option("-p", "--package", "package")
@click.option('--poss', is_flag=True)
def upgrade(poss, package):
    if poss:
        os.system("git merge")
        return 0
    upgradepkg.upgrade(package)

    

    

    

    
