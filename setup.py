import os
from setuptools import setup, find_packages

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "extjs",
    version = read('extjs/static/extjs/version.txt'),
    packages = find_packages(),
    url = "https://github.com/akimboio/django-extjs",
    description = read('README.md'),
    include_package_data = True,
    zip_safe = False
)
