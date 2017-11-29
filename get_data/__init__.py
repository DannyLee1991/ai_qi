from db import engine
import pandas as pd

# 股票基本信息表
TABLE_STOCK = "stock"
# 股票行业表
TABLE_STOCK_INDUSTRY = "stock_industry"
# 股票地区表
TABLE_STOCK_AREA = "stock_area"
# 股票概念表
TABLE_STOCK_CONCEPT = "stock_concept"
# 股票每日基本信息表
TABLE_STOCK_BASICS = "stock_basics"
# 交易数据 - 每日
TABLE_TRANSACTION = 'transaction'
# 交易数据 - 每五分钟
TABLE_TRANSACTION_5MIN = 'transaction_5min'

def distinct_codes():
    '''
    获取不重复的股票代码
    :return:
    '''
    r = pd.read_sql("select code from stock", engine)
    codes = r['code']
    return codes