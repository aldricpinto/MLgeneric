from setuptools import find_packages,setup
from typing import *

HYPHEN_CONST="-e ."
def get_req(path:str) -> List[str]:
    # returns list of requirements
    requirements = []
    with open(path) as file_obj:
        requirements = file_obj.readlines()
        requirements =[req.replace("\n","") for req in requirements]
    if "-e ." in requirements:
        requirements.remove("-e .")
    
    return requirements


setup(
    name="mlproject",
    version="1.1.1",
    author="Aldric",
    author_email="aldric878@gmail.com",
    packages=find_packages(),
    install_requires=get_req('requirements.txt')
)