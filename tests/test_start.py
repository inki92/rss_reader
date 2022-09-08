import rss_reader.core

# Default values
json = False
verbose = False
limit = 1
date = 0
to_html = None
to_pdf = None
source = "https://news.yahoo.com/rss/"


class MockCmdParser:
    """
    Class for mocking input_parser method of CmdParser class
    """
    def __init__(self, json, verbose, limit, date, to_html, to_pdf, source):
        self.json = json
        self.verbose = verbose
        self.limit = limit
        self.date = date
        self.to_html = to_html
        self.to_pdf = to_pdf
        self.source = source


def test_start(mocker):
    """
    Test for json method(True)
    """
    mock_now = mocker.patch("rss_reader.core.CmdParser.input_parser")
    mock_now.return_value = MockCmdParser(json, verbose, limit, date, to_html, to_pdf, source)
    test_cmd = rss_reader.core.start()
    assert test_cmd is None

