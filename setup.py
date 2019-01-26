from setuptools import setup, find_packages, tests_require, packages, name

with open("README", 'r') as f:
    long_description = f.read()

setup = (
    name='Linkbox',
    version='1.0',
    description='Generates a JSON object containing link preview information by passing a URL parameter.',
    long_description=long_description,
    author='Todd Birchard',
    author_email='toddbirchard@gmail.com',
    url="https://github.com/toddbirchard/linkbox",
    packages=['/', 'tests'],
    tests_require=["pytest"],
    cmdclass={"pytest": PyTest},
    install_requires=[
        "bs4",
        "flask",
        "requests"
    ]
)
