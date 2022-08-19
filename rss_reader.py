import feedparser
import argparse

class cmd_parser:

    def __init__(self):
        pass

    def input_parser(self):

        parser = argparse.ArgumentParser(prog='PROG')

        parser.add_argument('-v', '--version', action='version', version='%(prog)s 1.0',
                    help="Print version info")
        parser.add_argument('--json', action='store_true',
                    help="Print result as JSON in stdout")
        parser.add_argument('--verbose', action='store_true',
                    help="Outputs verbose status messages")
        parser.add_argument('--limit', action='store', type=int,
                    help="Limit news topics if this parameter provided")
        parser.add_argument('source', action='store', type=str,
                    help="RSS URL")

        args = parser.parse_args()

        return args

    def json(self):
        output = self.input_parser()
        return output.json

    def verbose(self):
        output = self.input_parser()
        return output.verbose

    def limit(self):
        output = self.input_parser()
        return output.limit

    def source(self):
        output = self.input_parser()
        return output.source



class rss_feed:

    def __init__(self, s_link, limit):
        self.s_link = s_link
        self.limit = limit

    def parce(self):
        return feedparser.parse(self.s_link)

    def news_source(self, item):
        print("Source: ", item.source.title)

    def news_title(self,item):
        print("Title: ",item.title)

    def news_date(self, item):
        print("Date: ",item.published)

    def news_link(self, item):
        print("Link:", item.link)

    def space(self):
        print("   ")

    def print_info(self):
        feed = self.parce()
        for item in feed.entries[:self.limit]:
            self.news_source(item)
            self.news_title(item)
            self.news_date(item)
            self.news_link(item)
            self.space()

    def print_json(self):
        feed = self.parce()
        print(feed.entries[:self.limit])



if __name__ == '__main__':
    cmd_args = cmd_parser()
    news = rss_feed(cmd_args.source(), cmd_args.limit())
    news.print_info()




