from s_lang.data_models import Code, State, Instruction
from s_lang.variables_store import VariablesStore
from s_lang.instructions import exec_instruction


class Runner:
    def __init__(self, code: Code, inputs: list[int], logger=None):  # TODO add typing to logger
        self.code: Code = code
        self.state: State = State(
            variables=VariablesStore(inputs),
            pc=0
        )
        self.logger = logger

    @property
    def current_instruction(self) -> Instruction:
        return self.code.instructions[self.state.pc]

    def log_state(self) -> None:
        if self.logger:
            self.logger(f"{self.state.pc}: {self.state.variables.y}, {self.state.variables.x}, {self.state.variables.z}")

    def run(self) -> int:
        prog_len = len(self.code.instructions)

        while 0 <= self.state.pc < prog_len:
            exec_instruction(
                inst=self.current_instruction,
                labels=self.code.labels,
                state=self.state
            )
            self.log_state()

        return self.state.variables.y
