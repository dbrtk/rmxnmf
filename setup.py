

from setuptools import find_packages, setup


with open('requirements.txt') as _file:

    requirements = []
    for package in _file.readlines():
        package = package.strip()
        if package:
            requirements.append(package)

setup(
    name='rmxnmf',
    # version='0.1',
    description='Non-negative matrix factorisation.',
    long_description='',

    url='http://dbrtk.org',

    author='Dominik Bartkowski',
    author_email='dominik.bartkowski@gmail.com',

    classifiers=[

        'Environment :: Console',

        'Framework :: Flake8',
        'Framework :: Flask',
        'Framework :: IDLE',
        'Framework :: IPython',

        'Intended Audience :: Developers',
        'Intended Audience :: Education',
        'Intended Audience :: Science/Research',

        'Natural Language :: English',

        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.0',
        'Programming Language :: Python :: 3.1',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3 :: Only',

        'Operating System :: POSIX :: Linux',
        'Operating System :: Unix',
    ],

    keywords='nmf matrix factorisation',

    packages=find_packages(include=['rmxnmf']),

    install_requires=requirements
)
