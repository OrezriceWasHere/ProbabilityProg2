# Jonathan Shaki, Or Shachar 204920367, 209493709

from abc import abstractmethod
from typing import List


class Task:

    @abstractmethod
    def produce_output(self) -> List[str]:
        raise NotImplementedError("Base class method!")
