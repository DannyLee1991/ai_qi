import matplotlib.pyplot as plt
from flaskr.get_data.db import handler
import pandas as pd
import matplotlib.ticker as ticker

df = handler.execute_sql("select count(*) as count,c_name from stock_industry group by c_name order by count desc")
print(df)
df.cumsum(0)
plt.figure()

df.plot(x='c_name',title="标题",kind='bar')

plt.show()