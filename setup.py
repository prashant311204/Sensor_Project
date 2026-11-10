from setuptools import find_packages, setup
from typing import List

def get_requirements(file_path: str) -> List[str]:
    """
    This function will return the list of requirements
    """
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n", "") for req in requirements]
        
       # yadi requirements.txt me '-e .' mauzud hai to usko remove kr dega......
        if "-e ." in requirements:
            requirements.remove("-e .")
            
    return requirements

setup(
    name='Fault detection',
    version='0.0.1',
    author='Prashant Kumar Puri',
    author_email='prashantkumarpuri1@gmail.com',
    install_requires=get_requirements('requirements.txt'),
    packages=find_packages()
)