from setuptools import setup, find_packages

def install_requires():
    with open('requirements.txt', 'r') as f:
        return [line.strip() for line in f.readlines()]

setup(
    name='sphinx-summaries',
    version='0.0.3',
    packages=['sphinx-summaries'],
    install_requires=install_requires()
)
