from setuptools import setup, find_packages
from codecs import open  # To use a consistent encoding
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the relevant file
with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='hellowebapp-deploy',
    version='1.0.5',
    description="Packages needed to deploy to Heroku using Hello Web App's tutorial.",
    url='https://github.com/hellowebapp/hellowebapp-deploy',
    download_url='https://github.com/hellowebbooks/hellowebapp-deploy/archive/v1.0.5.tar.gz',
    author='Tracy Osborn',
    author_email='tracy@limedaring.com',
    license='MIT',
    classifiers=[
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3.6',
        'License :: OSI Approved :: MIT License',
    ],
    keywords='deployment heroku hellowebapp',
    packages=find_packages(exclude=['contrib', 'docs', 'tests*']),
    install_requires = [
        'waitress==2.0.0',
        'dj-database-url==0.5.0',
        'whitenoise==5.2.0',
    ],
)
