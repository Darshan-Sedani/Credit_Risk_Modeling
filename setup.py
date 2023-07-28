import os
from setuptools import setup,find_packages

def get_requirements(file_path:str)->List[str]:
    requirements = []
    with open(file_path) as f:
        requirements = f.readlines()
        requirements=[req.replace('\n','') for req in requirements]

    if "-e ." in requirements:
        requirements.remove("-e.")

    return requirements

setup(
    name="credit_risk",
    version="0.0.1",
    author="Darshan",
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt")
)