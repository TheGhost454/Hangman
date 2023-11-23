import hangman as hangman


def test_consonant_returns_0_guesses_remaining():
    assert hangman.incorrect_guess('c', 1) == 0


def test_consonant_word_returns_1_guesses_remaining():
    assert hangman.incorrect_guess('c', 2) == 1


def test_vowel_returns_2_guesses_remaining():
    assert hangman.incorrect_guess('e', 4) == 2


def test_vowel_returns_0_guesses_remaining():
    assert hangman.incorrect_guess('e', 2) == 0


def test_vowel_returns_0_guesses_remaining_when_1_guess_remaining():
    assert hangman.incorrect_guess('e', 1) == 0


def test_vowel_returns_0_guesses_remaining_when_negative_guess_remaining():
    assert hangman.incorrect_guess('e', -1) == 0
