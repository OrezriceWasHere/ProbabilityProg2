from typing import List, Dict, Tuple
from data.arguments_dictionary import ArgumentsDictionary
import math


def calculate_lidstone_smoothing(word: str, word_count_dict: Dict[str, int], lamda=0.0) -> float:
    count_word = word_count_dict.get(word) or 0 # c(x)
    count_all_possible_words = ArgumentsDictionary()["language_vocabulary_size"]# s
    count_distinct_words = len(word_count_dict) # X

    # TODO: shouldn't the divisor be lambda * count_all_possible_words + number_of_events?
    return (count_word + lamda) / (lamda * count_distinct_words + count_all_possible_words)


def calculate_perplexity(probabilities: List[float]) -> float:
    sum_logs = sum(math.log(p) for p in probabilities)
    return math.pow(math.e, -sum_logs / len(probabilities))


def calculate_perplexity_repetitive_items(probabilities: List[Tuple[int, float]]) -> float:
    sum_logs = sum(math.log(p) * count for count, p in probabilities)
    return math.pow(math.e, -sum_logs / sum(c for c, _ in probabilities))
