# 예제 2-18번. 나도 이런 코드를 짤 수 있으면 좋겠다...
import bisect

def grade(score, breakpoint=[60, 70, 80, 90], grade="FDCBA"):
    i = bisect.bisect(breakpoint, score)
    return grade[i]

print([grade(score) for score in [33, 99, 77, 70, 89, 90, 100]])  # ['F', 'A', 'C', 'C', 'B', 'A', 'A']

c = (1, 2, [3, 4, 5])
print(c)
c[-1][-1] = 2
print(c)  # 이 과정에서 더 이상 에러가 나지 않음.