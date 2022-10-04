#!/usr/bin/python3.8
from setuptools import setup
from distutils.util import convert_path
import codecs

# Load version information
main_ns = {}
ver_path = convert_path('crawler/__init__.py')
with codecs.open(ver_path, 'rb', 'utf8') as ver_file:
    exec(ver_file.read(), main_ns)

install_requires = ['requests~=2.28.1']

setup(
    name=main_ns['__name__'],
    version=main_ns['__version__'],
    author=main_ns['__author__'],
    author_email=main_ns['__author_email__'],
    description='API Crawler',
    license='',
    platforms=['Any'],
    keywords=['mongodb', 'openaq'],
    url='',
    packages=['crawler',
              'crawler.wrappers',
              'crawler.helpers',
              'crawler.wrappers.openaqapi'],
    zip_safe=False,
    include_package_data=True,
    install_requires=install_requires,
    entry_points={},
    test_suite='tests'
)
