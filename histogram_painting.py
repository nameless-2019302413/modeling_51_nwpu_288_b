import numpy as np  # 最重要的库
from pandas import read_csv
# 画图用的
import seaborn as sns
import matplotlib.pyplot as plt
from scipy import stats
# 14个数据的名称，别问为啥是英文，问就是中文不支持,而且中文烦，所以图是matlab画的
column_names = ['人均犯罪率', '大块占地住宅区比例', '非零售商业占地比例', '查尔斯河虚拟变量', '氮氧化物浓度', '每户平均房间数', '1940年前建造的户主所有房比例',
                '与五个波士顿劳动力聚集区的加权距离',
                '与辐射式公路接近指数', '每1万美元的全值财产税', '学生/教师比例', '非洲裔美国人比例的一个计算值', '低社会地位人口的比例', '房价']
# 读取数据
data = read_csv('bostonh.csv', header=None, delimiter=r"\s+", names=column_names)

# 处理坏点
data = data[~(data['房价'] >= 50.0)]  # 最后用16个数据被剔除了
# print(np.shape(data))
fig, axs = plt.subplots(ncols=7, nrows=2, figsize=(20, 10))
index = 0
axs = axs.flatten()
sns.set(palette="muted", color_codes=True)    # seaborn样式
plt.rcParams['font.sans-serif'] = ['SimHei']  # 黑体
plt.rcParams['axes.unicode_minus'] = False    # 解决无法显示符号的问题
sns.set(font='SimHei', font_scale=0.8)        # 解决Seaborn中文显示问题
plt.figure(figsize=(20, 10))
sns.heatmap(data.corr().abs(),  annot=True)
plt.show()
plt.tight_layout(pad=0.4, w_pad=0.5, h_pad=5.0)
