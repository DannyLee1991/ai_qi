from get_data import TABLE_STOCK, TABLE_STOCK_INDUSTRY, TABLE_STOCK_AREA, TABLE_STOCK_CONCEPT, TABLE_TRANSACTION, \
    TABLE_TRANSACTION_5MIN, TABLE_STOCK_BASICS, TABLE_FUQUAN
from get_data.for_Stock import sql_for_basic_stock, sql_for_industry_stock, sql_for_area_stock, sql_for_concept_stock
from get_data.for_Stock_basic import sql_for_stock_basics
from get_data.for_Transaction import sql_for_transaction_d, sql_for_transaction_5min
from get_data.for_Fuquan import sql_for_fuquan

table_func_dict = {
    TABLE_STOCK: sql_for_basic_stock,
    TABLE_STOCK_INDUSTRY: sql_for_industry_stock,
    TABLE_STOCK_AREA: sql_for_area_stock,
    TABLE_STOCK_CONCEPT: sql_for_concept_stock,
    TABLE_STOCK_BASICS: sql_for_stock_basics,
    TABLE_TRANSACTION: sql_for_transaction_d,
    TABLE_TRANSACTION_5MIN: sql_for_transaction_5min,
    TABLE_FUQUAN: sql_for_fuquan
}


def get_data(table_name, **kwargs):
    func = table_func_dict[table_name]
    func(**kwargs)

# get_data(TABLE_STOCK_BASICS, begin_date='1999-01-01', end_date='2010-10-10')



# # 获取前复权数据
# get_data(TABLE_FUQUAN,autype='qfq')

# # 获取后复权数据
# get_data(TABLE_FUQUAN,autype='hfq')

# 获取不复权数据
# get_data(TABLE_FUQUAN,autype=None)
