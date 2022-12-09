from typing import Set

from data import data_utils
from data.arguments_dictionary import ArgumentsDictionary
from data.items import *


class InputDatasets:
    instance = None
    initialized = False

    def __new__(cls):
        if cls.instance is None:
            cls.instance = super().__new__(cls)
        return cls.instance

    def __init__(self):
        if not InputDatasets.initialized:
            self.parser = InputParser()

            dev_file = ArgumentsDictionary().get("dev_filename")
            self.dev_dataset = self.parser.build_input_cache(dev_file)

            test_file = ArgumentsDictionary().get("test_filename")
            self.test_dataset = self.parser.build_input_cache(test_file)
        InputDatasets.initialized = True

    def get_development_set(self) -> List[InputItem]:
        return self.dev_dataset

    def get_test_set(self) -> List[InputItem]:
        return self.test_dataset


class InputParser:

    def build_input_cache(self, filename: str) -> List[InputItem]:
        result = []
        buffer = []
        with open(filename) as file:
            for line in file:
                if line == "\n":
                    continue
                if len(buffer) < 2:
                    buffer.append(line)
                if len(buffer) == 2:
                    item = self.parse_item(buffer)
                    buffer.clear()
                    result.append(item)
        return result

    def parse_item(self, buffer):
        header = buffer[0].replace("<", "").replace(">", "").replace("\n", "").split("\t")
        content = buffer[1].split(" ")
        source, idd, topics = header[0], header[1], header[2:]
        return InputItem(
            SourceItem(source),
            int(idd),
            [TopicItem(item) for item in topics],
            content
        )
