def productExceptSelf(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """

    ans = [0 for i in nums]
    lsum = 1
    for i in range(len(nums)):
        ans[i] = lsum
        lsum *= nums[i]

    rsum = 1
    for i in range(len(nums) - 1, -1, -1):
        ans[i] *= rsum
        rsum *= nums[i]

    return ans


print(productExceptSelf([1, 2, 3, 4]))
