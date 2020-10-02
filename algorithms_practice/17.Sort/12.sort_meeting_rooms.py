#from algorithms.sort import meeting_rooms
## person can attend all meeting

## check


def can_attend_meetings(intervals):
    """
    :type intervals: List[Interval]
    :rtype: bool
    """
    intervals = sorted(intervals, key=lambda x: x[0])
    for i in range(1, len(intervals)):
        if intervals[i][0] < intervals[i - 1][1]:
            return False
    return True


alist=[[0, 30],[5, 10],[15, 20]]
blist=[[0, 30],[35, 40],[45, 50]]
print(can_attend_meetings(alist))
print(can_attend_meetings(blist))
