# _*_ coding: utf-8 _*_

# Third
from setuptools import find_packages, setup

__version__ = "0.1.0"
__description__ = "Python API Restful test"

__author__ = "Dheinny Marques"
__author_email__ = "dheinny@gmail.com"
testing_extras = [
    "pytest",
    "pytest-cov"
]

setup(
    name="api",
    version=__version__,
    author=__author__,
    author_email=__author_email__,
    packages=find_packages(),
    license="MIT",
    description=__description__,
    url="https://github.com/Dheinny/python_restful_api.git",
    keywords="API, Restful, Flask",
    include_package_data=True, 
    zip_safe=False,
    classifiers=[
        "Intended Audience :: Interviewers"
        "Operation System :: OS Independent",
        "Topic :: Software Development",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.6",
        "License :: OSI Approved :: MIT License",
    ],
    setup_requires=["pytest-runner"],
    tests_require=["pytest"],
    extras_require={
        "testing": testing_extras,
    },
)

