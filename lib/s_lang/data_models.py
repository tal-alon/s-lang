from dataclasses import dataclass

from s_lang.variables_store import VariablesStore

Instruction = list[str]
Labels = dict[str, int]


@dataclass
class Code:
    instructions: list[Instruction]
    labels: Labels


@dataclass
class State:
    variables: VariablesStore
    pc: int
