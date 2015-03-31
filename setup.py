import os
from setuptools import setup

with open(os.path.join(os.path.dirname(__file__), 'README.md')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-monitor',
    version='0.1',
    packages=['monitor'],
    include_package_data=True,
    license='MIT License',
    description='A simple Web-based Django app to monitor linux hosts.',
    long_description=README,
    url='https://github.com/chonpz28/django-monitor/',
    author='Diego G. Slomp',
    author_email='diegogslomp@gmail.com',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: IT Administrators',
        'License :: MIT License',
        'Operating System :: Linux',
        'Programming Language :: Python :: 2.7',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)
