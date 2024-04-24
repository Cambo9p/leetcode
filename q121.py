def maxProfit(prices):
    """
    :type prices: List[int]
    :rtype: int
    """
    buy = prices[0]
    max_profit = 0

    for sell in prices:
        if buy > sell:
            buy = sell
        profit = sell - buy
        if profit > max_profit:
            max_profit = profit

    return max_profit


print(maxProfit([2,1,2,0,1]))
