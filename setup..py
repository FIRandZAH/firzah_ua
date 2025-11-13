from setuptools import setup, find_packages

setup(
    name="firzah_ua",
    version="0.0.1",
    author="FIRandZAH",
    author_email="firmanalayk@gmail.com",
    description="Library Python sederhana untuk mengelola user agent",
    long_description=open("README.md", "r").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/FIRandZAH/firzah_ua",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.12",
)
