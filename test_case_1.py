import re
import hangman as hangman


def test_perfect_score(capsys):
    input_values = ['e', 'p', 'l', 'i', 's', 'm']
    hangman.choose_word = lambda _: "simple"
    hangman.input = lambda _: input_values.pop(0)

    hangman.main()
    out, err = capsys.readouterr()
    assert re.search(r'.*\s*score.*\s*36', out, re.IGNORECASE), out
    assert err == ''


def test_perfect_score_with_duplicate_letters(capsys):
    input_values = ['b', 'o', 'b', 'o']
    hangman.choose_word = lambda _: "bobo"
    hangman.input = lambda _: input_values.pop(0)

    hangman.main()
    out, err = capsys.readouterr()
    assert re.search(r'.*\s*score.*\s*12', out, re.IGNORECASE), out
    assert err == ''


def test_used_all_guesses(capsys):
    input_values = ['h', 'i', 'j', 'b', 'k', 'l', 'm']
    hangman.choose_word = lambda _: "baby"
    hangman.input = lambda _: input_values.pop(0)

    hangman.main()
    out, err = capsys.readouterr()
    assert re.search(r'Sorry, you ran out of guesses.', out, re.IGNORECASE), out
    assert err == ''


def test_guessed_word_with_duplicate_letters(capsys):
    input_values = ['b', 'a', 'b', 'y']
    hangman.choose_word = lambda _: "baby"
    hangman.input = lambda _: input_values.pop(0)

    hangman.main()
    out, err = capsys.readouterr()
    assert re.search(r'.*\s*score.*\s*18', out, re.IGNORECASE), out
    assert err == ''


def test_uppercase_letters(capsys):
    input_values = ['B', 'A', 'B', 'Y']
    hangman.choose_word = lambda _: "baby"
    hangman.input = lambda _: input_values.pop(0)

    hangman.main()
    out, err = capsys.readouterr()
    assert re.search(r'.*\s*score.*\s*18', out, re.IGNORECASE), out
    assert err == ''


def test_vowel_guessed_when_word_is_all_vowels(capsys):
    input_values = ['a']
    hangman.choose_word = lambda _: "aa"
    hangman.input = lambda _: input_values.pop(0)

    hangman.main()
    out, err = capsys.readouterr()
    assert re.search(r'.*\s*score.*\s*6', out, re.IGNORECASE), out
    assert err == ''


def test_incorrect_vowel_guess_when_word_is_1_vowel_(capsys):
    input_values = ['a', 'e', 'c', 'r']
    hangman.choose_word = lambda _: "car"
    hangman.input = lambda _: input_values.pop(0)

    hangman.main()
    out, err = capsys.readouterr()
    assert re.search(r'.*\s*score.*\s*12', out, re.IGNORECASE), out
    assert err == ''
