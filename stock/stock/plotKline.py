import pandas as pd
import numpy as np
import matplotlib.dates as mdates


def plot_K_line(stockCode, sliceSize):
    # 1.数据预处理
    # 读取数据
    data = pd.read_csv(("stocks/" + stockCode + ".csv"))

    # 将时间数据转换为pandas的时间格式
    data["date"] = pd.to_datetime(data["date"], infer_datetime_format=True, yearfirst=True)

    # 将时间数据转换为matplotlib的时间格式
    data['date'] = data['date'].apply(lambda d: mdates.date2num(d.to_pydatetime()))
    data['date'] = np.float64(range(int(data['date'][0].item()), int(data['date'][0].item()) + len(data)))
    # 将数据框转换为元组
    tuples = [tuple(x) for x in data[['date', 'open', 'close', 'high', 'low']].values][-sliceSize:]
    #
    # # 2.图像设置
    # # 获得fig和ax对象
    # fig, ax = plt.subplots()
    # # 调节横坐标距离底部的长度
    # fig.subplots_adjust(bottom=0.2)
    # ax.xaxis_date()
    # ax.autoscale_view()
    # # 3.绘图
    # # 烛台图绘制
    #
    # candlestick_ochl(ax, tuples, width=0.6, colorup='r', colordown="g", alpha=0.8)
    # # 调整图像设置横坐标标签的显示样式，获得当前坐标轴plt.gca、获得x轴刻度标签get_xticklabels、转换角度rotation、旋转角度hori...ent
    # plt.setp(plt.gca().get_xticklabels(), rotation=45, horizontalalignment='right')
    # plt.show()
    return tuples
