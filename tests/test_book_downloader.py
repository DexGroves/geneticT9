from code.book_downloader import BookDownloader


def test_strip_unicode():
    """priority calculated correctly for standard T9."""
    bd = BookDownloader

    assert bd.strip_unicode('\xa3') == ''
    assert bd.strip_unicode('abc') == 'abc'
    assert bd.strip_unicode('\xa3abc\xa3') == 'abc'
