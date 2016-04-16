import urllib2


class BookDownloader(object):
    """
    Download a book and parse out any nastiness that can't be
    represented by a supplied set of keys.
    """

    def __init__(self):
        pass

    def download(self, book_url, allowed_chars):
        data = urllib2.urlopen(book_url)
        book = data.read()

        book = book.replace("\n", " ")
        book = self.strip_unicode(book)
        book = book.lower()
        book = ''.join([letter for letter in book if letter in allowed_chars])

        return book

    @staticmethod
    def strip_unicode(book):
        return book.decode('unicode_escape').encode('ascii', 'ignore')
