import feedparser
import argparse
import configparser
import requests
import datetime
from bs4 import BeautifulSoup as bs
import os
from pyhtml2pdf import converter

# Name of application
app_name = 'RSS READER'
# Version of application
app_version = '0.14'


class CmdParser:
    """
    Class for parsing arguments in cmd user input
    and output variables values as objects
    """

    def __init__(self):
        pass

    @staticmethod
    def input_parser():
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
        parser.add_argument('--date', action='store', type=lambda s: datetime.datetime.strptime(s, '%Y%m%d'),
                            help="Date in YYYYMMDD format for printing news topics from the cache")
        parser.add_argument('--to-html', action='store', type=str,
                            help="Path and name of saved html file with rss feed")
        parser.add_argument('--to-pdf', action='store', type=str,
                            help="Path and name of saved pdf file with rss feed")
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
        if output.source is None:
            if self.date() is None:
                err_text = "RSS READER: error: the following arguments are required: source"
                print(err_text)
                raise SystemExit(0)
        else:
            return output.source

    def date(self):
        """
        Method for return cmd arg --date value
        """
        output = self.input_parser()
        if output.date is not None:
            date = str(output.date)
            sdate = date.split(" ")
            return str(sdate[0])
        else:
            return 0

    def to_html(self):
        """
        Method for return cmd arg --to-html value
        """
        output = self.input_parser()
        if output.to_html is not None:
            self.check_path(output.to_html)
            path = str(output.to_html)
            return str(path)
        else:
            return 0

    def to_pdf(self):
        """
        Method for return cmd arg --to-pdf value
        """
        output = self.input_parser()
        if output.to_pdf is not None:
            self.check_path(output.to_pdf)
            path = str(output.to_pdf)
            return str(path)
        else:
            return 0

    @staticmethod
    def check_path(path):
        try:
            f = open(path, 'w')
            f.close()
        except:
            err_text = "RSS READER: error: output file path received incorrect path"
            print(err_text)
            raise SystemExit(0)


class RssFeed:
    """
    Class for parsing news in rss feed
    and output it in json or text
    """

    def __init__(self, s_link, limit):
        """
        s_link - link to rss feed
        limit - int value with limit of output
        """
        self.s_link = s_link
        self.limit = limit

    def parce(self):
        """
        Method for parse rss feed with
        feedparser lib, also this method
        write feed to cache file
        """
        parse_feed = feedparser.parse(self.s_link)
        self.cache_file_write()
        return parse_feed

    def parce_cache(self):
        """
        Method for parse rss feed with
        feedparser lib from cache file
        """
        try:
            self.cache_file_write()
        except:
            if self.s_link is not None:
                print("RSS READER: warning: can't connect to RSS source")
            else:
                print("RSS READER: use --help")
                raise SystemExit(0)
        cache_file = self.config_parser()
        parse_feed = feedparser.parse(cache_file)
        return parse_feed

    @staticmethod
    def error_msg(name, verbose):
        """
        Methode for print error message about absence key in feed.
        name - name of error value of rss feed;
        verbose - value for show this error message or not.
        """
        if verbose:
            message = "RSS READER: error: the following key absence in RSS feed: " + name
            print(message)
        else:
            pass
        status = 'pass'
        return status

    def news_source(self, item, verbose, file=0, json=False):
        """
        Method for print source of news from rss feed.
        item - part of rss feed;
        verbose - value for err_msg method;
        file - value for create or not file output;
        json - value for create or not json output.
        """
        try:
            message = "Source: " + item.source.title
            if file == 0:
                if json is not True:
                    print(message)
            return item.source.title
        except:
            self.error_msg('source', verbose)
            return None

    def news_title(self, item, verbose, file=0, json=False):
        """
        Method for print title of news from rss feed.
        verbose - value for err_msg method;
        file - value for create or not file output;
        json - value for create or not json output.
        """
        try:
            message = "Title: " + item.title
            if file == 0:
                if json is not True:
                    print(message)
            return item.title
        except:
            self.error_msg('title', verbose)
            return None

    def news_date(self, item, verbose, file=0, json=False):
        """
        Method for print publish date of news from rss feed.
        verbose - value for err_msg method;
        file - value for create or not file output;
        json - value for create or not json output.
        """
        try:
            message = "Date: " + item.published
            if file == 0:
                if json is not True:
                    print(message)
            return item.published
        except:
            self.error_msg('date', verbose)
            return None

    def news_link(self, item, verbose, file=0, json=False):
        """
        Method for print link to news from rss feed.
        verbose - value for err_msg method;
        file - value for create or not file output;
        json - value for create or not json output.
        """
        try:
            message = "Link:" + item.link
            if file == 0:
                if json is not True:
                    print(message)
            return item.link
        except:
            self.error_msg('link', verbose)
            return None

    @staticmethod
    def space(file=0, json=False):
        """
        Method for print space.
        file - value for create or not file output
            (if file != 0 - space not will be print);
        json - value for create or not json output
            (if json == True - space not will be print).
        """
        message = "   "
        if json is False:
            if file == 0:
                print(message)
        status = 'pass'
        return status

    @staticmethod
    def error_source():
        """
        Method for print user visible message about source error.
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
        try:
            response = requests.get(self.s_link)
            cache_file = open(self.config_parser(), 'a+b')
            if response.content not in cache_file.read():
                cache_file.write(response.content)
            else:
                pass
            cache_file.close()
        except:
            pass

    def split_url(self):
        """
        Method for return source url without https:// and sublinks.
        """
        if self.s_link is not None:
            url = str(self.s_link)
            surl = url.split("/")
            return surl[2]
        else:
            return None

    def print_item_cmd(self, item, verbose, file=0, json=False):
        """
        Method for print items of RSS feed in cmd output.
        item - part of rss feed;
        verbose - value for err_msg method;
        file - value for create or not file output;
        json - value for create or not json output.
        """
        src = self.news_source(item, verbose, file, json)
        title = self.news_title(item, verbose, file, json)
        pub_date = self.news_date(item, verbose, file, json)
        link = self.news_link(item, verbose, file, json)
        self.space(file, json)
        html = self.rss2html(src, title, pub_date, link)
        return html

    def print_info(self, verbose, date=0, source=None, file=0, json=False):
        """
        Method for print all(or some number with limit)
        news from rss feed.
        item - part of rss feed;
        verbose - value for err_msg method;
        date - value for finding news with date in cache,
            if date=0 output will be from rss source via link;
        source - value for the source link of rss feed,
            if source=None output will be only from cache;
        file - value for create or not file output;
        json - value for create or not json output.
        """
        html_str = ""
        if source is not None:
            if date == 0:
                feed = self.parce()
            else:
                feed = self.parce_cache()
        else:
            feed = self.parce_cache()
        if len(feed.entries) > 0:
            for item in feed.entries[:self.limit]:
                if self.split_url() is not None:
                    if self.split_url() in str(item.link):
                        if date != 0:
                            if str(date) in item.published:
                                x = self.print_item_cmd(item, verbose, file, json)
                                if file != 0:
                                    html_str += str(x)
                        else:
                            x = self.print_item_cmd(item, verbose, file, json)
                            if file != 0:
                                html_str += str(x)
                else:
                    if date != 0:
                        if str(date) in item.published:
                            x = self.print_item_cmd(item, verbose, file, json)
                            if file != 0:
                                html_str += str(x)
        else:
            self.error_source()
        status = 'pass'
        if file != 0:
            self.print_html(html_str, file)
        return status

    def print_json(self, date=0, source=None):
        """
        Method for print all(or some number with limit)
        news from rss feed in json format.
        date - value for finding news with date in cache,
            if date=0 output will be from rss source via link;
        source - value for the source link of rss feed,
            if source=None output will be only from cache;
        """
        if source is not None:
            if date == 0:
                feed = self.parce()
            else:
                feed = self.parce_cache()
        else:
            feed = self.parce_cache()
        if len(feed.entries) > 0:
            for item in feed.entries[:self.limit]:
                if self.split_url() is not None:
                    if self.split_url() in str(item):
                        if date != 0:
                            if str(date) in str(item):
                                print(item)
                        else:
                            print(item)
                else:
                    if date != 0:
                        if str(date) in str(item):
                            print(item)
        else:
            self.error_source()
        status = 'pass'
        return status

    @staticmethod
    def config_file_test():
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

    @staticmethod
    def config_file_rewrite():
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
        Method for parsing config file rss_reader.cfg.
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

    @staticmethod
    def rss2html(src, title, pub_date, link):
        """
        Format rss feed item to html by template.
        title - value with title of item from rss feed;
        pub_date - value for finding news with date in cache,
            if date=0 output will be from rss source via link;
        link - value for the source link of rss feed,
            if source=None output will be only from cache;
        """
        template = """\
        <h2 class='title'>{title}</h2>\
        <a class='link' href='{link}'>{title}</a>\
        <br>\
        <span class='description'>{source}</span>\
        <br>\
        <span class='date'>{date}</span>\
        <br>"""
        return template.format(title=title, link=link, source=src, date=pub_date)

    @staticmethod
    def print_html(info, path):
        """
        Method for create html output from RSS feed.
        info - rss feed after rss2html method;
        path - path to html file by user.
        """
        f = open(path, 'w')
        f.write(bs(info, 'lxml').prettify())
        f.close()

    @staticmethod
    def convert_to_pdf(input_html, output_path):
        """
        Method for create pdf output from RSS feed.
        input_html - input html file;
        output_path - path and name for output pdf file.
        """
        path = os.path.abspath(input_html)
        converter.convert(f'file:///{path}', output_path)

    @staticmethod
    def remove_tmp(tmp_file):
        """
        Method for remove tmp files.
        """
        os.remove(tmp_file)


def start():
    """
    Main function for start and work rss reader.
    """

    cmd_args = CmdParser()
    news = RssFeed(cmd_args.source(), cmd_args.limit())
    date = cmd_args.date()
    source = cmd_args.source()
    file = cmd_args.to_html()
    pdf = cmd_args.to_pdf()

    def create_pdf():
        """
        Function for create pdf file from tmp html.
        """
        tmp_file = 'tmp.html'
        news.print_info(verbose, date, source, tmp_file, json)
        news.convert_to_pdf('tmp.html', pdf)
        news.remove_tmp('tmp.html')

    if cmd_args.json() is not True:
        json = False
        if cmd_args.verbose() is True:
            verbose = True
            if pdf == 0:
                news.print_info(verbose, date, source, file, json)
            else:
                create_pdf()
        else:
            verbose = False
            if pdf == 0:
                news.print_info(verbose, date, source, file, json)
            else:
                create_pdf()
    else:
        json = True
        news.print_json(date, source)
        if cmd_args.verbose() is True:
            verbose = True
            if pdf == 0:
                news.print_info(verbose, date, source, file, json)
            else:
                create_pdf()
        else:
            verbose = False
            if pdf == 0:
                news.print_info(verbose, date, source, file, json)
            else:
                create_pdf()
