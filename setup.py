from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in walk_in/__init__.py
from walk_in import __version__ as version

setup(
	name="walk_in",
	version=version,
	description="yashjyoti",
	author="Vp",
	author_email="vaibhav.parmar@syscort.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
