from typing import List
def merge_intervals(intervals: List[List[int]]) -> List[List[int]]:
    if not intervals:
        return []

    intervals.sort(key=lambda x: x[0])
    merged = []
    current = intervals[0]   

    for i in range(1, len(intervals)):
        start, end = intervals[i]

        if start <= current[1]:
            current[1] = max(current[1], end)
        else:
            merged.append(current)
            current = intervals[i]

    merged.append(current)

    return merged

if __name__ == "__main__":
    tests = [
        ([[1,3],[2,6],[8,10],[15,18]], [[1,6],[8,10],[15,18]]),
        ([[1,4],[4,5]], [[1,5]]),
        ([[4,7],[1,4]], [[1,7]])
    ]

    for arr, expected in tests:
        result = merge_intervals(arr)
        print(f"Input: {arr}")
        print(f"Output: {result}   (expected: {expected})\n")
