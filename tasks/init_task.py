# Jonathan Shaki, Or Shachar 204920367, 209493709

from typing import List

from tasks.task import Task
from data.arguments_dictionary import ArgumentsDictionary


def calc_uniform_dist_of_a_word():
    vocabulary_size = ArgumentsDictionary()["language_vocabulary_size"]
    return 1 / vocabulary_size


class InitTask(Task):

    def produce_output(self) -> List[str]:
        input_dict = ArgumentsDictionary()

        return [
            input_dict["dev_filename"],
            input_dict["test_filename"],
            input_dict["word"],
            input_dict["out_filename"],
            input_dict["language_vocabulary_size"],
            calc_uniform_dist_of_a_word()
        ]
