import json
from code.key_presser import KeyPresser
from code.keyboard_layout import KeyboardLayout


with open('data/standard_t9_map.json') as r:
    standard_map = json.load(r)

st9 = KeyboardLayout(standard_map)


def test_travel_speed():
    """Travel speed added correctly."""
    kp = KeyPresser(1.0, 1.0, 1.0)
    assert kp.time_between('a', 'd', st9) == 1.0
    assert kp.time_between('a', ' ', st9) == 3.0

    kp = KeyPresser(2.0, 1.0, 1.0)
    assert kp.time_between('a', 'd', st9) == 0.5
    assert kp.time_between('a', ' ', st9) == 1.5


def test_repeat_delay():
    """Repeat delay added correctly."""
    kp = KeyPresser(1.0, 1.0, 1.0)
    assert kp.time_between('a', 'e', st9) == 2.0
    assert kp.time_between('a', '0', st9) == 4.0

    kp = KeyPresser(1.0, 1.5, 1.0)
    assert kp.time_between('a', 'e', st9) == 2.5
    assert kp.time_between('a', '0', st9) == 4.5


def test_key_cooldown():
    """Key cooldown added correctly."""
    kp = KeyPresser(1.0, 1.0, 1.0)
    assert kp.time_between('a', 'a', st9) == 1.0
    assert kp.time_between(' ', ' ', st9) == 1.0

    kp = KeyPresser(1.0, 1.0, 2.0)
    assert kp.time_between('a', 'a', st9) == 2.0
    assert kp.time_between(' ', ' ', st9) == 2.0
