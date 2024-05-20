from setuptools import setup, find_packages
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()
with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = fh.read()
setup(
    name = 'mytool',
    version = '1.0.0',
    author = 'my cool thing',
    author_email = 'zacharyj@bitsyncdev.com',
    license = 'IDNC',
    description = 'forme',
    long_description = long_description,
    long_description_content_type = "text/markdown",
    url = 'https://git.bitsyncdev.com/Extraskilled56/MyTool.git',
    py_modules = ['my_tool', 'app'],
    packages = find_packages(),
    install_requires = [requirements],
    python_requires='>=3.7',
    classifiers=[
        "Programming Language :: Python :: 3.8",
        "Operating System :: OS Independent",
    ],
    entry_points = '''
        [console_scripts]
        cooltool=my_tool:cli
    '''
)