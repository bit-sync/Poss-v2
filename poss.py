import click
import inspkgs as inspkgs
import runpkgs as runpkgs
import rmpkgs as rmpkgs
import os

@click.group()
def cli():
    pass

@cli.command()
@click.argument('package')
def install(package):
    if package == 'pycalculate':
        inspkgs.install_pyCalculate()
    elif package == 'gitpython':
        inspkgs.install_gitpython()
    elif package == 'fgxcli':
        inspkgs.install_FusionGamesXCLI()
    else:
        print("Package not found")

@cli.command()
@click.argument('package')
def run(package):
    if package == 'pycalculate':
        runpkgs.run_pyCalculate()
    elif package == 'gitpython':
        runpkgs.run_gitpython()
    elif package == 'fgxcli':
        runpkgs.run_FusionGamesXCLI()
    else:
        print("Package not found")
        
@cli.command()
@click.argument('package')
def uninstall(package):
    if package == 'pycalculate':
        rmpkgs.run_pyCalculate()
    elif package == 'gitpython':
        rmpkgs.run_gitpython()
    elif package == 'fgxcli':
        rmpkgs.run_FusionGamesXCLI()
    else:
        print("Package not found")
        
@cli.command()
def version():
    print("Version 0.5.3")
    
@cli.command()
def setup():
    os.system("mkdir poss")
    os.system("sudo mv poss /usr/bin/")
    os.system("mkdir installed-pkgs")
    os.system("sudo mv installed-pkgs /usr/bin/poss")
    print("Setup complete! (please do not run this again, might cause issues)")
    
    