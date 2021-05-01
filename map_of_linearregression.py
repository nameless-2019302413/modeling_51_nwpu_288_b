import numpy as np  # 最重要的库
from pandas import read_csv
# 画图用的
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn import preprocessing
import pandas as pd
from scipy import stats
# 14个数据的名称，别问为啥是英文，问就是中文不支持,而且中文烦，所以图是matlab画的
column_names = ['CRIM', 'ZN', 'INDUS', 'CHAS', 'NOX', 'RM', 'AGE', 'DIS', 'RAD', 'TAX', 'PTRATIO', 'B', 'LSTAT', 'MEDV']

# 读取数据
data = read_csv('bostonh.csv', header=None, delimiter=r"\s+", names=column_names)

# 处理坏点
data = data[~(data['MEDV'] >= 50.0)]  # 最后用16个数据被剔除了

min_max_scaler = preprocessing.MinMaxScaler()
column_sels = ['LSTAT', 'INDUS', 'NOX', 'PTRATIO', 'RM', 'TAX', 'DIS', 'AGE']
x = data.loc[:, column_sels]
y = data['MEDV']
x = pd.DataFrame(data=min_max_scaler.fit_transform(x), columns=column_sels)
fig, axs = plt.subplots(ncols=4, nrows=2, figsize=(20, 15))
index = 0
plt.rcParams['font.sans-serif'] = ['SimHei']  # 中文字体设置-黑体
plt.rcParams['axes.unicode_minus'] = False  # 解决保存图像是负号'-'显示为方块的问题
sns.set(font='SimHei',font_scale=1.5)  # 解决Seaborn中文显示问题并调整字体大小
axs = axs.flatten()


for i, k in enumerate(column_sels):
    sns.regplot(y=y, x=x[k], ax=axs[i])
plt.show()
plt.tight_layout(pad=0.4, w_pad=0.5, h_pad=5.0)
