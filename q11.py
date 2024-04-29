def maxArea(height):
    """
    :type height: List[int]
    :rtype: int
    """
    l = 0
    r = len(height) - 1
    curr_max = 0

    while r > l:
        rheight = height[r]
        lheight = height[l]
        if rheight > lheight:
            # left is smaller
            vol = lheight * (r - l)
            print(f"vol is {vol}")

            l += 1
        else:
            vol = rheight * (r - l)
            print(f"vol is {vol}")
            r -= 1

        if vol > curr_max:
            curr_max = vol
    return curr_max


print(maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))
