from setuptools import setup, find_packages

setup(
    name="pdfmaster",
    version="0.1",
    packages=find_packages(),
    url="https://github.com/ensarkaya/pdfmaster",
    license="MIT",
    author="Ensar Kaya",
    author_email="ensarben@gmail.com",
    description="A Python library for converting office files to PDF using the iLovePDF API",
    install_requires=[
        "requests",
    ],
)
