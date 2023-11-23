import hangman as hangman


def test_2_occurences_of_1_letter_in_word_returns_true():
    assert hangman.is_word_guessed('happy', 'hkydpra') is True


def test_2_occurences_of_2_letters_in_word_returns_true():
    assert hangman.is_word_guessed('prosecutes', 'kpqrolsecut') is True


def test_3_occurences_of_1_letter_in_word_returns_true():
    assert hangman.is_word_guessed('witticisms', 'jwtligmscr') is True


def test_all_but_one_letter_guessed_returns_false():
    assert hangman.is_word_guessed('wonderful', 'wnoetdfrl') is False


def test_no_letters_guessed_returns_false():
    assert hangman.is_word_guessed('car', '') is False


def test_no_letters_guessed_returns_false_using_string():
    assert hangman.is_word_guessed('car', "") is False


def test_2_letter_secret_word_returns_true():
    assert hangman.is_word_guessed(
        'ad', 'dba') is True


def test_2_letter_secret_word_returns_true_using_string():
    assert hangman.is_word_guessed('ad', 'dba') is True


def test_2_letter_secret_word_returns_false():
    assert hangman.is_word_guessed('ad', 'kd') is False
