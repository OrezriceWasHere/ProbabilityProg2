from typing import List, Set, Tuple, Dict

from data.input_datasets import InputDatasets
from data.items import InputItem


def count_word_appearances(items: List[InputItem]) -> Dict[str, int]:
    word_count_dict = {}
    for item in items:
        for word in item.words:
            if word not in word_count_dict:
                word_count_dict[word] = 0
            word_count_dict[word] = word_count_dict[word] + 1
    return word_count_dict


def distinct_words_of_list(items: List[InputItem]) -> Set[str]:
    return set(count_word_appearances(items).keys())


def split_development_data(split_ratio=0.9) -> Tuple[List[InputItem], List[InputItem]]:
    dev_set = InputDatasets().get_development_set()
    count_train_items = round(split_ratio * len(dev_set))
    return (
        dev_set[:count_train_items],
        dev_set[count_train_items:]
    )
