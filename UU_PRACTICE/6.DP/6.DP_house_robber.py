"""
You are a professional robber planning to rob houses along a street.
Each house has a certain amount of money stashed,
the only constraint stopping you from robbing each of them
is that adjacent houses have security system connected and
it will automatically contact the police if two adjacent houses
were broken into on the same night.
Given a list of non-negative integers representing the amount of money
of each house, determine the maximum amount of money you
can rob tonight without alerting the police.
당신은 거리를 따라 집을 강탈하려는 전문 강도입니다.
각 집에는 일정 금액의 돈이 숨겨져 있습니다.
그들 각각을 강탈하는 것을 막는 유일한 제약
인접한 집에 보안 시스템이 연결되어 있고
인접한 두 집이 있으면 자동으로 경찰에 연락합니다
같은 날에 깨졌습니다.
금액을 나타내는 음이 아닌 정수 목록이 제공됩니다.
각 집의 최대 금액을 결정하십시오
경찰에게 알리지 않고 오늘 밤 강탈 할 수 있습니다
"""
from algorithms.dp import house_robber
a=[6, 7, 1, 3, 8, 2, 4]  # 6 1 8 4  / 7 8 4
b=[5, 3, 4, 11, 2]    # 5 11

a=[6, 7, 1, 3, 8, 2, 4]
b=[5, 3, 4, 11, 2]


print(house_robber(a))

print(house_robber(b))