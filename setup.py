import os
from setuptools import setup

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-monitor',
    version='0.1.3',
    packages=['monitor'],
    include_package_data=True,
    license='MIT License',
    description='A simple Web-based Django app to monitor hosts.',
    long_description=README,
    url='https://github.com/chonpz28/django-monitor/',
    author='Diego Gobbi Slomp',
    author_email='diegogslomp@gmail.com',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django:: 1.9',
        'Framework :: Django:: 1.10',
        'Intended Audience :: System Administrators',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: System :: Monitoring',
        'Topic :: System :: Networking :: Monitoring',
    ],
    keywords='monitor services linux',
    install_requires=[
        'Django',
        'paramiko'
    ],
)
