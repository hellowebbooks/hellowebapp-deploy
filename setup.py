from setuptools import setup, find_packages
from codecs import open  # To use a consistent encoding
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the relevant file
with open(path.join(here, 'DESCRIPTION.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='hellowebapp-deploy-toolbelt',
    version='0.0.1',
    description="Packages needed to deploy to Heroku using Hello Web App's tutorial.",
    url='https://github.com/limedaring/HelloWebApp-deploy-toolbelt',
    author='Tracy Osborn',
    author_email='tracy@limedaring.com',
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 2.7',
        'License :: OSI Approved :: MIT License',
    ],
    keywords='deployment heroku',
    packages=find_packages(exclude=['contrib', 'docs', 'tests*']),
    install_requires = [
        'django',
        'gunicorn',
        'dj-database-url',
        'dj-static',
        'whitenoise',
    ],
)
