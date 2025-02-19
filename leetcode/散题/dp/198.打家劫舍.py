class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        f = [0] * (n + 1)
        f[1] = nums[0]
        for i in range(2,n + 1):
            for j in range(i - 1):
                f[i] = max(f[i],f[j] + nums[i - 1])
        return max(f)        