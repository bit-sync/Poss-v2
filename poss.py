import click
import os
import sys
sys.path.insert(1, 'package_index/')
import package_index.install as installpkg

@click.group()
def cli():
    pass

@cli.command()
@click.argument('package')
def install(package):
    installpkg(package)

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
    print("Version 0.5.5")
    
@cli.command
@click.option("-p", "--package", "package")
def update(package): 
    pass