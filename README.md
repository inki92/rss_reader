# rss_reader
RSS feed reader utility.

# Version
09.09.22 v.0.14 docs: Add and edit doc strings for classes and methods. Edit README.md.

For see version of installed utility use command:
   
    # rss_reader -v

#Changelog
You can see actual changelog in file CHANGELOG in main directory of this utility.

# Description
Python command line utility is for printing in console and saving in to the files RSS feed.
The utility can work both with the installation and without installation.
The reader saves the RSS feed to the cache file for access early news or work 
without internet connection.

For start this utility without installation use a call specifying an interpreter *python3*, 
for example call utility with version option:

    # python3 rss_reader -v

After installation it will work without it, when you have interpreter in your system, for example:

    # rss_reader -v

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

    usage: RSS READER [-h] [-v] [--json] [--verbose] [--limit LIMIT] [--date DATE] [source]
    
    positional arguments:
      source            RSS URL
    
    options:
    -h, --help          show this help message and exit
    -v, --version       Print version info
    --json              Print result as JSON in stdout
    --verbose           Outputs verbose status messages
    --limit LIMIT       Limit news topics if this parameter provided
    --date DATE         Date in YYYYMMDD format for printing news topics from the cache
    --to-html TO_HTML   Path and name of saved html file with rss feed
    --to-pdf TO_PDF     Path and name of saved pdf file with rss feed


# Description of arguments and options

      source            RSS URL

Argument with link to RSS feed, for example:

    rss_reader https://news.yahoo.com/rss/

If you use it with option *--date* this argument is the value for finding
news in cache with a source like in argument.

If you do not specify this argument when using *--date* option, 
you will get the output from the cache without filtering by source.


    --json              Print result as JSON in stdout

*optional*

Option print json output in console. This option can work with addition options:

*--limit* to print some number of news, 

*--date* to find only news with some date and then print it in json, 

*--to-html* and *--to-pdf* for save news in files with json output in console.

    --limit LIMIT       Limit news topics if this parameter provided

*optional*

This option need integer format number as an argument, for example for print 
only one item from news feed it must be:
    
    --limit 1

If this option exists - utility find only some number items from rss feed, as in argument.
If number in argument more than news items in rss feed utility will be printed only this max number of news.

This option can work with other options for limit news feed.

    --verbose           Outputs verbose status messages

*optional*

If this option exists all error messages about empty news feed items like published date, 
link to source, author etc. will be printed in the console output.

    --date DATE         Date in YYYYMMDD format for printing news topics from the cache

*optional*

This option need to YYYYMMDD format date as argument, for example for 1 december 2022 this must be
    
    --date 20221201

If this option exists - utility finds only news with specified published date in cache file and
then prints them in console or write in file.

    --to-html TO_HTML   Path and name of saved html file with rss feed

*optional*

This option need path and name to html file as argument, for example:
    
    --to-html /path/to/file/example.html

If this option exists - utility print news in this html file. If path to file incorrect, 
or utility can't create it - you will see exception in console about this error.

Option also works with another options:

*--limit* to save only some number of news, 

*--date* to find only news with some date and then save it, 

*--json* for save news in files with json output in console.

    --to-pdf TO_PDF     Path and name of saved pdf file with rss feed

*optional*

This option needs path and name to pdf file as argument, for example:
    
    --to-html /path/to/file/example.pdf

If this option exists - utility prints news in this html file. If path to file incorrect, 
or utility can't create it - you will see exception in console about this error.

This option creates temporary html file in the path of start utility, then convert it to pdf with
the path and name like in argument of option and after delete temporary html file *tmp.html*.

Option also works with another options:

*--limit* to save only some number of news, 

*--date* to find only news with some date and then save it, 

*--json* for save news in files with json output in console.

# CONFIG FILE

*rss_reader.cfg*

Config file of this utility contain cache file path.
This file must be created automaticly in first start of utility in the path, when utility started.
You can change path of cache file in this file.

When utility can't create this config file - you can see error about it in console.

Default config file includes:

    [paths]
    cache_path = cache_feed

For change path of cache file edit cache_path variable(in default this is *cache_feed*)

# CACHE FILE

Cache file contains all rss feed in xml format. Default path of this 
described in paragraph *CONFIG FILE* of this manual.
When utility can't create or read this file - you can see error about it in console.

    
