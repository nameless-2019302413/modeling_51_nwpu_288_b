
# coding=utf-8
import pandas as pd
import os
path1 = os.getcwd() + '/bostonh.dat'  # 获取当前路径下的.dat文件
data = pd.read_table(path1, header=None, sep='\s+')  # 用pd读此文件，详细参数（索引一类的）
print(data)
data = data.to_csv('bostonh.csv', index=False, header=False)
# 本代码用于转dat为csv，那个csv我又手动改了下，莫名的最后一个数据有个空格，变成str类型了......
