import copy
import random
import queue
import time

def bubble(t: list[int]) -> list[int]:
    result = queue.deque() 
    lt = len(t)

    i = 0
    while lt > 1:
        if t[i] > t[i+1]:
            temp = t[i]
            t[i] = t[i+1]
            t[i+1] = temp
        i += 1
        if i == lt-1:
            result.appendleft(t[lt-1])
            lt -= 1
            i = 0

    return result

def main() -> None:
    for i in range(1, 5):
        amount = 4**i
        print(f"--- {amount} ---")
        begin = time.time()
        target = list(range(amount))
        random.shuffle(target)
        bubble(target)
        end = time.time()
        print(f"elapsed time: {end-begin}")
        print("--------------------------")


if __name__ == "__main__":
    main()

