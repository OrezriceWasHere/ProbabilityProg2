from typing import List

from tasks.task import Task
from data import data_utils


class EvaluationTask(Task):

    def __init__(self, lidstone_task, heldout_task):
        self.heldout_task = heldout_task
        self.lidstone_task = lidstone_task
        self.test = data_utils.get_test_data()

    def produce_output(self) -> List[str]:
        return [str(value) for value in
                self.produce_count_output() +
                self.produce_perplexity_output() +
                self.produce_table_output()]

    def produce_count_output(self):
        return [str(sum(self.test.values()))]  # output25

    def produce_perplexity_output(self) -> list:
        lidstone_perplexity = self.lidstone_task.calculate_perplexity(self.test, self.lidstone_task.best_lambda)

        heldout_perplexity = self.heldout_task.calculate_perplexity(self.test)

        best = 'L' if lidstone_perplexity < heldout_perplexity else 'H'

        return [
            lidstone_perplexity,  # Output26
            heldout_perplexity,  # Output27
            best  # Output28
        ]

    def produce_table_output(self) -> list:
        result = ''

        for i in range(10):
            result += f'{i}\t{round(self.lidstone_task.get_expected_frequency(i), 5)}\t{round(self.heldout_task.get_expected_frequency(i), 5)}\t' \
                     + f'{self.heldout_task.get_number_of_words_with(i)}\t{self.heldout_task.get_occurrences_in_heldout(i)}\n'

        return [result]
