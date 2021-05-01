import matplotlib.pyplot as plt
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.model_selection import train_test_split

# 数据读取

column_names = ['CRIM', 'ZN', 'INDUS', 'CHAS', 'NOX', 'RM', 'AGE', 'DIS', 'RAD', 'TAX', 'PTRATIO', 'B', 'LSTAT', 'MEDV']
df = pd.read_csv('bostonh.csv', header=None, delimiter=r"\s+", names=column_names)
# 所有属性拟合线性模型
X = df.iloc[:, :-1].values
y = df[['MEDV']].values
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=0)
# 线性模型训练
slr = LinearRegression()
slr.fit(X_train, y_train)
y_train_pred = slr.predict(X_train)
y_test_pred = slr.predict(X_test)


# 残差评估方法
plt.scatter(y_train_pred, y_train_pred - y_train,
            c='blue', marker='o', label='Training data')
plt.scatter(y_test_pred, y_test_pred - y_test,
            c='lightgreen', marker='s', label='Test data')
plt.xlabel('Predicted values')
plt.ylabel('Residuals')
plt.legend(loc='upper left')
plt.hlines(y=0, xmin=-10, xmax=50, lw=2, colors='red')
plt.xlim([-10, 50])
plt.savefig('residuals_metric.png')
plt.show()

# 均方误差评价指标
from sklearn.metrics import mean_squared_error

print('MSE train: %.3f, test: %.3f' % (
    mean_squared_error(y_train, y_train_pred),
    mean_squared_error(y_test, y_test_pred))
      )
print('PolynomialFeatures MSE train: %.3f, test: %.3f' % (
    mean_squared_error(y_train, y_train_pred_quad),
    mean_squared_error(y_test, y_test_pred_quad))
      )

# 决定系数评价指标
from sklearn.metrics import r2_score

print('R^2 train: %.3f, test: %.3f' %
      (r2_score(y_train, y_train_pred),
       r2_score(y_test, y_test_pred)))
print('PolynomialFeatures R^2 train: %.3f, test: %.3f' %
      (r2_score(y_train, y_train_pred_quad),
       r2_score(y_test, y_test_pred_quad)))
