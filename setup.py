import setuptools

with open("README.md","r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="HelloWorld",
    version="0.0.0",
    author="Santiago Lopez",
    author_email="Santiago.Lopez@usherbrooke.ca",
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 2-3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=['numpy','pybind11'],
    packages=setuptools.find_packages(),
    include_package_data=True,
    zip_safe=False
)
