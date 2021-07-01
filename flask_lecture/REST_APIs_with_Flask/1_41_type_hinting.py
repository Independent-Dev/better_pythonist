from typing import List


def list_avg(sequence: List) -> float:
    return sum(sequence) / len(sequence)


list_avg(123)  # pycharm에서는 여기에 list type을 넣지 않으면 경고문구가 뜸.
