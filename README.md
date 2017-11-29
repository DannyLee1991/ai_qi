## 股票数据分析

运行环境 Python3

使用前先执行:

```
pip3 install -r requirements.txt
```

-----

### 获取数据

> **注意：** 目前数据会存储在sqlite数据库中

执行`./get_data/manager.py`中的`get_data`方法，即可获取指定表的数据。

例如:

```
get_data(TABLE_STOCK)
```

即可获得股票基本信息表的数据

----

支持参数传递 例如：

```
get_data(TABLE_STOCK_BASICS, begin_date='1999-01-01', end_date='2017-10-10')
```

具体传递参数的含义，需要到对应的方法中查看

-----

todo:

sqlite转mysql
爬取数据脚本
数据可视化
数据预测

done:

股票基本信息相关数据获取：

- stock
- stock_industry
- stock_area
- stock_concept

股票每日基本信息获取：

- stock_basics

交集记录数据获取：

- transaction
- transaction_5min
