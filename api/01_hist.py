import tushare as ts


# # 获取个股历史交易记录
# t = ts.get_hist_data('600848',start='2016-11-28 13:00:00',ktype='5') #一次性获取全部日k线数据
# print(t)

# 获取历史复权数据
# h = ts.get_h_data('600000',start='2017-01-01')
# print(h)
#
# # 一次性获取最近一个日交易日所有股票的交易数据
# td = ts.get_today_all()
# print(td)
#
#
# # 获取分笔数据
# df = ts.get_tick_data('600848',date='2014-01-09')
# print(df)
#
#
# # 获取实时分笔数据
# df = ts.get_realtime_quotes('000581') #Single stock symbol
# print(df)
#
#
# # 当日历史分笔
# df = ts.get_today_ticks('601333')
#
#
# # 大盘指数行情列表
# df = ts.get_index()
# print(df)
#
# # 大单交易数据  默认400手
# df = ts.get_sina_dd('600848', date='2015-12-24', vol=500)
# print(df)