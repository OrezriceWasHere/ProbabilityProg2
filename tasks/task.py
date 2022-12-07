from typing import List


class Task:

    def produce_output(self) -> List[str]:
        raise NotImplementedError("Base class method!")
