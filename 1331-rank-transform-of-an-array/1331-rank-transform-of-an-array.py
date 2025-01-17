class Solution(object):
    def arrayRankTransform(self, arr):
        arr_sorted = sorted(set(arr))
        result = []
        arr_rank = {}
        rank = 1

        for i in arr_sorted:
            arr_rank[i] = rank
            rank += 1

        for i in arr:
            result.append(arr_rank[i])

        return result