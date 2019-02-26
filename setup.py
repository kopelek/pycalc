from setuptools import setup, find_packages
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()
  
setup(
    name='pycalc-kkopel',
    version='0.0.1',
    author='Krzysztof Kopel',
    author_email='krzysztof_kopel@epam.com',
    description='Pure Python calculator.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    python_requires='>=3.6',
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    entry_points={
        'console_scripts': [
            'pycalc = pycalc.__main__:main',
        ],
    },
    project_urls={
        'Source Code': 'https://github.com/kopelek/pycalc',
        'Test Pypi': 'https://test.pypi.org/project/pycalc-kkopel',
    },
)
