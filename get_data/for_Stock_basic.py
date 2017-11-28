from get_data import ts
from get_data import engine
from utils.strutils import getEveryDay
from utils.cache import write_cache, read_cache


#
#     公司每日基本信息
#     相关接口 get_stock_basics
#
#     __tablename__ = 'Stock_basic'
#     id = Column(Integer, primary_key=True, autoincrement=True)
#     # 代码
#     code = Column(Integer, index=True)
#     # 股票名
#     name = Column(String)
#     # 日期 eg: 2017-11-24
#     date = Column(String)
#     # 市盈率 eg: 1033.02
#     pe = Column(Float)
#     # 流通股本 eg: 22.46
#     outstanding = Column(Float)
#     # 总股本(万) eg: 30.11
#     totals = Column(Float)
#     # 总资产(万) eg: 738695.50
#     totalAssets = Column(Float)
#     # 流动资产 eg: 375573.72
#     liquidAssets = Column(Float)
#     # 固定资产 eg: 108218.02
#     fixedAssets = Column(Float)
#     # 公积金 eg: 61736.45
#     reserved = Column(Float)
#     # 每股净资 eg: 2.11
#     bvps = Column(Float)
#     # 市净率 eg: 2.18
#     pb = Column(Float)
#     # 未分利润 eg: 259275.80
#     undp = Column(Float)
#     # 每股未分配 eg: 0.86
#     perundp = Column(Float)
#     # 收入同比( %) eg: -11.93
#     rev = Column(Float)
#     # 利润同比( %) eg: -5.31
#     profit = Column(Float)
#     # 毛利率( %) eg: 71.65
#     gpr = Column(Float)
#     # 净利润率(%) eg: 18.88
#     npr = Column(Float)
#     # 股东人数 eg: 71907.0
#     holders = Column(Float)


def sql_for_stock_basics_date(date_str):
    '''
    将目标日期的 get_stock_basics 数据入库
    :param date_str:
    :return:
    '''

    # 检查缓存
    # 如果缓存文件 sql_for_stock_basics_date 被删除，那么stock_basics这张表也需要清空重新爬取，否则会产生重复数据
    method = "sql_for_stock_basics_date"
    cache = read_cache(method)
    if cache:
        if date_str in cache:
            return
    else:
        cache = []

    # ------------------------------------

    try:
        df = ts.get_stock_basics(date_str)
    except:
        print(date_str)
        return None
    df['date'] = date_str

    if df is not None:
        df.to_sql('stock_basics', engine, if_exists='append')


    # 写入缓存
    cache.append(date_str)
    write_cache(method, cache)


def sql_for_stock_basics(begin_date, end_date):
    '''
    将begin_date到end_date 的日期的数据全部入库 （注意数据不去重）
    数据可是是YYYY-MM-DD
    :param begin_date:
    :param end_date:
    :return:
    '''
    dates = getEveryDay(begin_date, end_date)[::-1]
    for date in dates:
        sql_for_stock_basics_date(date)


# sql_for_stock_basics('2010-11-20', '2017-11-27')
