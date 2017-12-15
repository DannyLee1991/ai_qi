import tudata as tu
# 解决matplotlib字体不显示的问题
from pylab import *
import pandas as pd

mpl.rcParams['font.sans-serif'] = ['SimHei']  # 指定默认字体
mpl.rcParams['axes.unicode_minus'] = False  # 解决保存图像是负号'-'显示为方块的问题


sql1 = "select open as '000002_open' ,date from transaction_d where code = '000002'  and  date >= '2016-12-13'  and  date <= '2017-12-13'  order by date "
df1 = tu.read_sql(sql1)

sql2 = "select open as '000001_open' ,date from transaction_d where code = '000001'  and  date >= '2016-12-13'  and  date <= '2017-12-13'  order by date "
df2 = tu.read_sql(sql2)
# df =pd.DataFrame(np.random.randn(100, 4), columns=list('ABCD'))

df = pd.merge(df1, df2, on='date')
df.cumsum()
plt.figure()

df.plot(x='date',title="标题")
plt.show()