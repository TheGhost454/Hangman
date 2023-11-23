import hangman as hangman


def test_no_letters_guessed_returns_all_letters():
    assert hangman.get_available_letters('') == hangman.ALL_LETTERS


def test_returns_letters_not_guessed():
    assert hangman.get_available_letters('cl') == 'abdefghijkmnopqrstuvwxyz'


def test_all_letters_guessed_returns_empty_string():
    guessed = hangman.ALL_LETTERS
    assert hangman.get_available_letters(guessed) == ''


def test_capitial_letters_guessed_returns_letters_not_guessed():
    assert hangman.get_available_letters('AZ') == 'bcdefghijklmnopqrstuvwxy'
