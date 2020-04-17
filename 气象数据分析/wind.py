# 风力数据数据分析

import numpy as np
import pandas as pd
import datetime
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from dateutil import parser
from sklearn.svm import SVR

df_ferrara = pd.read_csv('WeatherData/ferrara_270615.csv')
df_milano = pd.read_csv('WeatherData/milano_270615.csv')
df_mantova = pd.read_csv('WeatherData/mantova_270615.csv')
df_ravenna = pd.read_csv('WeatherData/ravenna_270615.csv')
df_torino = pd.read_csv('WeatherData/torino_270615.csv')
df_asti = pd.read_csv('WeatherData/asti_270615.csv')
df_bologna = pd.read_csv('WeatherData/bologna_270615.csv')
df_piacenza = pd.read_csv('WeatherData/piacenza_270615.csv')
df_cesena = pd.read_csv('WeatherData/cesena_270615.csv')
df_faenza = pd.read_csv('WeatherData/faenza_270615.csv')

# 把一个 DataFrame 中的数据点做成散点图
plt.plot(df_ravenna['wind_deg'],df_ravenna['wind_speed'],'ro')
# plt.show()
# 很显然该图的表现力也有不足

# 另一种可视化方法：极区图
# 创建一个直方图，
# 也就是将 360 度分为八个面元，每个面元为 45 度，
# 把所有的数据点分到这八个面元中
# histogram() 函数返回结果中的数组 hist 为落在每个面元的数据点数量
# 数组 bins 定义了 360 度范围内各面元的边界
hist, bins = np.histogram(df_ravenna['wind_deg'],8,[0,360])
print(hist)
print(bins)

# 创建一个函数来绘制极区图
# 三个参数：values 数组，指的是想为其作图的数据，也就是这里的 hist 数组；
# city_name 为字符串类型，指定图表标题所用的城市名称；
# max_value 为整型，指定最大的蓝色值

def showRoseWind(values,city_name,max_value):
    N = 8

    # theta = [pi*1/4, pi*2/4, pi*3/4, ..., pi*2]
    theta = np.arange(2 * np.pi / 16, 2 * np.pi, 2 * np.pi / 8)
    radii = np.array(values)
    # 绘制极区图的坐标系
    plt.axes([0.025, 0.025, 0.95, 0.95], polar=True)

    # 列表中包含的是每一个扇区的 rgb 值，x越大，对应的color越接近蓝色
    colors = [(1-x/max_value, 1-x/max_value, 0.75) for x in radii]

    # 画出每个扇区
    plt.bar(theta, radii, width=(2*np.pi/N), bottom=0.0, color=colors)

    # 设置极区图的标题
    plt.title(city_name, x=0.2, fontsize=20)

    plt.show()

# showRoseWind(hist, 'Ravenna', max(hist))
# 以得知风向在极坐标系中的分布方式。
# 该图表示这一天大部分时间风都吹向西南和正西方向

# 定义好 showRoseWind() 函数之后，查看其他城市的风向情况也非常简单
# hist, bin = np.histogram(df_ferrara['wind_deg'],8,[0,360])
# print(hist)
# showRoseWind(hist,'Ferrara', max(hist))

# 计算风速均值的分布情况
def RoseWind_Speed(df_city):
    # degs = [45, 90, ..., 360]
    degs = np.arange(45,361,45)
    tmp = []
    for deg in degs:
        # 获取 wind_deg 在指定范围的风速平均值数据
        # 获取的是风向大于 deg-46 度和风向小于 deg 的数据
        tmp.append(df_city[(df_city['wind_deg']>(deg-46)) & (df_city['wind_deg']<deg)]
        ['wind_speed'].mean())
    return np.array(tmp)

showRoseWind(RoseWind_Speed(df_ravenna),'Ravenna',max(hist))
