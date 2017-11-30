from get_data import TABLE_STOCK, TABLE_STOCK_INDUSTRY, TABLE_STOCK_AREA, TABLE_STOCK_CONCEPT, TABLE_TRANSACTION_D, \
    TABLE_TRANSACTION_5MIN, TABLE_STOCK_BASICS, TABLE_FUQUAN, TABLE_TICK
from get_data.for_Stock import sql_for_basic_stock, sql_for_industry_stock, sql_for_area_stock, sql_for_concept_stock
from get_data.for_Stock_basic import sql_for_stock_basics
from get_data.for_Transaction import sql_for_transaction_d, sql_for_transaction_5min
from get_data.for_Fuquan import sql_for_fuquan
from get_data.for_Tick import sql_for_Tick

table_func_dict = {
    TABLE_STOCK: sql_for_basic_stock,
    TABLE_STOCK_INDUSTRY: sql_for_industry_stock,
    TABLE_STOCK_AREA: sql_for_area_stock,
    TABLE_STOCK_CONCEPT: sql_for_concept_stock,
    TABLE_STOCK_BASICS: sql_for_stock_basics,
    TABLE_TRANSACTION_D: sql_for_transaction_d,
    TABLE_TRANSACTION_5MIN: sql_for_transaction_5min,
    TABLE_FUQUAN: sql_for_fuquan,
    TABLE_TICK: sql_for_Tick
}


def get_data(table_name, **kwargs):
    func = table_func_dict[table_name]
    func(**kwargs)


# # ---- 获取基础数据 不必要频繁更新 ----
# # 获取【股票基础信息】 - 必备
# get_data(TABLE_STOCK)
# # 获取【股票行业表】数据
# get_data(TABLE_STOCK_INDUSTRY)
# # 获取【股票地区表】数据
# get_data(TABLE_STOCK_AREA)
# # 获取【股票概念表】数据
# get_data(TABLE_STOCK_CONCEPT)
#
#
# # ---- 获取股票每日基本信息 ----
# # 股票每日基本信息 包含指定时间区间的股票基础信息数据，大部分字段不会发生变化，不建议大量获取
# get_data(TABLE_STOCK_BASICS, begin_date='2016-01-01', end_date='2017-10-10')
#
#
# # ---- 获取股票交易数据（重要数据） 需要频繁更新----
# # 股票每日交易数据
# get_data(TABLE_TRANSACTION_D)
# # 股票每5分钟交易数据
# get_data(TABLE_TRANSACTION_5MIN)
#
#
# # ---- 获取复权数据 （重要数据）需要频繁更新 ----
# # 获取【前复权】数据
# get_data(TABLE_FUQUAN, autype='qfq')
# # 获取【后复权】数据
# get_data(TABLE_FUQUAN, autype='hfq')
# # 获取【不复权】数据
# get_data(TABLE_FUQUAN, autype=None)
#
#
# # ---- 获取分笔数据 （重要数据）需要频繁更新 ----
# # 获取指定股票的分笔数据
# get_data(TABLE_TICK,code='000001', date='2017-11-29')
