import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="inspirational_quotes",
    version="0.0.3",
    author="saip007",
    author_email="saip4622@outlook.com",
    description="inspirational quotes package",
    license='MIT',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/saip007/inspirational_quotes",
    keywords=["quotes","python","development"],
    install_requires=['ujson'],
    platforms = ['any'],
    packages=setuptools.find_packages(include=['inspirational_quotes', 'inspirational_quotes.*']),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)