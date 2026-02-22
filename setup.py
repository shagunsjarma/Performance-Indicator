from setuptools import setup, find_packages

HYPEN_E_DOT = '-e .'
def get_requirements(path = 'requirements.txt'):
    requirements = []
    with open(path) as file:
        requirements = file.readlines()
        requirements = [req.replace('/n', ' ') for req in requirements]
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    return requirements
        
    

setup(
    name='Performance Indicator',
    version = '0.0.1',
    author='Shagun Sharma',
    author_email='shagunsharma029@gmail.com',
    packages=find_packages(),
    install_requires= get_requirements()
)