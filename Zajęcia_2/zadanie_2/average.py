from typing import List


def average(numbers: List[float]) -> float:
    return sum(numbers) / len(numbers)


print(average([1.0, 2.22, 3.3, 4.4, 5.4]))
