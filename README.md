# rss_reader
RSS feed reader

# Description
Python command line utility for downloading and parsing RSS feed

## Common requirements
    python >= 3.9

# Installation
For install unpack archive with package and run:

    # python3 setup.py install

# Tests
For run tests before building package

    # python setup.py test 

# Build 
For build package from source code:

    # python setup.py sdist

# How to use

    usage: RSS READER [-h] [-v] [--json] [--verbose] [--limit LIMIT] [source]
    
    positional arguments:
      source         RSS URL
    
    options:
      -h, --help     show this help message and exit
      -v, --version  Print version info
      --json         Print result as JSON in stdout
      --verbose      Outputs verbose status messages
      --limit LIMIT  Limit news topics if this parameter provided
