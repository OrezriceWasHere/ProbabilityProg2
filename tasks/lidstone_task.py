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
            sum(self.validation.values()),
            sum(self.train.values()),
            len(self.train.keys()),
            self.train.get(self.input_word) or 0
        ]

    def produce_probability_output(self) -> list:
        return [
            calculate_lidstone_smoothing(self.input_word, self.train, lamda=0.0),
            calculate_lidstone_smoothing(UNSEEN_WORD, self.train, lamda=0.0),
            calculate_lidstone_smoothing(self.input_word, self.train, lamda=0.1),
            calculate_lidstone_smoothing(UNSEEN_WORD, self.train, lamda=0.1),
        ]

    def produce_perplexity_output(self) -> list:
        lamdas_to_check = [0.01, 0.1, 1.0]
        lamdas_proababilities_calculations = [unigram_probability_calculation(self.train,
                                                                              lamda=lamda)
                                              for lamda in lamdas_to_check]
        perplexities_calculations = [calculate_perplexity(probabilities)
                                     for probabilities in lamdas_proababilities_calculations]

        min_perplexity = min(perplexities_calculations)
        min_lamda = -1

        for lamda, perplexity in zip(lamdas_to_check, perplexities_calculations):
            if perplexity == min_perplexity:
                min_lamda = lamda

        return perplexities_calculations + [min_lamda, min_perplexity]
