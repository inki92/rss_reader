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
        'feedparser==6.0.10',
        'async-generator==1.10',
        'attrs==22.1.0',
        'beautifulsoup4==4.11.1',
        'bs4==0.0.1',
        'certifi==2022.6.15',
        'cffi==1.15.1',
        'charset-normalizer==2.1.1',
        'colorama==0.4.5',
        'feedparser==6.0.10',
        'h11==0.13.0',
        'idna==3.3',
        'outcome==1.2.0',
        'pdfkit==1.0.0',
        'pycparser==2.21',
        'pyhtml2pdf==0.0.5',
        'PySocks==1.7.1',
        'python-dotenv==0.21.0',
        'requests==2.28.1',
        'selenium==4.4.3',
        'sgmllib3k==1.0.0',
        'sniffio==1.3.0',
        'sortedcontainers==2.4.0',
        'soupsieve==2.3.2.post1',
        'tqdm==4.64.1',
        'trio==0.21.0',
        'trio-websocket==0.9.2',
        'urllib3==1.26.12',
        'webdriver-manager==3.8.3',
        'wsproto==1.2.0',
        'coverage==6.4.4',
        'iniconfig==1.1.1',
        'packaging==21.3',
        'pluggy==1.0.0',
        'py==1.11.0',
        'pyparsing==3.0.9',
        'pytest==7.1.3',
        'pytest-runner',
        'pytest-cov==3.0.0',
        'pytest-mock==3.8.2',
        'tomli==2.0.1'
    ],
    tests_require=[
        'pytest',
    ],
    test_suite='tests',

)
