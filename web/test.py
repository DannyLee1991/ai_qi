import matplotlib.pyplot as plt
from flaskr.get_data.db.manager import query_by_sql
import pandas as pd
import matplotlib.ticker as ticker

df = query_by_sql("select * from transaction_d ")
print(df)
df.cumsum(0)
plt.figure()

df.plot(x='date',title="标题")

plt.show()