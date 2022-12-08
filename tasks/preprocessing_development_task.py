from typing import List
from tasks.task import Task
from data.input_datasets import InputDatasets


class PreprocessingDevelopmentTask(Task):

    def produce_output(self) -> List[str]:
        distinct_words = InputDatasets().get_distinct_words_dev()
        return [str(len(distinct_words))]
