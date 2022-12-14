# Jonathan Shaki, Or Shachar 204920367, 209493709

import sys
from os.path import exists

from data.arguments_dictionary import ArgumentsDictionary
from tasks.init_task import InitTask
from tasks.lidstone_task import LidstoneTask
from tasks.heldout_task import HeldoutTask
from tasks.evaluation_task import EvaluationTask
from tasks.preprocessing_development_task import PreprocessingDevelopmentTask

LANGUAGE_VOCABULARY_SIZE = 300000


def get_output():
    """returns the output of the whole program"""

    result = generate_header() + "\n"

    lidstone_task = LidstoneTask()
    heldout_task = HeldoutTask()
    evaluation_task = EvaluationTask(lidstone_task, heldout_task)

    tasks = [
        InitTask(),
        PreprocessingDevelopmentTask(),
        lidstone_task,
        heldout_task,
        evaluation_task
    ]

    output_number = 1

    for task in tasks:
        for output in task.produce_output():
            result += f'#Output{output_number}\t{str(output)}\n'
            output_number += 1

    return result


def initialize(**input_variables):
    ArgumentsDictionary().__init__(**input_variables)


def main():
    """process the command line and write the output to the appropriate file"""

    argv = sys.argv
    if len(argv) < 5:
        raise Exception("Not enough arguments to unpack. Expecting: "
                        " < development set filename > "
                        " < test set filename > "
                        " < INPUT WORD > "
                        " < output filename >")

    _, dev_filename, test_filename, word, out_filename = argv

    if any([
        not exists(dev_filename),
        not exists(test_filename)
    ]):
        raise Exception("Some or all of the input files do not exist")

    initialize(dev_filename=dev_filename,
               test_filename=test_filename,
               word=word,
               out_filename=out_filename,
               language_vocabulary_size=LANGUAGE_VOCABULARY_SIZE)

    with open(out_filename, 'w') as file:
        file.write(get_output())


def generate_header():
    names = ["Or Shachar", "Jonathan Shaki"]
    ids = ["209493709", "204920367"]
    return f"#Students\t{' '.join(names)}\t{' '.join(ids)}"


if __name__ == '__main__':
    main()
