"""
You are given K eggs, and you have access to a building with N floors
from 1 to N. Each egg is identical in function, and if an egg breaks,
you cannot drop it again. You know that there exists a floor F with
0 <= F <= N such that any egg dropped at a floor higher than F will
break, and any egg dropped at or below floor F will not break.
Each move, you may take an egg (if you have an unbroken one) and drop
it from any floor X (with 1 <= X <= N). Your goal is to know with
certainty what the value of F is. What is the minimum number of moves
that you need to know with certainty what F is, regardless of the
initial value of F?
Example:
Input: K = 1, N = 2
Output: 2
Explanation:
Drop the egg from floor 1.  If it breaks, we know with certainty that F = 0.
Otherwise, drop the egg from floor 2.  If it breaks, we know with
certainty that F = 1.
If it didn't break, then we know with certainty F = 2.
Hence, we needed 2 moves in the worst case to know what F is with certainty.

K 개의 계란이 제공되며 N 개의 층이있는 건물을 이용할 수 있습니다.
각 난은 기능면에서 동일하며 난이 깨지면
다시 떨어 뜨릴 수 없습니다. 당신은 바닥 F가 있다는 것을 알고 있습니다.
0 <= F <= N 계란이 F보다 높은 바닥에 떨어질 경우
바닥 F 또는 그 아래에 떨어진 달걀은 깨지지 않습니다.
움직일 때마다, 알을 낳고 (깨지지 않은 경우) 떨어 뜨릴 수 있습니다
모든 층 X에서 (1 <= X <= N). 당신의 목표는
F의 가치가 무엇인지 확신하십시오. 최소 이동 횟수는 얼마입니까
F가 무엇인지 확실하게 알아야합니다.
F의 초기 값?
"""
# Function to get minimum number of trials
# needed in worst case with n eggs and k floors
import sys
def eggDrop(n, k):

    # If there are no floors, then no trials
    # needed. OR if there is one floor, one
    # trial needed.
    if (k == 1 or k == 0):
        return k

        # We need k trials for one egg
    # and k floors
    if (n == 1):
        return k

    min = sys.maxsize

    # Consider all droppings from 1st
    # floor to kth floor and return
    # the minimum of these values plus 1.
    for x in range(1, k + 1):

        res = max(eggDrop(n - 1, x - 1),
                  eggDrop(n, k - x))
        if (res < min):
            min = res

    return min + 1

from algorithms.dp import egg_drop

k=10
n=20  ## 4
print(egg_drop(n,k))