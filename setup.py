from setuptools import setup, find_packages

setup(
    name="kwcontributes",
    version="0.0.0",
    description="Tools for investigating Kitware's contributions to open source projects",
    author="Chris Kotfila",
    author_email="chris.kotfila@kitware.com",
    url="https://github.com/Kitware/KWContributes",
    packages=find_packages(exclude=["*.tests", "*.tests.*",
                                    "tests.*", "tests"]),
    package_data={
        "kwcontributes": ["data/*.json", "data/*.txt"],
    })
