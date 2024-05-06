from setuptools import find_packages,setup
from typing import List

def fetch_requirements(file_path:str) -> List[str]:
    
    """ 
    This function will the list of requirements
    Args:
        str
    Returns:
        list: ['str']

    """
    HYPEN_E_DOT='-e .'

    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]
        
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    
    return requirements

setup(
name='End2EndML',
version='0.0.1',
author='Abdulrahman Iyaniwura',
author_email='adebolarahman@gmail.com',
packages=find_packages(),
install_requires=  fetch_requirements('requirements.txt') 

)