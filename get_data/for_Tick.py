import tushare as ts
from get_data import engine, TABLE_TICK
import pandas as pd
from utils.strutils import date2str

'''
分笔数据
相关接口： get_tick_data

__tablename__ = 'tick'
id = Column(Integer, primary_key=True, autoincrement=True)
# 代码
code = Column(Integer, index=True)
# 交易日期 eg: 2017-11-24
date = Column(String, index=True)
# 成交时间 eg: 15:00:00
time = Column(String, index=True)
# 成交价格
price = Column(Float)
# 价格变动
change = Column(Float)
# 成交手
volume = Column(Integer)
# 成交金额(元)
amount = Column(BIGINT)
# 买卖类型
type = Column(String)
'''


def is_exist(code, date):
    '''
    指定日期的股票记录是否存在
    :param code:
    :param date:
    :return:
    '''
    try:
        sql = "select date from %s where code = '%s' and date = '%s'" % (TABLE_TICK, code, date)
        df = pd.read_sql(sql, engine)
        return len(df) > 0
    except:
        return False

def sql_for_Tick(code, date=date2str()):
    if is_exist(code, date):
        print("数据已存在 [code %s  date %s]" % (code, date))
    else:
        df = ts.get_tick_data(code, date=date)
        df['code'] = code
        df['date'] = date
        if len(df) <= 3 and len(df['time'][0]) > 8:
            print("异常数据 不需要插入")
        else:
            df.to_sql(TABLE_TICK, engine, if_exists='append')
            print("新数据插入成功 [code %s  date %s]" % (code, date))

# sql_for_Tick('000001')