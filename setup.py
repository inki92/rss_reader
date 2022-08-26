from setuptools import setup, find_packages
from os.path import join, dirname
import rss_reader

setup(
    name='rss_reader',
    version=rss_reader.__version__,
    packages=find_packages(),
    long_description=open(join(dirname(__file__), 'README.md')).read(),
    entry_points={
        'console_scripts':
            ['rss_reader = rss_reader.core:start']
    },
    install_requires=[
        'feedparser==6.0.10'
    ],
    test_suite='tests',

)
