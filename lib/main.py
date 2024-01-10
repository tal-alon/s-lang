from s_lang import run


def read_file(path: str) -> str:
    with open(path, mode="r") as file:
        return file.read()


def main() -> None:
    path = "../programs/ex5b.s"
    inputs = [5, 6]
    code = read_file(path)

    result: int = run(code, inputs)
    print(result)


if __name__ == "__main__":
    main()
