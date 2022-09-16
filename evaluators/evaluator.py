from random import Random
from simulator import WordleWordSimulator, CharacterStatus

class EvaluatorBase:

    NUM_WORDS = 10

    def __init__(self, wordle_file, random_seed=1, allowed_guesses=6):
        self.random = Random(random_seed)
        self._words = [word.strip() for word in open(wordle_file).readlines()]
        self.allowed_guesses = allowed_guesses

    def _guess(self, round, previous_state):
        """
            To be implemented: prevoius state is None, if you enter an invalid word 
            (on the other hand, the counter will not go up) or if it is the first round.
            Otherwise it will be a list of CharacterStatus.
        """
        raise NotImplemented()

    def evaluate(self):
        correct_guesses = 0
        for _ in range(self.NUM_WORDS):
            simulator = WordleWordSimulator(self.random.choice(self._words))
            previous_state = None
            for i in range(self.allowed_guesses):
                guessed_word = None
                while guessed_word not in self._words:
                    guessed_word = self._guess(i, previous_state if guessed_word is None else None)
                
                    
                previous_state = simulator.guess(guessed_word)
                if previous_state == [CharacterStatus.CORRECT] * 5:
                    correct_guesses += 1
                    break
        
        return correct_guesses / self.NUM_WORDS
