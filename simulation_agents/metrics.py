from dataclasses import dataclass


@dataclass
class Metrics:
    tick: int
    counter: int


metric = Metrics(0, 0)
