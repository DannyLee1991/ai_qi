import pandas as pd
import tushare as ts

from get_data.db import engine, TABLE_STOCK, TABLE_STOCK_AREA, TABLE_STOCK_CONCEPT, TABLE_STOCK_INDUSTRY

'''
相关接口 get_stock_basics、get_industry_classified、get_area_classified、get_concept_classified

__tablename__ = 'Stock'
# 代码
code = Column(Integer, index=True)
# 股票名
name = Column(String)
# 细分行业
industry = Column(String)
# 地区
area = Column(String)
# 概念名称
c_name = Column(String)
# 上市日期
timeToMarket = Column(String)
'''

def fetch_stock_basic():
    '''
    获取股票 基础数据
    :return:
    '''
    df = ts.get_stock_basics()
    name = df['name']
    timeToMarket = df['timeToMarket']
    df = pd.DataFrame({'name': name, 'timeToMarket': timeToMarket})
    return df


def fetch_stock_industry():
    '''
    获取股票 行业数据
    :return:
    '''
    df = ts.get_industry_classified()
    return df


def fetch_stock_area():
    '''
    获取股票 地区数据
    :return:
    '''
    df = ts.get_area_classified()
    return df


def fetch_stock_concept():
    '''
    获取股票 概念数据
    :return:
    '''
    df = ts.get_concept_classified()
    return df


# sql_for_basic_stock()
# sql_for_industry_stock()
# sql_for_area_stock()
# sql_for_concept_stock()