import copy

def trace(A, begin, end) -> None:
    for i in range(0, end-begin):
        print("  ", end="")
        print(A[begin+i], end = " ")
        print()
    print("----------")

def merge_sort(A) -> list[int]:
    B = copy.copy(A)
    split_elements(A, 0, len(A), B)
    return A


def merge(B, begin, middle, end, A) -> None:
    b = begin
    m = middle

    for i in range(begin, end):
        if b >= middle:
            B[i] = A[m]
            m += 1
            continue
        if m >= end:
            B[i] = A[b]
            b += 1
            continue

        if A[b] <= A[m]:
            B[i] = A[b]
            b += 1

        else: # A[b] > A[m]
            B[i] = A[m]
            m += 1
    trace(B, begin, end)


def split_elements(B: list[int], begin: int, end: int, A: list[int]) -> None:
    if end - begin <= 1:
        return

    middle = (begin + end) // 2
    split_elements(A, begin, middle, B)
    split_elements(A, middle, end, B)

    merge(B, begin, middle, end, A)


import random

if __name__ == "__main__":
    random.seed(1)
    target = list(range(5))
    random.shuffle(target)
    B = copy.copy(target)
    print(target)
    result = merge_sort(target)
    print(result)

