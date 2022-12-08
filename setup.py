from setuptools import setup, find_packages


with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='consolidate_subdirectories',
    version='0.1.0',
    description='Allows for moving of files of a similar type (video, picture, ect.) to be moved from subdirectories up to a root',
    long_description=readme,
    author='Erik Liubakka',
    author_email='erik.liubakka97@gmailcom',
    url='https://github.com/eliubakk/consolidate_subdirectories',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)