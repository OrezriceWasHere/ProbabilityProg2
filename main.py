import sys
from os.path import exists

from data.arguments_dictionary import ArgumentsDictionary
from tasks.init_task import InitTask
from tasks.lidstone_task import LidstoneTask
from tasks.preprocessing_development_task import PreprocessingDevelopmentTask

LANGUAGE_VOCABULARY_SIZE = 300000


def print_output():
    result = generate_header() + "\n"

    tasks = [
        InitTask(),
        PreprocessingDevelopmentTask(),
        LidstoneTask()
    ]

    output_number = 1

    for task in tasks:
        for output in task.produce_output():
            result += f'#Output{output_number}\t{str(output)}\n'
            output_number += 1

    print(result)


def initialize(**input_variables):
    ArgumentsDictionary().__init__(**input_variables)


def main():
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
    print_output()


def generate_header():
    names = ["Or Shachar", "Jonathan Shaki"]
    ids = ["123456789", "???"]
    return f"#Students\t{' '.join(names)}\t{' '.join(ids)}"


if __name__ == '__main__':
    main()
