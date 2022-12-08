from typing import List
from enum import Enum
from dataclasses import dataclass


@dataclass
class TopicItem(str, Enum):
    ACK = "acq"
    MONEY_FX = "money-fx"
    GRAIN = "grain"
    CRUDE = "crude"
    TRADE = "trade"
    INTEREST = "interest"
    SHIP = "ship"
    WHEAT = "wheat"
    CORN = "corn"


@dataclass
class SourceItem(str, Enum):
    TRAIN = "TRAIN"
    TEST = "TEST"


@dataclass
class InputItem:
    source: SourceItem
    id: int
    topics: List[TopicItem]
    words: List[str]
