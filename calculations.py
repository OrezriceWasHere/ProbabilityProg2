from typing import List, Dict, Tuple
from data.arguments_dictionary import ArgumentsDictionary
import math

def calculate_perplexity(probabilities: List[float]) -> float:
    sum_logs = sum(math.log(p) for p in probabilities)
    return math.pow(math.e, -sum_logs / len(probabilities))


def calculate_perplexity_repetitive_items(probabilities: List[Tuple[int, float]]) -> float:
    sum_logs = sum(math.log(p) * count for count, p in probabilities)
    return math.pow(math.e, -sum_logs / sum(c for c, _ in probabilities))

