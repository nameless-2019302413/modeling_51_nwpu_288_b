import numpy as np # 最重要的库
from pandas import read_csv
# 14个数据的名称

column_names = ['人均犯罪率', '大块占地住宅区比例', '非零售商业占地比例', '查尔斯河虚拟变量', '氮氧化物浓度', '每户平均房间数', '1940年前建造的户主所有房比例',
                '与五个波士顿劳动力聚集区的加权距离',
                '与辐射式公路接近指数', '每1万美元的全值财产税', '学生/教师比例', '非洲裔美国人比例的一个计算值', '低社会地位人口的比例', '房价']

# column_names = ['CRIM', 'ZN', 'INDUS', 'CHAS', 'NOX', 'RM', 'AGE', 'DIS', 'RAD', 'TAX', 'PTRATIO', 'B', 'LSTAT', 'MEDV']
# 读取数据
data = read_csv('bostonh.csv', header=None, delimiter=r"\s+", names=column_names)
data.describe().to_csv("toulaang.csv")
print(type(data.describe()))


