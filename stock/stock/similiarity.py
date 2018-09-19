import csv
import numpy as np

stockcode = str(input("input the num you chosed: \n"))
if stockcode > '0' and stockcode < '900957':
  print('thanks!')
else:
  print('bad Num')
print('your Num is %s\n' % stockcode)


#读取对应序号的股票开盘数据，存于数列
with open('stocks/' + stockcode + '.csv', 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    aim_line = [row['open'] for row in reader]
    # aim_line = [row[1] for row in reader]


#根据得到的价格序列，生成变化率时间序列
aim_p = []
for i in range(0, len(aim_line)-1):
  w1 = aim_line[i]
  w2 = aim_line[i+1]
  aim_p.insert(i,(w2-w1)/w1)


#计算开盘价时间序列的均值与标准差，以备两支股票的相似度计算
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
    return variance ** 0.5

variance = prices_variance(aim_p)
aim_std=prices_std_deviation(variance)


#与其他股票协方差对比，越大表示相似度越高，存于指定数组
stocks = 1
sim = 0
sim_line = []
while stocks != stockcode:
    with open('stocks/'+stocks+'.csv', 'r') as sam_csvfile:
        read = csv.reader(csvfile)
        sample_line = [row[1] for row in reader]

    sample_p=[]
    for i in range(0,len(aim_p)-1,1):
      w1=sample_p[i]
      w2=sample_p[i+1]
      sample_p.insert(i,(w2-w1)/w1)

    variance = prices_variance(sample_p)
    sample_std=prices_std_deviation(variance)

    #计算协方差
    stock_cov = np.cov(aim_p,sample_p)
    #计算相似度
    rou = stock_cov/(aim_std*sample_std)
    stocks = stocks+1
    if rou > sim:
        sim = rou
        sim_line = sample_line
        print('The stock number with the highest similarity is %d\n' % stocks)

print('Analysis of the similarity ends')