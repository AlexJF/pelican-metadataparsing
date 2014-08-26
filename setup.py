from os.path import abspath, dirname, join, normpath
from setuptools import setup

with open('README.rst') as f:
    long_description = f.read()

setup(

    # Basic package information:
    name = 'pelican-metadataparsing',
    version = '0.1.0',
    py_modules = ('metadataparsing',),

    # Packaging options:
    zip_safe = False,
    include_package_data = True,

    # Package dependencies:
    install_requires = ['pelican>=3.4.0'],

    # Metadata for PyPI:
    author = 'Alexandre Fonseca',
    author_email = 'alexandrejorgefonseca@gmail.com',
    license = 'Apache',
    url = 'https://github.com/AlexJF/pelican-metadataparsing',
    download_url = 'https://github.com/AlexJF/pelican-metadataparsing/archive/v0.1.0.zip',
    keywords = 'pelican blog static metadata parser',
    description = ('Allow definition of custom metadata parsers for Pelican'
            ' content'),
    long_description = long_description
)
