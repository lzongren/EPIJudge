from test_framework import generic_test

OPEN = ['(', '[', '{']
CLOSE_MAP = {
    ')': '(',
    ']': '[',
    '}': '{'
}

def is_well_formed(s: str) -> bool:
    if not s:
        return True

    stack = list()
    for ch in s:
        if ch in OPEN:
            stack.append(ch)
        elif ch in CLOSE_MAP:
            if not stack:
                return False
            matched = False
            while stack and not matched:
                pop = stack.pop()
                if pop in OPEN:
                    if CLOSE_MAP[ch] != pop:
                        return False
                    else:
                        matched = True
                elif pop in CLOSE_MAP:
                    return False
            if not matched:
                return False
        else:
            stack.append(ch)

    return len(stack) == 0


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "is_valid_parenthesization.py",
            "is_valid_parenthesization.tsv",
            is_well_formed,
        )
    )
