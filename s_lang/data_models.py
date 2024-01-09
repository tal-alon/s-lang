from dataclasses import dataclass

Instruction = list[str]
Labels = dict[str, int]
Variable = tuple[str, int]

@dataclass
class Code:
    instructions: list[Instruction]
    labels: Labels

@dataclass
class Variables:
    x: dict[int, int] = field(default_factory=lambda: defaultdict(int))
    z: dict[int, int] = field(default_factory=lambda: defaultdict(int))
    y: int = 0
