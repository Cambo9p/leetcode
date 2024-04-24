def productExceptSelf(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    # sum of everything to the left
    left = []
    for i in range(len(nums)):
        val = 1
        s = [x for x in nums[:i]]

        for j in s:
            val *= j
        left.append(val)

    right = []
    for i in range(len(nums)):
        val = 1
        s = [x for x in nums[i + 1:]]

        for j in s:
            val *= j
        right.append(val)

    ans = []
    for i in range(len(nums)):
        ans.append(left[i] * right[i])

    return ans


print(productExceptSelf([1, 2, 3, 4]))
