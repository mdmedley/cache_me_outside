from setuptools import setup
from sys import version_info

__version__ = '0.1'

requirements = []
# If Python version is lower than 3.2 require backports.functools_lru_cache
if version_info < (3, 2):
    requirements = ['backports.functools_lru_cache']

description = 'A package that makes caching fun! How about that?'


setup(
    name='cache_me_outside',
    version=__version__,
    description=description,
    long_description=description,
    author='Marcus Medley',
    author_email='mdmeds@gmail.com',
    license='MIT',
    py_modules=['cache_me_outside'],
    install_requires=[requirements],
    setup_requires=['pytest-runner'],
    tests_requires=['pytest'],
    keywords=['cache', 'caching', 'python cache'],
    url='https://github.com/mdmedley/cache_me_outside',
    classifiers=(
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Libraries',
        'Topic :: Utilities'
    ))
