import pathlib

from setuptools import find_packages, setup

from misc.version import VERSION

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="fake-http-header",
    version=VERSION,
    description="Generates random request fields for a http request header",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/MichaelTatarski/fake-http-header",
    author="Michael Tatarski",
    author_email="michaeltatarski@yahoo.de",
    license="MIT",
    python_requires=">=3.6",
    packages=find_packages(),
    include_package_data=True,
    package_data={"": ["data/*.json"]},
    install_requires=[
        'importlib_resources; python_version<"3.9"',
    ],
)
