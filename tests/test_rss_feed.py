import os.path
from rss_reader.core import RssFeed

# Default values
test_obj = RssFeed('https://news.yahoo.com/rss/', 1)
name = 'test'
verbose = True
item = 'test'


def test_error_msg():
    """
    Test for error_msg method(special status = pass)
    """
    test_cmd = test_obj.error_msg(name, verbose)
    assert test_cmd == 'pass'


def test_news_source():
    """
    Test for news_source method(callable)
    """
    test_cmd = test_obj.news_source(item, verbose)
    assert test_cmd is None


def test_news_title():
    """
    Test for news_title method(callable)
    """
    test_cmd = test_obj.news_title(item, verbose)
    assert test_cmd is None


def test_news_date():
    """
    Test for news_date method(callable)
    """
    test_cmd = test_obj.news_date(item, verbose)
    assert test_cmd is None


def test_news_link():
    """
    Test for news_link method(callable)
    """
    test_cmd = test_obj.news_link(item, verbose)
    assert test_cmd is None


def test_error_source():
    """
    Test for error_source method(special status = pass)
    """
    test_cmd = test_obj.error_source()
    assert test_cmd == 'pass'


def test_split_url():
    """
    Test for split_url method(special status = 'news.yahoo.com')
    """
    test_cmd = test_obj.split_url()
    assert test_cmd == 'news.yahoo.com'


def test_print_item_cmd():
    """
    Test for print_item_cmd method(return item != None)
    """
    test_cmd = test_obj.print_item_cmd(item, verbose)
    assert test_cmd is not None


def test_print_info():
    """
    Test for print_info method(special status = pass)
    """
    test_cmd = test_obj.print_info(item, verbose)
    assert test_cmd == 'pass'


def test_print_json():
    """
    Test for print_json method(special status = pass)
    """
    test_cmd = test_obj.print_json()
    assert test_cmd == 'pass'


def test_config_parser():
    """
    Test for config_parser method(default value = cache_feed)
    """
    test_cmd = test_obj.config_parser()
    assert test_cmd == 'cache_feed'


def test_rss2html():
    """
    Test for rss2html method(return item != None)
    """
    test_cmd = test_obj.rss2html('src', 'title', 'pub_date', 'link')
    assert test_cmd is not None


def test_convert_to_pdf():
    """
    Test for convert_to_pdf method(callable module)
    """
    f = open("test.html", 'w')
    f.close()
    test_obj.convert_to_pdf('test.html', 'test.pdf')
    test_cmd = os.path.exists('test.pdf')
    os.remove('test.pdf')
    assert test_cmd is True


def test_parse():
    """
    Test for parse method(return item != None)
    """
    test_cmd = test_obj.parce()
    assert test_cmd is not None


def test_parce_cache():
    """
    Test for parce_cache method(return item != None)
    """
    test_cmd = test_obj.parce_cache()
    assert test_cmd is not None
