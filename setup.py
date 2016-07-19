from setuptools import setup, find_packages


setup(
    name='manifestor',
    maintainer='Eric Moritz',
    maintainer_email='eric.moritz@gmail.com',
    url='https://github.com/ericmoritz/python-manifestor',
    version='0.1.0',
    packages=find_packages(),
    scripts=['bin/manifestor'],
    install_requires=[
        'pureyaml >=0.1.0, <1',
        'pyld >=0.7.1, < 1',
        'fp >= 0.2, < 1',
        'jsonpointer >= 1.10, < 2',
        'docopt >= 0.6.2, < 1',
        'behave >= 1.2.5, < 2',
        'testfixtures >= 4.10.0, < 5',
        'pytest >= 2.9.2, < 3',
        'pytest-pep8 >= 1.0.6, < 2',
    ]
)
