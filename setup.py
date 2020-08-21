import os
from setuptools import setup

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-monitor',
    version='0.5.0',
    packages=['monitor'],
    include_package_data=True,
    license='MIT License',
    description='Ping devices and check router/switch port status. Useful in ring topology networks.',
    long_description=README,
    url='https://github.com/diegogslomp/django-monitor/',
    author='Diego Gobbi Slomp',
    author_email='diegogslomp@gmail.com',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: System :: Monitoring',
        'Topic :: System :: Networking :: Monitoring',
    ],
    keywords='monitor ping icmp telnet',
    install_requires=[
        'django',
        'gunicorn',
        'psycopg2',
        'whitenoise',
    ],
)
