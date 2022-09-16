from .evaluator import EvaluatorBase
from simulator import CharacterStatus
from termcolor import colored

class StdinEvaluator(EvaluatorBase):

    def __init__(self, wordle_file, random_seed=1, allowed_guesses=6):
        super().__init__(wordle_file, random_seed, allowed_guesses)
        self.__previous_guess = None

    def __colored_guess(self, args):
        char, state = args
        if state == CharacterStatus.CORRECT:
            return colored(char, "green")
        elif state == CharacterStatus.MISPLACED:
            return colored(char, "yellow")
        elif state == CharacterStatus.MISMATCH:
            return colored(char, "grey")
        else:
            raise Exception()
    
    def _guess(self, round, previous_state):
        if previous_state:
            print("Prevoius round results: %s" % "".join(map(self.__colored_guess, zip(self.__previous_guess, previous_state))))
        else:
            print("Waiting for guess")
        self.__previous_guess = input("Please enter next input:").strip()
        return self.__previous_guess


if __name__ == "__main__":
    print("Accuracy: %f" % StdinEvaluator("words.txt").evaluate())