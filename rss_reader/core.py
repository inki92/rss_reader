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
app_version = '0.12'

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
        if output.source == None:
            if self.date() == None:
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
        if output.date != None:
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
        if output.to_html != None:
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
        if output.to_pdf != None:
            self.check_path(output.to_pdf)
            path = str(output.to_pdf)
            return str(path)
        else:
            return 0

    def check_path(self, path):
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
        self.s_link = s_link
        self.limit = limit


    def parce(self):
        """
        Method for parse rss feed with
        feedparser lib
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
            if self.s_link != None:
                print("RSS READER: warning: can't connect to RSS source")
            else:
                print("RSS READER: use --help")
                raise SystemExit(0)
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

    def news_source(self, item, verbose, file=0, json=False):
        """
        Method for print source of news from rss feed
        """
        try:
            message = "Source: " + item.source.title
            if file == 0:
                if json != True:
                    print(message)
            return item.source.title
        except:
            self.error_msg('source', verbose)
            return None

    def news_title(self, item, verbose, file=0, json=False):
        """
        Method for print title of news from rss feed
        """
        try:
            message = "Title: " + item.title
            if file == 0:
                if json != True:
                    print(message)
            return item.title
        except:
            self.error_msg('title', verbose)
            return None

    def news_date(self, item, verbose, file=0, json=False):
        """
        Method for print publish date of news from rss feed
        """
        try:
            message = "Date: " + item.published
            if file == 0:
                if json != True:
                    print(message)
            return item.published
        except:
            self.error_msg('date', verbose)
            return None

    def news_link(self, item, verbose, file=0, json=False):
        """
        Method for print link to news from rss feed
        """
        try:
            message = "Link:" + item.link
            if file == 0:
                if json != True:
                    print(message)
            return item.link
        except:
            self.error_msg('link', verbose)
            return None

    def space(self, file=0):
        """
        Method for print space
        """
        message = "   "
        if file == 0:
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
        Method for return source url without https:// and sublinks
        """
        if self.s_link != None:
            url = str(self.s_link)
            surl = url.split("/")
            return surl[2]
        else:
            return None

    def print_item_cmd(self, item, verbose, file=0, json=False):
        """
        Method for print items of RSS feed in cmd output.
        """
        src = self.news_source(item, verbose, file, json)
        title = self.news_title(item, verbose, file, json)
        pub_date = self.news_date(item, verbose, file, json)
        link = self.news_link(item, verbose, file, json)
        self.space(file)
        html = self.rss2html(src, title, pub_date, link)
        return html

    def print_info(self, verbose, date=0, source=None, file=0, json=False):
        """
        Method for print all(or some number with limit)
        news from rss feed
        """
        html_str = ""
        if source != None:
            if date == 0:
                feed = self.parce()
            else:
                feed = self.parce_cache()
        else:
            feed = self.parce_cache()
        if len(feed.entries) > 0:
            for item in feed.entries[:self.limit]:
                if self.split_url() != None:
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
        news from rss feed in json format
        """
        if source != None:
            if date == 0:
                feed = self.parce()
            else:
                feed = self.parce_cache()
        else:
            feed = self.parce_cache()
        if len(feed.entries) > 0:
            for item in feed.entries[:self.limit]:
                if self.split_url() != None:
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

    def rss2html(self, src, title, pub_date, link):
        """
        Format feed item to html
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

    def print_html(self, info, path):
        """
        Method for create html output from RSS feed
        """
        f = open(path, 'w')
        f.write(bs(info, 'lxml').prettify())
        f.close()

    def convert_to_pdf(self, input_html, output_path):
        """
        Method for create pdf output from RSS feed
        """
        path = os.path.abspath(input_html)
        converter.convert(f'file:///{path}', output_path)

    def remove_tmp(self, tmp_file):
        """
        Method for remove tmp files
        """
        os.remove(tmp_file)

def start():
    """
    Main function for start and work rss reader
    """

    cmd_args = CmdParser()
    news = RssFeed(cmd_args.source(), cmd_args.limit())
    date = cmd_args.date()
    source = cmd_args.source()
    file = cmd_args.to_html()
    pdf = cmd_args.to_pdf()

    def create_pdf():
        """
        Function for create pdf file from tmp html
        """
        news.print_info(verbose, date, source, 'tmp.html', json)
        news.convert_to_pdf('tmp.html', pdf)
        news.remove_tmp('tmp.html')

    if cmd_args.json() != True:
        json = False
        if cmd_args.verbose() == True:
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
        if cmd_args.verbose() == True:
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







