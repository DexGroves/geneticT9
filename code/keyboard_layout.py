from __future__ import division
import numpy as np


class KeyboardLayout(object):
    """Represent a T9 keyboard and its important properties."""

    def __init__(self, layout_dictionary):
        self.layout = layout_dictionary

    def priority(self, letter):
        """
        Return how many times the key must be pressed to get the
        desired letter.
        """
        button, priority = self.layout[letter]
        n_higher = len([k for (k, p) in self.layout.values()
                        if k == button and p < priority])
        return n_higher

    def distance(self, letter, prev_letter):
        """Return thumb travel distance between two letters."""
        cur, _ = self.layout[letter]
        prev, _ = self.layout[prev_letter]

        # 0 is positioned as if it were 11
        if cur == 0:
            cur = 11
        if prev == 0:
            prev = 11

        hoz_distance = np.abs((cur-1) % 3 - (prev-1) % 3)
        vert_distance = np.abs(np.floor((cur-1)/3) - np.floor((prev-1)/3))

        return np.sqrt(hoz_distance**2 + vert_distance**2)

    def get_button(self, letter):
        """Get the button associated with a letter."""
        return self.layout[letter][0]
