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

        self.events_in_train = sum(self.train.values())
        self.events_in_heldout = sum(self.heldout.values())

    def produce_output(self) -> List[str]:
        return [str(value) for value in
                self.produce_count_output() +
                self.produce_probability_output()]

    def produce_count_output(self) -> list:
        return [
            self.events_in_train,  # Output21
            self.events_in_heldout,  # Output22
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
        """Calculate the number of occurrences in heldout of words with r occurrences in training set"""

        return sum(self.heldout.get(key) for key in self.heldout if (self.train.get(key) or 0) == r)

    def get_number_of_words_with(self, r):
        if r == 0:
            return ArgumentsDictionary()["language_vocabulary_size"] - len(self.train) # the words we didn't see

        return len([key for key in self.train if self.train[key] == r])

    def get_expected_probability(self, r):
        """return the expected probability of word with r occurrences"""
        return self.get_occurrences_in_heldout(r) / (self.get_number_of_words_with(r) * self.events_in_heldout) # heldout smoothing

    def get_expected_frequency(self, r):
        """the expected frequency of a word with r occurrences on dataset with the same size as the training set"""
        return self.get_expected_probability(r) * self.events_in_train # expected frequency in the training set