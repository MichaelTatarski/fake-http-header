import pathlib
from setuptools import setup, find_packages

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="fake-http-header",
    version="0.1",
    description="Generates random request fields for a http header",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/realpython/fake-http-header",
    author="Michael Tatarski",
    author_email="michaeltatarski@yahoo.de",
    license="MIT",
    python_requires=">=3.6",
    packages=find_packages(),
    include_package_data=True,
    package_data={"": ["data/*.json"]},
)
