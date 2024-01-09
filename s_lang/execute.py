from s_lang.data_models import Code, Labels, Instruction
from s_lang.variables_store import VariablesStore
from s_lang.parse import is_label_valid


def inc_var(variables: VariablesStore, var: str) -> None:
    variables[var] += 1


def dec_var(variables: VariablesStore, var: str) -> None:
    variables[var] = max(variables[var] - 1, 0)


def if_nez_goto(variables: VariablesStore, labels: Labels, var: str, label: str, pc: int) -> int:
    val = variables[var]
    labels_target = labels.get(label, -1)

    return labels_target if 0 < val else pc + 1


def exec_instruction(pc: int, inst: Instruction, labels: Labels, variables: VariablesStore) -> int:
    match inst:
        case [v1, "<-", v2] if v1 == v2:
            return pc + 1

        case [v1, "<-", v2, "+", "1"] if v1 == v2:
            inc_var(variables, v1)
            return pc + 1

        case [v1, "<-", v2, "-", "1"] if v1 == v2:
            dec_var(variables, v1)
            return pc + 1

        case ["IF", v, "!=", "0", "GOTO", l]:
            if not is_label_valid(l):
                raise Exception(f"Syntax error at line {pc}: {' '.join(inst)}\ninvalid label")

            return if_nez_goto(variables, labels, v, l, pc)

        case _:
            raise Exception(f"Syntax error at line {pc}: {' '.join(inst)}")


def exec_code(code: Code, input_vars: list[int]) -> int:
    variables = VariablesStore(input_vars)
    pc = 0
    prog_len = len(code.instructions)

    while 0 <= pc < prog_len:
        pc = exec_instruction(pc, code.instructions[pc], code.labels, variables)

    return variables.y
