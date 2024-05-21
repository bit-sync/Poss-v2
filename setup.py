from setuptools import setup, find_packages
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()
with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = fh.read()
setup(
    name = 'Poss Package Manager',
    version = '0.5.0',
    author = 'Bit Sync',
    author_email = 'software@bitsyncdev.com',
    license = 'Apache 2.0',
    description = 'A nice package manager coded in python',
    long_description = long_description,
    long_description_content_type = "text/markdown",
    url = 'https://git.bitsyncdev.com/bit-sync/Poss-v2.git',
    py_modules = ['poss', 'app'],
    packages = find_packages(),
    install_requires = [requirements],
    python_requires='>=3.7',
    classifiers=[
        "Programming Language :: Python :: 3.8",
        "Operating System :: OS Independent",
    ],
    entry_points = '''
        [console_scripts]
        poss=poss:cli
    '''
)