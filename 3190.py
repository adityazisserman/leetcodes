class Solution:
    def minimumOperations(self, nums: list[int]) -> int:
        calcs = 0
        done = 0
        for i in nums:
            if i%3 == 0:
                done += 1
            else:
                calcs += 1
                    
        if done == len(nums):
            return(0)
        else:
            return(calcs)
        
result = Solution()
print(result.minimumOperations(nums = [1,2,3,4]))