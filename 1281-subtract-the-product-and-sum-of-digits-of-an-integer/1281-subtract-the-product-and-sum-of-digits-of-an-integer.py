class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        str_n = str(n)
        prod, sumd = 1, 0

        for i in str_n:
            val = int(i)

            prod *= val
            sumd += val

        return prod - sumd