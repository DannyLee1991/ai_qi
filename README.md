## 股票数据分析

运行环境 Python3

使用前先执行:

```
pip3 install -r requirements.txt
```

-----

### 1.初始化数据库

进入web目录，执行:

```
python3 manage.py db init
```

创建db文件:

```
python3 manage.py db migrate
```

### 2.开启服务

```
python3 manage.py runserver
```

打开浏览器 [http://127.0.0.1:5000/](http://127.0.0.1:5000/)


-----

todo:

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
