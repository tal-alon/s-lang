# s-lang
s-lang interpreter

### Basic usage:
```python
from s_lang import run


def main() -> None:
    inputs = [5]
    code = """
    Z <- Z + 1
[A] IF X != 0 GOTO B
    IF Z != 0 GOTO E
[B] Y <- Y + 1
    X <- X - 1
    IF Z != 0 GOTO A
"""

    result: int = run(code, inputs)
    print(result) 


if __name__ == "__main__":
    main()

```

Notes:
- The interpreter is sensitive to both white space and letter case.
- Variable names must be an upper-case X, Z or Y. X or Z vars may or may not have an adjacent positive index (X1, X2, Z10)
- Labels must be an upper-case letter and may or may not have an adjacent positive index (L, A1, B5)
- A variable or label which are not indexed will be indexed by 1 as default

### Instruction with tags:
```
[L] {...}
```

### Supported commands:

| V <- V           | V: VAR           | assign V to itself                                                                               |
|------------------|------------------|--------------------------------------------------------------------------------------------------|
| V <- V + 1       | V: VAR           | increase V by 1                                                                                  |
| V <- V - 1       | V: VAR           | decrease V by 1                                                                                  |
| IF V != 0 GOTO L | V: VAR, L:LABEL  | if V is not eq to 0 jump to the instruction tagged with L, else continue to the next instruction |
| V <- V + k       | V: VAR, k: CONST | increase V by k                                                                                  |
| V <- V - k       | V: VAR, k: CONST | decrease V by k                                                                                  |
| IF V = 0 GOTO L  | V: VAR, L: LABEL | if V is eq to 0 jump to the instruction tagged with L, else continue to the next instruction     |
| GOTO L           | L: LABEL         | jump to the instruction tagged with L                                                            |


