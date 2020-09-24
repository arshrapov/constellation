import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()


setuptools.setup(
    name='constellation',
    version="0.0.1",
    author="Raphael",
    author_email="ashrapov.rafa@yande.com",
    description="Modelling of space Object in space Systems",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/arshrapov/constellation",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU v2.1 License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)