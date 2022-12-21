from data import data_utils
from tasks.task import Task
from calculations import *

UNSEEN_WORD = "unseen-word"


class LidstoneTask(Task):

    def __init__(self):
        self.train, self.validation = data_utils.split_development_data()
        self.input_word = ArgumentsDictionary()["word"]

    def produce_output(self) -> List[str]:

        return [str(value) for value in
                self.produce_count_output() +
                self.produce_probability_output() +
                self.produce_perplexity_output()]

    def produce_count_output(self) -> list:
        return [
            sum(self.validation.values()),  # Output8
            sum(self.train.values()),  # Output9
            len(self.train.keys()),  # Output10
            self.train.get(self.input_word) or 0  # Output11
        ]

    def produce_probability_output(self) -> list:
        return [
            calculate_lidstone_smoothing(self.input_word, self.train, lamda=0.0),  # Output12
            calculate_lidstone_smoothing(UNSEEN_WORD, self.train, lamda=0.0),  # Output13
            calculate_lidstone_smoothing(self.input_word, self.train, lamda=0.1),  # Output14
            calculate_lidstone_smoothing(UNSEEN_WORD, self.train, lamda=0.1),  # Output15
        ]

    def produce_perplexity_output(self) -> list:
        lamdas_to_check = [0.01, 0.1, 1.0]
        # Word probabilities is a list where for each lamda
        # there

        # TODO: we probably want to use self.validation.items()
        word_probabilities = [[(count, calculate_lidstone_smoothing(word, self.train, lamda))
                               for word, count in self.train.items()]
                              for lamda in lamdas_to_check
                              ]

        perplexities_calculations = [calculate_perplexity_repetitive_items(word_probability)
                                     for word_probability in word_probabilities]

        # TODO: (from the exercise document) "Your program should check the range of different values for λ between 0 and 2, and choose the one that minimizes the perplexity on the validation set. λ values should be specified up to two digits after the decimal point"

        min_perplexity = min(perplexities_calculations)
        min_lamda = -1

        for lamda, perplexity in zip(lamdas_to_check, perplexities_calculations):
            if perplexity == min_perplexity:
                min_lamda = lamda

        return perplexities_calculations + [min_lamda, min_perplexity]
