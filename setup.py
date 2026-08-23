from setuptools import setup, find_packages

setup(
    name="my_custom_app",
    version="1.0.0",
    description="Enterprise ERPNext Custom Application",
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
    install_requires=["frappe"],
)
