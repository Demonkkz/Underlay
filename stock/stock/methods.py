# 定义求和函数
def prices_sum(prices):
    total = 0
    for price in prices:
        total += price
    return total

# 定义求平均值函数
def prices_average(prices):
    sum_of_prices = prices_sum(prices)
    average = sum_of_prices / float(len(prices))
    return average

# 定义求方差函数
def prices_variance(pir):
    average = prices_average(pir)
    variance = 0
    for a in pir:
        variance += (average - a) ** 2
    return variance / len(pir)

# 定义求标准差函数
def prices_std_deviation(variance):
    variance = prices_variance(prices)
    return variance ** 0.5