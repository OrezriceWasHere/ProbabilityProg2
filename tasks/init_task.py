from typing import List

from tasks.task import Task
from data import input_data_factory


def calc_uniform_dist_of_a_word():
    vocabulary_size = input_data_factory.get_instance()["language_vocabulary_size"]
    return 1 / vocabulary_size


class InitTask(Task):

    def produce_output(self) -> List[str]:
        input_dict = input_data_factory.get_instance()

        return [
            input_dict["dev_filename"],
            input_dict["test_filename"],
            input_dict["word"],
            input_dict["out_filename"],
            input_dict["language_vocabulary_size"],
            calc_uniform_dist_of_a_word()
        ]
