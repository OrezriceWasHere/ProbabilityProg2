from typing import List, Tuple
import math

def calculate_perplexity(probabilities: List[float]) -> float:
    if 0 in probabilities:
        return 0

    sum_logs = sum(math.log(p) for p in probabilities)
    return math.pow(math.e, -sum_logs / len(probabilities))


def calculate_perplexity_repetitive_items(probabilities: List[Tuple[int, float]]) -> float:
    for count, probability in probabilities:
        if probability == 0:
            return math.inf

    sum_logs = sum(math.log(p) * count for count, p in probabilities)
    return math.pow(math.e, -sum_logs / sum(c for c, _ in probabilities))

