def mergeIntervals(intervals):
    # need to check input
    if (len(intervals) <= 1):
        return intervals
    else:
        intervals.sort()
        i=0
        # had index errors trying to use range with a for loop
        # also while trying to use for a in b:
        while i < len(intervals) - 1:
            j = i + 1
            print ('0',intervals[i][1], '1', intervals[j][0])
            if (intervals[i][1] >= intervals[j][0]):
                intervals[j] = [intervals[i][0], intervals[j][1]]
                intervals.pop(i)
            i += 1
        return intervals