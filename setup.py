# coding: utf-8

import sys
from setuptools import setup, find_packages

NAME = "swagger_server"
VERSION = "1.0.0"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = [
    "connexion",
    "swagger-ui-bundle>=0.0.2"
]

setup(
    name=NAME,
    version=VERSION,
    description="Regression - OpenAPI 3.0",
    author_email="apinyarr@gmail.com",
    url="",
    keywords=["Swagger", "Regression - OpenAPI 3.0"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['swagger/swagger.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['swagger_server=swagger_server.__main__:main']},
    long_description="""\
    This is Inclass Activity 1 on [Moodle](https://moodle.cestarcollege.com/moodle/mod/assign/view.php?id&#x3D;1430966).  Some useful links: - [Building and testing Python - GitHub Docs](https://docs.github.com/en/actions/automating-builds-and-tests/building-and-testing-python)
    """
)
