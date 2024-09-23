from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT='-e .'
def get_requirements(file_path:str)->List[str]:
    '''
    this function will return the list og requirements
       
    '''
    requrements=[]
    with open(file_path) as file_obj:
        requrements=file_obj.readlines()
        requrements=[req.replace("\n" ,"")for req in requrements]

        if HYPEN_E_DOT in requrements:
            requrements.remove(HYPEN_E_DOT)
    return requrements


setup(
    name='mlProject',
    version='0.01',
    author='glory',
    author_email='jemimahkodamalla@gmail.com',
    packages=find_packages(),
    install_requeires=get_requirements('requirements.txt')
)

