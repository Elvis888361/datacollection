from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in datacollection/__init__.py
from datacollection import __version__ as version

setup(
	name="datacollection",
	version=version,
	description="data",
	author="data",
	author_email="elvisndegwa90@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
