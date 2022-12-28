# Jonathan Shaki, Or Shachar 204920367, 209493709

from typing import List

import data.data_utils
from tasks.task import Task
from data.input_datasets import InputDatasets


class PreprocessingDevelopmentTask(Task):

    def produce_output(self) -> List[str]:
        all_words = InputDatasets().get_development_set()
        count_all_words = data.data_utils.count_word_appearances_by_items(all_words)
        return [str(sum(count_all_words.values()))]
