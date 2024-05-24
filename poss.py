import click
import os
import sys
sys.path.insert(1, 'pindex/install.py')
import pindex.install as installpkg

@click.group()
def cli():
    pass 

@cli.command()
@click.argument('package')
def install(package):
    installpkg.install(package)

@cli.command()
@click.argument('package')
def run(package):
    if package == 'pycalculate':
        os.system("cd /usr/bin/poss/package-index/pycalculate")
        os.system("sudo bash run.sh")
    else:
        print("Package not found")
        
@cli.command()
@click.argument('package')
def uninstall(package):
    if package == 'pycalculate':
        os.system("cd /usr/bin/poss/package-index/pycalculate")
        os.system("sudo bash remove.sh")
    else:
        print("Package not found")
        
@cli.command()
def version():
    print("Version 0.6.0")
    

@cli.command
@click.option("-p", "--package", "package")
@click.option('--poss', is_flag=True)
def update(package, poss): 
    if poss:
        os.system("git fetch")
    if package == "pycalculate":
        os.system("sudo bash /usr/bin/pindex/pycalculate/update.sh")
        
@cli.command
@click.option("-p", "--package", "package")
@click.option('--poss', is_flag=True)
def upgrade(package, poss): 
    if poss:
        os.system("git merge")
    if package == "pycalculate":
        os.system("sudo bash /usr/bin/pindex/pycalculate/upgrade.sh")
    
    

    
