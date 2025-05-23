# building as application as a package
'''
In Python, setup.py is a module used to build and distribute Python packages. It typically contains information about the package, such as its name, version, and dependencies, as well as instructions for building and installing the package
'''
from setuptools import setup, find_packages
from typing import List

def get_requirements(file_path: str) -> List[str]:
    '''
    This function will return the list of requirements
    '''
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace('\n', '') for req in requirements]
        
        if '-e .' in requirements:
            requirements.remove('-e .')
    
    return requirements


setup(
    
    name='mlproject',
    version='0.1',
    author='Monalika Pingale',
    author_email='monalikapingale480@gmail.com',
    description='Building a machine learning project',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt'),
    
)