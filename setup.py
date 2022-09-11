from setuptools import setup

setup(
    name="mobi2cbz",
    version="1.1",
    author="Melano",
    url="https://github.com/1b0325h/mobi2cbz",
    py_modules=["mobi2cbz"],
    install_requires=[
        "beautifulsoup4==4.9.3",
        "fire==0.4.0",
        "mobi==0.3.3"],
    entry_points={"console_scripts": ["mobi2cbz = mobi2cbz:main"]})
