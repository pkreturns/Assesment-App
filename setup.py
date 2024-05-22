from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in assessment_app/__init__.py
from assessment_app import __version__ as version

setup(
	name="assessment_app",
	version=version,
	description="assesment app",
	author="Nijith",
	author_email="nijithanil501",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
