from setuptools import find_packages,setup
from typing import List

eDot = '-e .'
def get_requirements(file_path:str)->List[str]:
    requirements = []
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n", " ") for req in requirements]

    if eDot in requirements:
        requirements.remove(eDot)
    
    return requirements

setup(
name = 'mlProject',
version = '0.0.1',
author = 'Gautham',
author_email = "mgautham0505@gmail.com",
packages = find_packages(),
install_requires = get_requirements("requirements.txt")

)

