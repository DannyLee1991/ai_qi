import tushare as ts

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

def fetch_tick(code,date):
    '''
    获取指定股票指定日期的分笔数据记录
    :param code:
    :param date:
    :return:
    '''
    df = ts.get_tick_data(code, date=date)
    df['code'] = code
    df['date'] = date
    if len(df) <= 3 and len(df['time'][0]) > 8:
        print("异常数据 不需要插入")
    else:
        return df

# sql_for_Tick('000001')