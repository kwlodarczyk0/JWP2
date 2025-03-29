from setuptools import setup, find_packages
setup(
    name="geompy",
    version="0.1.0",
    author="Krystian Włodarczyk",
    packages=find_packages(),
    install_requires=[
        "numpy>=1.26",
        "requests"
    ],
)