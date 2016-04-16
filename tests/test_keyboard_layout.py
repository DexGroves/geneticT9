import json
import numpy as np
from code.keyboard_layout import KeyboardLayout


with open('data/standard_t9_map.json') as r:
    standard_map = json.load(r)

st9 = KeyboardLayout(standard_map)


def test_priority():
    """priority calculated correctly for standard T9."""
    assert st9.priority('a') == 0
    assert st9.priority('b') == 1
    assert st9.priority('c') == 2

    assert st9.priority('p') == 0
    assert st9.priority('q') == 1
    assert st9.priority('r') == 2
    assert st9.priority('s') == 3

    assert st9.priority(' ') == 0


def test_distance():
    """distance between keys calculated correctly for standard T9."""
    assert st9.distance('a', 'b') == 0
    assert st9.distance('a', 'c') == 0
    assert st9.distance('a', 'd') == 1
    assert st9.distance('a', ' ') == 3
    assert st9.distance('a', 'm') == np.sqrt(2)
