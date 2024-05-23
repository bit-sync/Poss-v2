import click
import os

@click.group()
def cli():
    pass

@cli.command()
@click.argument('package')
def install(package):
    if package == 'pycalculate':
        os.system("cd /usr/bin/poss/package-index/pycalculate")
        os.system("sudo bash install.sh")

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
    
@cli.command()
def setup():
    """
    os.system("mkdir poss")
    os.system("sudo mv poss /usr/bin/")
    os.system("mkdir installed-pkgs")
    os.system("sudo mv installed-pkgs /usr/bin/poss")
    print("Setup complete! (please do not run this again, might cause issues)")
    """
    