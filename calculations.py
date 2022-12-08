from typing import List, Dict
from data.arguments_dictionary import ArgumentsDictionary
import math


def calculate_lidstone_smoothing(word: str, word_count_dict: Dict[str, int], lamda=0.0) -> float:
    count_word = word_count_dict.get(word) or 0
    count_all_possible_words = ArgumentsDictionary()["language_vocabulary_size"]
    count_distinct_words = len(word_count_dict)
    return (count_word + lamda) / (count_all_possible_words + lamda * count_distinct_words)


def unigram_probability_calculation(word_count_dict: Dict[str, int], lamda=0.0) -> List[float]:
    return [
        calculate_lidstone_smoothing(word, word_count_dict, lamda)
        for word in word_count_dict.keys()
    ]


def calculate_perplexity(probabilities: List[float]) -> float:
    sum_logs = sum(math.log(p) for p in probabilities)
    return math.pow(math.e, -sum_logs / len(probabilities))
