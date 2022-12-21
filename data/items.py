from typing import List
from enum import Enum
from dataclasses import dataclass


@dataclass
class SourceItem(str, Enum):
    TRAIN = "TRAIN"
    TEST = "TEST"


@dataclass
class InputItem:
    source: SourceItem
    id: int
    words: List[str]
