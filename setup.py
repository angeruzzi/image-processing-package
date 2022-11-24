from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="package_name",
    version="0.0.1",
    author="Alessandro Angeruzzi",
    author_email="alessandro@angeruzzi.com.br",
    description="My short description",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="https://github.com/angeruzzi/image-processing-package",
    packages= find_packages(),
    instal_requires=requirements.txt,
    python_requires='>=3.8'
)