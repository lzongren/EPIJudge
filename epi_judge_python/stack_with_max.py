from test_framework import generic_test
from test_framework.test_failure import TestFailure


class Stack:
    def __init__(self) -> None:
        super().__init__()
        self._stack = list()
        self._max_stack = list()

    def empty(self) -> bool:
        return len(self._stack) == 0

    def max(self) -> int:
        if self.empty():
            raise IndexError("Stack is empty, cannot call max!")
        return self._max_stack[-1]

    def pop(self) -> int:
        if self.empty():
            raise IndexError("Stack is empty, cannot pop!")

        elem = self._stack.pop()
        self._max_stack.pop()
        return elem

    def push(self, x: int) -> None:
        self._stack.append(x)
        self._max_stack.append(max(x, self._max_stack[-1]) if self._max_stack else x)


def stack_tester(ops):
    try:
        s = Stack()

        for (op, arg) in ops:
            if op == "Stack":
                s = Stack()
            elif op == "push":
                s.push(arg)
            elif op == "pop":
                result = s.pop()
                if result != arg:
                    raise TestFailure(
                        "Pop: expected " + str(arg) + ", got " + str(result)
                    )
            elif op == "max":
                result = s.max()
                if result != arg:
                    raise TestFailure(
                        "Max: expected " + str(arg) + ", got " + str(result)
                    )
            elif op == "empty":
                result = int(s.empty())
                if result != arg:
                    raise TestFailure(
                        "Empty: expected " + str(arg) + ", got " + str(result)
                    )
            else:
                raise RuntimeError("Unsupported stack operation: " + op)
    except IndexError:
        raise TestFailure("Unexpected IndexError exception")


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "stack_with_max.py", "stack_with_max.tsv", stack_tester
        )
    )
