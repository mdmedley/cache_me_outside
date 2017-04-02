from setuptools import setup

__version__ = '0.1'

description = 'A package that wraps functools_lru_cache with a fun name'


setup(
    name='cache_me_outside',
    version=__version__,
    description=description,
    long_description=description,
    author='Marcus Medley',
    author_email='mdmeds@gmail.com',
    license='MIT',
    py_modules=['cache_me_outside'],
    install_requires=['backports.functools_lru_cache', 'setuptools'],
    setup_requires=['pytest-runner'],
    tests_requires=['pytest'],
    keywords=['functools', 'lru_cache', 'cache', 'python 2.7 cache'],
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
