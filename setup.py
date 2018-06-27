import codecs
from setuptools import setup, find_packages

with codecs.open('README.rst', encoding='utf-8-sig') as f:
    LONG_DESCRIPTION = f.read()
    
setup(
    name='crowdflower',
    version='0.0.5',
    author='Christopher Brown',
    author_email='io@henrian.com',
    url='https://github.com/chbrown/crowdflower',
    keywords='crowdflower crowdsourcing api client',
    description='Crowdflower API - Python Client',
    long_description=LONG_DESCRIPTION,
    license=open('LICENSE').read(),
    packages=find_packages(),
    include_package_data=True,
    classifiers=[
        # https://pypi.python.org/pypi?:action=list_classifiers
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: MIT License',
    ],
    install_requires=[
        'requests>=2.0.0',
        # 'grequests',
    ],
    entry_points={
        'console_scripts': [
        ],
    },
)
