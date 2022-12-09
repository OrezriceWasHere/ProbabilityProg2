from typing import List, Set, Tuple, Dict

from data.input_datasets import InputDatasets
from data.items import InputItem


def count_word_appearances(words: List[str]) -> Dict[str, int]:
    word_count_dict = {}
    for word in words:
        if word not in word_count_dict:
            word_count_dict[word] = 0
        word_count_dict[word] = word_count_dict[word] + 1
    return word_count_dict

def get_words_by_input_items(items: List[InputItem]) -> List[str]:
    all_words = []
    for item in items:
        all_words += item.words
    return all_words

def count_word_appearances_by_items(items: List[InputItem]) -> Dict[str, int]:
    all_words = get_words_by_input_items(items)
    return count_word_appearances(all_words)


def distinct_words_of_list(items: List[InputItem]) -> Set[str]:
    return set(count_word_appearances(items).keys())


def split_development_data(split_ratio=0.9) -> Tuple[Dict[str, int], Dict[str, int]]:
    dev_set = InputDatasets().get_development_set()
    all_words = get_words_by_input_items(dev_set)
    words_in_train = round(split_ratio*len(all_words))
    train, dev = all_words[:words_in_train], all_words[words_in_train:]
    return (
        count_word_appearances(train),
        count_word_appearances(dev)
    )
