import feedparser
import argparse
import configparser
import requests

# Name of application
app_name = 'RSS READER'
# Version of application
app_version = '0.09'

class CmdParser:
    """
    Class for parsing arguments in cmd user input
    and output variables values as objects
    """

    def __init__(self):
        pass

    def input_parser(self):
        """
        Method for parse arguments in cmd user input
        """

        parser = argparse.ArgumentParser(prog=str(app_name))

        parser.add_argument('-v', '--version', action='version',
                            version=str(app_name + ' v.' + app_version),
                            help="Print version info")
        parser.add_argument('--json', action='store_true',
                            help="Print result as JSON in stdout")
        parser.add_argument('--verbose', action='store_true',
                            help="Outputs verbose status messages")
        parser.add_argument('--limit', action='store', type=int,
                            help="Limit news topics if this parameter provided")
        parser.add_argument('--date', action='store', type=int,
                            help="Date in %Y%m%d format for printing news topics from the cache")
        parser.add_argument('source', nargs='?', action='store', type=str,
                            help="RSS URL")

        args = parser.parse_args()
        return args

    def json(self):
        """
        Method for return cmd arg --json value
        (for output in json)
        """
        output = self.input_parser()
        return output.json

    def verbose(self):
        """
        Method for return cmd arg --verbose value
        (for verbose output in console)
        """
        output = self.input_parser()
        return output.verbose

    def limit(self):
        """
        Method for return cmd arg --limit value
        (number of news in output)
        """
        output = self.input_parser()
        return output.limit

    def source(self):
        """
        Method for return cmd arg --source value
        (link to rss feed)
        """
        output = self.input_parser()
        if output.source == None:
            err_text = "RSS READER: error: the following arguments are required: source"
            print(err_text)
            raise SystemExit(0)
        else:
            return output.source


class RssFeed:
    """
    Class for parsing news in rss feed
    and output it in json or text
    """

    def __init__(self, s_link, limit):
        self.s_link = s_link
        self.limit = limit


    def parce(self):
        """
        Method for parse rss feed with
        feedparser lib
        """
        parse_feed = feedparser.parse(self.s_link)
        return parse_feed

    def parce_cache(self):
        """
        Method for parse rss feed with
        feedparser lib
        """
        self.cache_file_write()
        cache_file = self.config_parser()
        parse_feed = feedparser.parse(cache_file)
        return parse_feed


    def error_msg(self, name, verbose):
        """
        Methode for print error message about absence key in feed
        """
        if verbose:
            message = "RSS READER: error: the following key absence in RSS feed: " + name
            print(message)
        else:
            pass
        status = 'pass'
        return status

    def news_source(self, item, verbose):
        """
        Method for print source of news from rss feed
        """
        try:
            message = "Source: " + item.source.title
            print(message)
        except:
            self.error_msg('source', verbose)

    def news_title(self, item, verbose):
        """
        Method for print title of news from rss feed
        """
        try:
            message = "Title: " + item.title
            print(message)
        except:
            self.error_msg('title', verbose)

    def news_date(self, item, verbose):
        """
        Method for print publish date of news from rss feed
        """
        try:
            message = "Date: " + item.published
            print(message)
        except:
            self.error_msg('date', verbose)

    def news_link(self, item, verbose):
        """
        Method for print link to news from rss feed
        """
        try:
            message = "Link:" + item.link
            print(message)
        except:
            self.error_msg('link', verbose)

    def space(self):
        """
        Method for print space
        """
        message = "   "
        print(message)
        status = 'pass'
        return status

    def error_source(self):
        """
        Method for print user visible message about source error
        """
        message = "RSS READER: error: reading RSS feed. Check the source."
        print(message)
        status = 'pass'
        return status

    def cache_file_test(self):
        """
        Method for open cache file or create it if file when doesn't exist.
        """
        try:
            cache_path = self.config_parser()
            cache = open(cache_path, "a+")
            cache.close()
            return cache
        except:
            print("RSS READER: error: cache file", cache_path, "can't be created!")
            raise SystemExit(0)


    def cache_file_write(self):
        """
        Method for write news feed to cache file.
        """
        self.cache_file_test()
        response = requests.get(self.s_link)
        cache_file = open(self.config_parser(), 'a+b')
        if response.content not in cache_file.read():
            cache_file.write(response.content)
        else:
            pass
        cache_file.close()

    def split_url(self):
        """
        Method for return source url without https:// and sublinks
        """
        url = str(self.s_link)
        surl = url.split("/")
        return surl[2]

    def print_info(self, verbose, date=0):
        """
        Method for print all(or some number with limit)
        news from rss feed
        """
        if date == 0:
            feed = self.parce()
        else:
            feed = self.parce_cache()
        if len(feed.entries) > 0:
            for item in feed.entries[:self.limit]:
                if self.split_url() in str(item.link):
                    self.news_source(item, verbose)
                    self.news_title(item, verbose)
                    self.news_date(item, verbose)
                    self.news_link(item, verbose)
                    self.space()
        else:
            self.error_source()
        status = 'pass'
        return status


    def print_json(self, date=0):
        """
        Method for print all(or some number with limit)
        news from rss feed in json format
        """
        if date == 0:
            feed = self.parce()
        else:
            feed = self.parce_cache()

        if len(feed.entries) > 0:
            for item in feed.entries[:self.limit]:
                if self.split_url() in str(item):
                    print(item)
        else:
            self.error_source()
        status = 'pass'
        return status


    def config_file_test(self):
        """
        Method for open config file or create it if file when doesn't exist.
        """
        try:
            config = open("rss_reader.cfg", "a+")
            config.close()
            return config
        except:
            print("RSS READER: error: config file rss_reader.cfg can't be created!")
            raise SystemExit(0)


    def config_file_rewrite(self):
        """
        Method for rewrite config file.
        """
        try:
            config = open("rss_reader.cfg", "w")
            config.close()
            return config
        except:
            print("RSS READER: error: config file rss_reader.cfg can't be created!")
            raise SystemExit(0)


    def config_parser(self):
        """
        Method for parsing config file rss_reader.cfg
        """
        self.config_file_test()
        config = configparser.ConfigParser()
        try:
            config.read("rss_reader.cfg")
        except:
            self.config_file_rewrite()
            config.read("rss_reader.cfg")

        if 'paths' in config:
            try:
                cache_path = config['paths']['cache_path']
            except:
                print("RSS READER: error: config file. Variable cache_path doesn't exist.")
                raise SystemExit(0)
            return cache_path
        else:
            config.add_section('paths')
            config['paths']['cache_path'] = 'cache_feed'
            with open('rss_reader.cfg', 'w') as configfile:
                config.write(configfile)
            cache_path = config['paths']['cache_path']
            return cache_path


def start():
    """
    Main function for start and work rss reader
    """

    cmd_args = CmdParser()
    news = RssFeed(cmd_args.source(), cmd_args.limit())
    if cmd_args.json() != True:
        if cmd_args.verbose() == True:
            verbose = True
            news.print_info(verbose)
        else:
            verbose = False
            news.print_info(verbose)
    else:
        news.print_json()
    news.split_url()




