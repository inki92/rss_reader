from rss_reader.core import CmdParser

test_obj = CmdParser()

# Default values
json = True
verbose = True
limit = 1
date = 20220202
to_html = True
to_pdf = True
source = 'test'


class MockInputParser:
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


def test_cmd_parser_json(mocker):
    """
    Test for json method(True)
    """
    mock_now = mocker.patch("rss_reader.core.CmdParser.input_parser")
    mock_now.return_value = MockInputParser(json, verbose, limit, date, to_html, to_pdf, source)
    test_cmd = test_obj.json()
    assert test_cmd is True


def test_cmd_parser_verbose(mocker):
    """
    Test for verbose method(True)
    """
    mock_now = mocker.patch("rss_reader.core.CmdParser.input_parser")
    mock_now.return_value = MockInputParser(json, verbose, limit, date, to_html, to_pdf, source)
    test_cmd = test_obj.verbose()
    assert test_cmd is True


def test_limit(mocker):
    """
    Test for parser_limit method(must be 1, like in defaults)
    """
    mock_now = mocker.patch("rss_reader.core.CmdParser.input_parser")
    mock_now.return_value = MockInputParser(json, verbose, limit, date, to_html, to_pdf, source)
    test_cmd = test_obj.limit()
    assert test_cmd == 1


def test_source(mocker):
    """
    Test for source method(must be 'test')
    """
    mock_now = mocker.patch("rss_reader.core.CmdParser.input_parser")
    mock_now.return_value = MockInputParser(json, verbose, limit, date, to_html, to_pdf, source)
    test_cmd = test_obj.source()
    assert test_cmd == 'test'


def test_date(mocker):
    """
    Test for date method(must be '20220202')
    """
    mock_now = mocker.patch("rss_reader.core.CmdParser.input_parser")
    mock_now.return_value = MockInputParser(json, verbose, limit, date, to_html, to_pdf, source)
    test_cmd = test_obj.date()
    assert test_cmd == '20220202'


def test_to_html(mocker):
    """
    Test for to_html method(must be 'True')
    """
    mock_now = mocker.patch("rss_reader.core.CmdParser.input_parser")
    mock_now.return_value = MockInputParser(json, verbose, limit, date, to_html, to_pdf, source)
    test_cmd = test_obj.to_html()
    assert test_cmd == 'True'


def test_to_pdf(mocker):
    """
    Test for to_pdf method(must be 'True')
    """
    mock_now = mocker.patch("rss_reader.core.CmdParser.input_parser")
    mock_now.return_value = MockInputParser(json, verbose, limit, date, to_html, to_pdf, source)
    test_cmd = test_obj.to_pdf()
    assert test_cmd == 'True'


def test_check_path():
    """
    Test for source method(must be None)
    """
    test_cmd = test_obj.check_path('test_file')
    assert test_cmd is None
