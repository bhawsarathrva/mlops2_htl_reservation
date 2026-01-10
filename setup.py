from setuptools import setup,find_packages

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="MLOPS2_htl_reservation",
    version="0.1",
    author="Athrva Bhawsar",
    packages=find_packages(),
    install_requires = requirements,
)
