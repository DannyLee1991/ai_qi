from sqlalchemy import VARCHAR
from utils.cache import cache
from ..db import *
from sqlalchemy.exc import OperationalError

from sqlalchemy import create_engine
import pandas as pd


# 股票基本信息表名
TN_STOCK = "stock"
# 股票行业表名
TN_STOCK_INDUSTRY = "stock_industry"
# 股票地区表名
TN_STOCK_AREA = "stock_area"
# 股票概念表名
TN_STOCK_CONCEPT = "stock_concept"
# 股票每日基本信息表名
TN_STOCK_BASICS_DAILY = "stock_basics_daily"
# 交易数据表名 - 每日
TN_TRANSACTION_D = 'transaction_d'
# 交易数据表名 - 每五分钟
TN_TRANSACTION_5MIN = 'transaction_5min'
# 复权数据表名
TN_FUQUAN = 'fuquan'
# 分笔数据表名
TN_TICK = 'tick'

table = lambda name, label: {"name": name, "label": label}

# 相关表
T_STOCK = table(TN_STOCK, "股票基本信息表")
T_STOCK_INDUSTRY = table(TN_STOCK_INDUSTRY, "股票行业表")
T_STOCK_AREA = table(TN_STOCK_AREA, "股票地区表")
T_STOCK_CONCEPT = table(TN_STOCK_CONCEPT, "股票概念表")
T_STOCK_BASICS_DAILY = table(TN_STOCK_BASICS_DAILY, "股票每日基本信息表")
T_TRANSACTION_D = table(TN_TRANSACTION_D, "交易数据 - 每日")
T_TRANSACTION_5MIN = table(TN_TRANSACTION_5MIN, "交易数据 - 每五分钟")
T_FUQUAN = table(TN_FUQUAN, "复权数据")
T_TICK = table(TN_TICK, "分笔数据")

TABLE_LIST = [
    T_STOCK,
    T_STOCK_INDUSTRY,
    T_STOCK_AREA,
    T_STOCK_CONCEPT,
    T_STOCK_BASICS_DAILY,
    T_TRANSACTION_D,
    T_TRANSACTION_5MIN,
    T_FUQUAN,
    T_TICK
]

COLUMN_LABEL_DICT = {
    'code':'代码',
    'name':'名称',
    'date':'时间',
    'industry':'细分行业',
    'area':'地区',
    'timeToMarket':'上市日期',
    'pe':'市盈率',
    'outstanding':'流通股本',
    'totals':'总股本(万)',
    'totalAssets':'总资产(万)',
    'liquidAssets':'流动资产(万)',
    'fixedAssets':'固定资产(万)',
    'reserved':'公积金(万)',
    'bvps':'每股净资',
    'pb':'市净率',
    'undp':'未分利润',
    'perundp':'每股未分配',
    'rev':'收入同比( %)',
    'profit':'利润同比( %)',
    'gpr':'毛利率( %)',
    'npr':'净利润率( %)',
    'holders':'股东人数',
    'open':'开盘价',
    'high':'最高价',
    'close':'收盘价',
    'low':'最低价',
    'volume':'成交量',
    'price_change':'价格变动',
    'p_change':'涨跌幅',
    'ma5':'5日均价',
    'ma10':'10日均价',
    'ma20':'20日均价',
    'v_ma5':'5日均量',
    'v_ma10':'10日均量',
    'v_ma20':'20日均量',
    'turnover':'换手率',
    'autype':'复权类型',
    'amount':'成交金额',
    'type':'类型',
    'year':'年度',
    'quarter':'季度',
    'eps':'每股收益',
    'eps_yoy':'每股收益同比(%)',
    'roe':'净资产收益率(%)',
    'epcf':'每股现金流量(元)',
    'net_profits':'净利润(万元)',
    'profits_yoy':'净利润同比(%)',
    'distrib':'分配方案',
    'report_date':'发布日期',
    'net_profit_ratio':'净利率( %)',
    'gross_profit_rate':'毛利率( %)',
    'business_income':'营业收入(百万元)',
    'bips':'每股主营业务收入(元)',
}

def column_label(column):
    '''
    根据列名 获取对应的标签名
    :param column:
    :return:
    '''
    return COLUMN_LABEL_DICT[column]

# ----------------------------------------------------------------------------------------

USER_NAME = 'root'
PASS_WORD = 'root'
DB_NAME = 'tu'

conn_mysql = 'mysql+mysqlconnector://%s:%s@localhost:3306/%s?charset=utf8' % (USER_NAME, PASS_WORD, DB_NAME)
conn_sqlite = 'sqlite:///%s.db' % DB_NAME

engine = create_engine(conn_sqlite, echo=False)



def execute_sql(sql):
    '''
    根据sql查询数据
    :param sql:
    :return:
    '''
    try:
        print("sql > %s" % sql)
        df = pd.read_sql(sql, engine)
    except OperationalError as e:
        print(e)
        df = None
    return df


def column_names(table_name):
    '''
    获取表的列名
    :param table_name:
    :return:
    '''
    df = execute_sql("select * from %s limit 1" % table_name)
    if df is not None:
        columns = [column for column in df]
        return columns
    return None



def write2db(df, table, if_exists):
    '''
    写入db
    :param df:
    :return:
    '''
    if df is not None:
        index_name = df.index.name
        dtype = {}
        if index_name:
            dtype[index_name] = VARCHAR(df.index.get_level_values(index_name).str.len().max())

        df.to_sql(table, engine, if_exists=if_exists, dtype=dtype)
        print("新数据插入成功 [table: %s ]" % (table))
    else:
        print("数据异常 没有数据入库")