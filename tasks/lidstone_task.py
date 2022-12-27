from data import data_utils
from tasks.task import Task
from calculations import *

from data.arguments_dictionary import ArgumentsDictionary

from constants import *


class LidstoneTask(Task):

    def __init__(self):
        self.train, self.validation = data_utils.split_development_data()
        self.input_word = ArgumentsDictionary()["word"]

        self.events_in_train = sum(self.train.values())
        self.events_in_validation = sum(self.validation.values())

        self.best_lambda = None # unknown yet

    def produce_output(self) -> List[str]:

        return [str(value) for value in
                self.produce_count_output() +
                self.produce_probability_output() +
                self.produce_perplexity_output()]

    def produce_count_output(self) -> list:
        return [
            self.events_in_validation,  # Output8
            self.events_in_train,  # Output9
            len(self.train.keys()),  # Output10
            self.train.get(self.input_word) or 0  # Output11
        ]

    def produce_probability_output(self) -> list:
        return [
            self.get_probability_of_word(self.input_word, 0.0),  # Output12
            self.get_probability_of_word(UNSEEN_WORD, 0.0),  # Output13
            self.get_probability_of_word(self.input_word, 0.1),  # Output14
            self.get_probability_of_word(UNSEEN_WORD, 0.1),  # Output15
        ]

    def calculate_perplexity(self, bag_of_words, lambda_):
        probabilities = [(count, self.get_probability_of_word(word, lambda_)) for word, count in bag_of_words.items()]
        return calculate_perplexity_repetitive_items(probabilities)

    def produce_perplexity_output(self) -> list:
        lambdas_to_output = [0.01, 0.1, 1.0]

        output_16_to_17 = [self.calculate_perplexity(self.validation, lambda_)
                                     for lambda_ in lambdas_to_output]

        lambdas_to_check = [i / 100 for i in range(201)] # each number between 0 and 2, with 2-digits-after-decimal point precision

        perplexities_calculations = [self.calculate_perplexity(self.validation, lambda_)
                           for lambda_ in lambdas_to_check]

        min_perplexity = min(perplexities_calculations)

        min_lambda = -1

        for lambda_, perplexity in zip(lambdas_to_check, perplexities_calculations): # searching for the lambda of the min perplexity
            if perplexity == min_perplexity:
                min_lambda = lambda_

        self.best_lambda = min_lambda

        return output_16_to_17 + [min_lambda, min_perplexity]

    def get_probability(self, r, lambda_):
        """Calculate the probability of word with r occurrences, given lambda"""

        # calculate lidstone smoothing
        return (r + lambda_) / (lambda_ * ArgumentsDictionary()["language_vocabulary_size"] + self.events_in_train)

    def get_probability_of_word(self, word, lambda_):
        return self.get_probability(self.train.get(word) or 0, lambda_)

    def get_expected_frequency(self, r):
        """Get the expected frequency of word with r occurrences (uses the best lambda found)"""

        return self.get_probability(r, self.best_lambda) * self.events_in_train # expected frequency in the training set
