def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    for i in range(len(nums)):
        diff = target - nums[i]
        for j in range(len(nums)):
            if i == j:
                continue
            if nums[j] == diff:
                return [i, j]

    return None


print(twoSum([2, 7, 11, 15], 9))
print(twoSum([3, 2, 4], 6))
 
