import pytest
import rss_reader

def test_rss_feed_error_msg():
    """
    Test for error_msg(special status = pass)
    """
    test_cmd = rss_reader.rss_feed('http://lorem-rss.herokuapp.com/feed?unit=year', 1)
    assert test_cmd.error_msg('test') == 'pass'

def test_rss_feed_news_source():
    """
    Test for news_source(method is callable)
    """
    test_cmd = rss_reader.rss_feed('http://lorem-rss.herokuapp.com/feed?unit=year', 1)
    assert test_cmd.news_source('test') == None

def test_rss_feed_news_title():
    """
    Test for news_title(method is callable)
    """
    test_cmd = rss_reader.rss_feed('http://lorem-rss.herokuapp.com/feed?unit=year', 1)
    assert test_cmd.news_title('test') == None

def test_rss_feed_news_date():
    """
    Test for news_date(method is callable)
    """
    test_cmd = rss_reader.rss_feed('http://lorem-rss.herokuapp.com/feed?unit=year', 1)
    assert test_cmd.news_date('test') == None

def test_rss_feed_news_link():
    """
    Test for news_link(method is callable)
    """
    test_cmd = rss_reader.rss_feed('http://lorem-rss.herokuapp.com/feed?unit=year', 1)
    assert test_cmd.news_link('test') == None

def test_rss_feed_space():
    """
    Test for feed_space(special status = pass)
    """
    test_cmd = rss_reader.rss_feed('http://lorem-rss.herokuapp.com/feed?unit=year', 1)
    assert test_cmd.space() == 'pass'

def test_rss_error_source():
    """
    Test for error_source(special status = pass)
    """
    test_cmd = rss_reader.rss_feed('http://lorem-rss.herokuapp.com/feed?unit=year', 1)
    assert test_cmd.error_source() == 'pass'

def test_rss_print_info():
    """
    Test for print_info(special status = pass)
    """
    test_cmd = rss_reader.rss_feed('http://lorem-rss.herokuapp.com/feed?unit=year', 1)
    assert test_cmd.print_info() == 'pass'

def test_rss_print_json():
    """
    Test for print_json(special status = pass)
    """
    test_cmd = rss_reader.rss_feed('http://lorem-rss.herokuapp.com/feed?unit=year', 1)
    assert test_cmd.print_json() == 'pass'











