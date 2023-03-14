import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="inspirational_quotes",
    version="0.0.2",
    author="saip007",
    author_email="saip4622@outlook.com",
    description="inspirational quotes package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/saip007/inspirational_quotes",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)