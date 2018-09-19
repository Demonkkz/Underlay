import numpy as np
import pandas as pd
import tushare as ts
from datetime import datetime
import matplotlib.pylab as plt
import mpl_finance as mpf
from matplotlib.dates import date2num


df = pd.read_csv('stocks/000001.csv', encoding='utf-8', index_col='date')
df.index = pd.to_datetime(df.index)  # 将字符串索引转换成时间索引
array = df['close'].values
window = array[-30:] # 将最近30天作为滑动窗口

def rolling(window, array):
    norms = []
    for index in range(0, len(array) - 60):
        norm = np.linalg.norm(array[index:index + 30] - window)
        norms.append(norm)
    return norms.index(min(norms))

index_of_min = rolling(window, array)
start_date = str(df.index[index_of_min])
end_date = str(df.index[index_of_min + 60])
data_list = []
t = int(date2num(datetime.now())) + 30
hist_data = ts.get_hist_data('000001', start=start_date, end=end_date)

for dates, row in hist_data.iterrows():
    date_time = datetime.strptime(dates,'%Y-%m-%d')
    t -= 1
    open,high,close,low = row[:4] # unpacking
    datas = (t,open,high,low,close)
    data_list.append(datas)
# 创建子图
fig, ax = plt.subplots()
fig.subplots_adjust(bottom=0.2)
# 设置X轴刻度为日期时间
ax.xaxis_date()
plt.xticks(rotation=45)
plt.yticks()
plt.title("predict result")
plt.xlabel("time")
plt.ylabel("close price")
mpf.candlestick_ohlc(ax, data_list, width=0.6, colorup='r', colordown='g')
plt.grid()
plt.show()
