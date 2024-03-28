from setuptools import setup, find_packages

setup(
    name='ISA-API',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        # Your library dependencies
    ],
    author='Yiqiao11',
    author_email='vanilla.att@gmail.com',
    description='This library is to combine some strategies under realistic scenarios with information structures and algorithms',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/ISA-API/ISA-API',
)
