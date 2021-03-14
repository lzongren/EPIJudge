from test_framework import generic_test

OPERATOR_DICT = {
    "+": lambda y, x: x + y,
    "-": lambda y, x: x - y,
    "*": lambda y, x: x * y,
    "/": lambda y, x: x // y,
}


def evaluate(expression: str) -> int:
    if not expression:
        return 0
    parts = expression.split(",")
    stack = list()

    for part in parts:
        if part in OPERATOR_DICT:
            if len(stack) < 2:
                raise ValueError(f"Invalid input, not enough operands before {part}")
            x = stack.pop()
            y = stack.pop()
            stack.append(OPERATOR_DICT[part](x, y))
        else:
            stack.append(int(part))

    return stack.pop()


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main("evaluate_rpn.py", "evaluate_rpn.tsv", evaluate)
    )
