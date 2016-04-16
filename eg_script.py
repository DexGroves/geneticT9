from __future__ import division
import collections
import json

from code.book_downloader import BookDownloader
from code.keyboard_layout import KeyboardLayout
from code.key_presser import KeyPresser


def book_to_most_common_tuples(book):
    letter_tuples = [(book[i], book[i+1]) for i in xrange(len(book) - 1)]
    grped_tups = collections.Counter(letter_tuples)
    return grped_tups.most_common()


with open('data/standard_t9_map.json') as r:
    standard_map = json.load(r)

war_and_peace_url = 'http://www.gutenberg.org/cache/epub/2600/pg2600.txt'


# Download the book
book = BookDownloader().download(war_and_peace_url, standard_map.keys())

# Figure out how common letter tuples are
com_tups = book_to_most_common_tuples(book)

# Standard T9 layout
st9 = KeyboardLayout(standard_map)

# Figure out how long it takes someone with these stats to reproduce W&P
kp = KeyPresser(10, 0.2, 0.5)


def evaluate_fitness(tuple_counter, keypresser, layout):
    total = 0
    for ((prev, cur), times) in tuple_counter:
        total += kp.time_between(prev, cur, layout) * times

    return total

evaluate_fitness(com_tups, kp, st9)
