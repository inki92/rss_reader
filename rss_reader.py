import feedparser
import argparse

# Name of application
app_name = 'RSS READER'
# Version of application
app_version = '0.02'


# CHANGELOG
# 19.08.22 v.0.01 Add doc strings. Create start function.
# 19.08.22 v.0.02 Add error_source method of rss_feed class. Add requirements.txt.
# 22.08.22 v.0.03 fix: Add None value bypass for source method value in cmd_parser.
#                 Add error_msg method. Add exceptions for absence keys.

class cmd_parser:
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
        parser.add_argument('source',  nargs='?', action='store', type=str,
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


class rss_feed:
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
        return feedparser.parse(self.s_link)

    def error_msg(self, name):
        """
        Methode for print error message about absence key in feed
        """
        print("RSS READER: error: the following key absence in RSS feed: ", name)


    def news_source(self, item):
        """
        Method for print source of news from rss feed
        """
        try:
            print("Source: ", item.source.title)
        except:
            self.error_msg('source')

    def news_title(self, item):
        """
        Method for print title of news from rss feed
        """
        try:
            print("Title: ", item.title)
        except:
            self.error_msg('title')

    def news_date(self, item):
        """
        Method for print publish date of news from rss feed
        """
        try:
            print("Date: ", item.published)
        except:
            self.error_msg('date')

    def news_link(self, item):
        """
        Method for print link to news from rss feed
        """
        try:
            print("Link:", item.link)
        except:
            self.error_msg('link')

    def space(self):
        """
        Method for print space
        """
        print("   ")

    def error_source(self):
        """
        Method for print user visible message about source error
        """
        print("RSS READER: error: reading RSS feed. Check the source.")

    def print_info(self):
        """
        Method for print all(or some number with limit)
        news from rss feed
        """
        feed = self.parce()
        if len(feed.entries) > 0:
            for item in feed.entries[:self.limit]:
                self.news_source(item)
                self.news_title(item)
                self.news_date(item)
                self.news_link(item)
                self.space()
        else:
            self.error_source()

    def print_json(self):
        """
        Method for print all(or some number with limit)
        news from rss feed in json format
        """
        feed = self.parce()
        if len(feed.entries) > 0:
            print(feed.entries[:self.limit])
        else:
            self.error_source()


def start():
    """
    Main function for start and work rss reader
    """

    cmd_args = cmd_parser()
    news = rss_feed(cmd_args.source(), cmd_args.limit())
    if cmd_args.json() != True:
        news.print_info()
    else:
        news.print_json()


if __name__ == '__main__':
    start()
