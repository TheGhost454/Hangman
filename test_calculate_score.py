import hangman as hangman


def test_1_duplicate_letters():
    assert hangman.calculate_score(1, "odo") == 2


def test_2_duplicate_letters():
    assert hangman.calculate_score(1, "oddo") == 2


def test_no_duplicate_letters():
    assert hangman.calculate_score(1, "castle") == 6


def test_no_duplicate_letters_score_greater_than_1():
    assert hangman.calculate_score(3, "castle") == 18


def test_2_letter_word_score_greater_than_1():
    assert hangman.calculate_score(4, "ad") == 8


def test_3_letter_word_2_duplicate_letters():
    assert hangman.calculate_score(6, "add") == 12
