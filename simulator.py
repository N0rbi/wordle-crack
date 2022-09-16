from enum import Enum

class CharacterStatus(Enum):
    MISMATCH = -1 # not in the word
    CORRECT = 0 # OK
    MISPLACED = 1 # in the word, but wrong position


class WordleWordSimulator:

    def __init__(self, word):
        self._word = word
        assert len(self._word) == 5
        print(word)


    def guess(self, guessed_word):
        assert len(guessed_word) == 5

        correct_chars = list(self._word)
        result = {}

        for i, (correct_char, guessed_char) in enumerate(zip(self._word, guessed_word)):
            if correct_char == guessed_char:
                result[i] = CharacterStatus.CORRECT
                correct_chars.pop(correct_chars.index(correct_char))

        for i, guessed_char in enumerate(guessed_word):
            if i not in result:
                if guessed_char in correct_chars:
                    result[i] = CharacterStatus.MISPLACED
                    correct_chars.pop(correct_chars.index(guessed_char))

        return [result.get(i, CharacterStatus.MISMATCH) for i in range(5)]


if __name__ == "__main__":
    wws = WordleWordSimulator("apple")
    print(wws.guess("apple"))
    print(wws.guess("allpe"))
    print(wws.guess("aelpp"))
    print(wws.guess("whate"))


