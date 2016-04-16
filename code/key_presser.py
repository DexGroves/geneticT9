class KeyPresser(object):
    """
    Represents a user who will take time to interact with
    a keyboard layout.
    """

    def __init__(self, travel_speed, repeat_delay, key_cooldown):
        """
        travel_speed: how quickly they cover one unit of
            cartesian distance between keys.
        repeat_delay: delay between successive presses
            towards producing one letter.
        key_cooldown: delay when next letter exists on
            the same key.
        """
        self.travel_speed = travel_speed
        self.repeat_delay = repeat_delay
        self.key_cooldown = key_cooldown

    def time_between(self, prev, cur, layout):
        """
        Compute time to finish producing current key based
        on previous key and layout.
        """
        elapsed = layout.distance(cur, prev) / self.travel_speed

        elapsed += layout.priority(cur) * self.repeat_delay

        if layout.get_button(cur) == layout.get_button(prev):
            elapsed += self.key_cooldown

        return elapsed
