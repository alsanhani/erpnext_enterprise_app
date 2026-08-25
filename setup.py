from setuptools import setup, find_packages

setup(
    name="my_custom_app",
    version="1.0.0",
    packages=find_packages(),
    include_package_data=True,
    install_requires=["frappe"],
)
