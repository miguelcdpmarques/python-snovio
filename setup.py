from setuptools import setup

setup(
    name='python-snovio',
    version="0.1.0",
    license="MIT",

    install_requires=[
        "requests",
    ],

    description='A Python wrapper around Snov.io API',
    long_description=open('README.txt').read(),

    author='Miguel Marques',
    author_email='miguelcdpmarques@gmail.com',

    url='http://github.com/miguelcdpmarques/python-snovio',
    download_url='http://github.com/miguelcdpmarques/python-snovio/downloads',

    include_package_data=True,

    packages=['snovio'],

    zip_safe=False,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
    ]
)