from setuptools import find_packages, setup

setup(
    # Needed to silence warnings (and to be a worthwhile package)
    name='base30',
    url='https://github.com/timwilson/base30',
    author='Tim Wilson',
    author_email='tim@savvytechgroup.com',
    # Needed to actually package something
    packages=find_packages(include['base30']),
    # Needed for dependencies
    install_requires=[''],
    # *strongly* suggested for sharing
    version='0.1',
    # The license can be anything you like
    license='MIT',
    description='A library to convert between decimal and a special form of base30.',
    long_description=open('README.md').read(),
)
