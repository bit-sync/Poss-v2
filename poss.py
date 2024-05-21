import click
import packages as packages
import runpkgs as runpkgs

@click.group()
def cli():
    pass

@cli.command()
@click.argument('package')
def install(package):
    if package == 'pycalculate':
        packages.install_pyCalculate()
    elif package == 'gitpython':
        packages.install_gitpython()
    elif package == 'fgxcli':
        packages.install_FusionGamesXCLI()

@cli.command()
@click.argument('package')
def run(package):
    if package == 'pycalculate':
        runpkgs.run_pyCalculate()
    elif package == 'gitpython':
        runpkgs.run_gitpython()
    elif package == 'fgxcli':
        runpkgs.run_FusionGamesXCLI()