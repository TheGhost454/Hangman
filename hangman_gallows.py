""" Hangman gallows """

__GALLOWS = [r"""
 +--+
 |  |
    |
    |
    |
    |
=====
""",
             r"""
 +--+
 |  |
 O  |
    |
    |
    |
=====
""",
             r"""
 +--+
 |  |
 O  |
 |  |
    |
    |
=====
""",
             r"""
 +--+
 |  |
 O  |
/|  |
    |
    |
=====
""",
             r"""
 +--+
 |  |
 O  |
/|\ |
    |
    |
=====
""",
             r"""
 +--+
 |  |
 O  |
/|\ |
/   |
    |
=====
""",
             r"""
 +--+
 |  |
 O  |
/|\ |
/ \ |
    |
=====
"""]


def draw(missed_letter_count):
    """
    Draws the gallows based on the value of the parameter.  Use a parameter value of 0 to draw the
    initial gallows without a hangman.

    :param missed_letter_count: the number of times the user guessed a letter incorrectly
    :type missed_letter_count: int
    :rtype: None
    """
    print(__GALLOWS[missed_letter_count])
