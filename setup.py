from setuptools import setup, find_packages


with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='sample',
    version='0.1.0',
    description='Sample package for Python-Guide.org',
    long_description=readme,
    author='Erik Liubakka',
    author_email='eliubakk@umich.edu',
    url='https://github.com/eliubakk/consolidate_subdirectories',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)