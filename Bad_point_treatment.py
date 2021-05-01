import numpy as np  # 最重要的库
from pandas import read_csv
# 画图用的
import seaborn as sns
import matplotlib.pyplot as plt
from scipy import stats
# 14个数据的名称，别问为啥是英文，问就是中文不支持，所以图是matlab画的
column_names = ['CRIM', 'ZN', 'INDUS', 'CHAS', 'NOX', 'RM', 'AGE', 'DIS', 'RAD', 'TAX', 'PTRATIO', 'B', 'LSTAT', 'MEDV']
# 读取数据
data = read_csv('bostonh.csv', header=None, delimiter=r"\s+", names=column_names)
fig, axs = plt.subplots(ncols=7, nrows=2, figsize=(20, 10))
index = 0
axs = axs.flatten()

# 评价坏点，公式见论文，没剔除之前
for k, v in data.items():
    q1 = v.quantile(0.25)
    q3 = v.quantile(0.75)
    irq = q3 - q1
    v_col = v[(v <= q1 - 1.5 * irq) | (v >= q3 + 1.5 * irq)]
    perc = np.shape(v_col)[0] * 100.0 / np.shape(data)[0]
    #print("Column %s outliers = %.2f%%" % (k, perc))
data = data[~(data['MEDV'] >= 50.0)]  # 50来源于图像观察，最后有16个数据被剔除了

# 剔除后的
for k, v in data.items():
    q1 = v.quantile(0.25)
    q3 = v.quantile(0.75)
    irq = q3 - q1
    v_col = v[(v <= q1 - 1.5 * irq) | (v >= q3 + 1.5 * irq)]
    perc = np.shape(v_col)[0] * 100.0 / np.shape(data)[0]
    print("Column %s outliers = %.2f%%" % (k, perc))
data.to_csv('bostonh_dealing.csv')  # 处理后的导出，给使用matlab的同学画个图
# print(np.shape(data))
'''
fig, axs = plt.subplots(ncols=7, nrows=2, figsize=(20, 10))
index = 0
axs = axs.flatten()
for k,v in data.items():
    sns.histplot(v, ax=axs[index])
    index += 1
plt.tight_layout(pad=0.4, w_pad=0.5, h_pad=5.0)
'''
