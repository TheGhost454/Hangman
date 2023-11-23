import hangman as hangman


def test_word_has_2_trailing_blanks():
    assert hangman.get_guessed_word('jog', 'tjz') == 'j_ _ '


def test_word_has_2_leading_blanks():
    assert hangman.get_guessed_word('jog', 'rdg') == '_ _ g'


def test_word_has_all_blanks():
    assert hangman.get_guessed_word('jog', 'rdf') == '_ _ _ '
