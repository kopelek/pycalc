import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pycalc-kkopel",
    version="0.0.1",
    author="Krzysztof Kopel",
    author_email="krzysztof_kopel@epam.com",
    description="Pure Python calculator.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/kopelek/pycalc",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
