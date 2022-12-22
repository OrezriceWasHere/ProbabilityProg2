from typing import List

from tasks.task import Task
from data.arguments_dictionary import ArgumentsDictionary
from data import data_utils
from calculations import calculate_perplexity_repetitive_items
from constants import *


class HeldoutTask(Task):

    def __init__(self):
        self.train, self.heldout = data_utils.split_development_data(0.5)
        self.input_word = ArgumentsDictionary()["word"]

    def produce_output(self) -> List[str]:
        return [str(value) for value in
                self.produce_count_output() +
                self.produce_probability_output()]

    def produce_count_output(self) -> list:
        return [
            sum(self.train.values()),  # Output21
            sum(self.heldout.values()),  # Output22
        ]

    def produce_probability_output(self) -> list:
        return [
            self.probability_of_word(self.input_word),  # Output23
            self.probability_of_word(UNSEEN_WORD)  # Output24
        ]

    def calculate_perplexity(self, bag_of_words):
        probabilities = [(count, self.probability_of_word(word)) for word, count in
                         bag_of_words.items()]
        return calculate_perplexity_repetitive_items(probabilities)

    def probability_of_word(self, word):
        return self.get_expected_probability(self.train.get(word) or 0)

    def get_occurrences_in_heldout(self, r):
        return sum(self.heldout.get(key) for key in self.heldout if (self.train.get(key) or 0) == r)

    def get_number_of_words_with(self, r):
        if r == 0:
            return ArgumentsDictionary()["language_vocabulary_size"] - len(self.heldout)

        return len([key for key in self.train if self.train[key] == r])

    def get_expected_probability(self, r):
        return self.get_occurrences_in_heldout(r) / (self.get_number_of_words_with(r) * sum(self.heldout.values()))

    def get_expected_frequency(self, r):
        return self.get_expected_probability(r) * (sum(self.train.values()) + sum(self.heldout.values()))