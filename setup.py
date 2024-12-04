from setuptools import setup, find_packages

setup(
    name="advent-of-code-sample",
    version="0.1",
    description="isthistechsupport's solutions for https://adventofcode.com/",
    url="https://github.com/isthistechsupport/advent-of-code",
    author="Diego Rivero",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Topic :: Games/Entertainment :: Puzzle Games",
    ],
    install_requires=[
        "advent-of-code-data >= 0.8.0",
        # list your other requirements here, for example:
        # "numpy", "parse", "networkx",
    ],
    packages=find_packages(),
    entry_points={
        "adventofcode.user": ["isthistechsupport = mypackage:mysolve"],
    },
)