from s_lang.data_models import Labels, Instruction, State
from s_lang.variables_store import VariablesStore
from s_lang.parse import is_label_valid


def inc_var(state: State, var: str) -> None:
    state.variables[var] += 1
    state.pc += 1


def dec_var(state: State, var: str) -> None:
    new_val: int = max(state.variables[var] - 1, 0)
    state.variables[var] = new_val
    state.pc += 1


def if_nez_goto(state: State, labels: Labels, var: str, label: str) -> None:
    if not is_label_valid(label):
        raise ValueError(f"invalid label")

    val = state.variables[var]
    labels_target = labels.get(label, -1)

    state.pc = labels_target if 0 < val else state.pc + 1


def add_k(state: State, var: str, k: int) -> None:
    if k < 1:
        raise ValueError("invalid const")

    state.variables[var] += k


def sub_k(state: State, var: str, k: int) -> None:
    if k < 1:
        raise ValueError("invalid const")

    state.variables[var] -= k


def if_ez_goto(state: State, labels: Labels, var: str, label: str) -> None:
    if not is_label_valid(label):
        raise ValueError(f"invalid label")

    val = state.variables[var]
    labels_target = labels.get(label, -1)

    state.pc = labels_target if 0 == val else state.pc + 1


def goto(state: State, labels: Labels, label: str) -> None:
    if not is_label_valid(label):
        raise ValueError(f"invalid label")

    labels_target = labels.get(label, -1)

    state.pc = labels_target


def exec_instruction(inst: Instruction, labels: Labels, state: State) -> None:
    try:
        match inst:
            # basic syntax:

            case [v1, "<-", v2] if v1 == v2:
                state.pc += 1

            case [v1, "<-", v2, "+", "1"] if v1 == v2:
                inc_var(state, v1)

            case [v1, "<-", v2, "-", "1"] if v1 == v2:
                dec_var(state, v1)

            case ["IF", v, "!=", "0", "GOTO", l]:
                if_nez_goto(state, labels, v, l)

            # syntactic sugars:

            case [v1, "<-", v2, "+", k] if v1 == v2 and isinstance(k, str) and k.isnumeric():
                add_k(state, v1, int(k))

            case [v1, "<-", v2, "-", k] if v1 == v2 and isinstance(k, str) and k.isnumeric():
                sub_k(state, v1, int(k))

            case ["IF", v, "=", "0", "GOTO", l]:
                if_ez_goto(state, labels, v, l)

            case ["GOTO", l]:
                return goto(state, labels, l)

            case _:
                raise ValueError("unknown command")

    except Exception as err:
        raise Exception(f"Syntax error at line {state.pc}: {' '.join(inst)}\n{err}")
