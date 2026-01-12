from setuptools import setup,find_packages
from typing import List

def get_requirements(file_path:str)->List:

    HYPHEN_E_DOT = '-e .'
    requirements = []

    with open(file_path,'r') as file:
        requirements = file.readlines()
        requirements = [req.replace('\n',"") for req in requirements]

        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)

    return requirements

setup(
    name='Phishing Prediction ML Model',
    version= '0.0.1',
    author= 'Rutvik',
    packages=find_packages(),
    install_requires = get_requirements('requirements.txt')
)