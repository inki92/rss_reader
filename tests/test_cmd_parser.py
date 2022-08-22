import pytest
import rss_reader

def test_cmd_parser_json():
    """
    Test for json method(empty)
    """
    test_cmd = rss_reader.cmd_parser()
    assert test_cmd.json() == False

def test_cmd_parser_verbose():
    """
    Test for verbose method(empty)
    """
    test_cmd = rss_reader.cmd_parser()
    assert test_cmd.verbose() == False

def test_cmd_parser_limit():
    """
    Test for parser_limit method(empty)
    """
    test_cmd = rss_reader.cmd_parser()
    assert test_cmd.limit() == None

def test_cmd_parser_source():
    """
    Test for source method(when empty - SystemExit)
    """
    test_cmd = rss_reader.cmd_parser()
    with pytest.raises(SystemExit) as e:
        test_cmd.source()
    assert e.type == SystemExit
    assert e.value.code == 0





