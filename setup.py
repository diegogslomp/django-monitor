import os
from setuptools import setup

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-monitor',
    version='0.1',
    packages=['monitor'],
    include_package_data=True,
    license='Apache 2 License',
    description='A simple Web-based Django app to monitor linux hosts.',
    long_description=README,
    url='https://github.com/chonpz28/django-monitor/',
    author='Diego G. Slomp',
    author_email='diegogslomp@gmail.com',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: IT Administrators',
        'License :: Apache 2 License',
        'Operating System :: Linux',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4.2',
        'Programming Language :: Python :: 3.4.3',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
    keywords='monitor services linux',
    install_requires=[
        'Django>=1.7',
        'paramiko'
    ],
)
