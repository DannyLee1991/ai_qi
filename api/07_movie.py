import tushare as ts

# 实时票房
# 获取实时电影票房数据，30分钟更新一次票房数据，可随时调用。
df = ts.realtime_boxoffice()
print(df)


# 每日票房
# 获取单日电影票房数据，默认为上一日的电影票房，可输入参数获取指定日期的票房。
# 似乎只能显示前一日的
df = ts.day_boxoffice("2015-01-01")
print(df)


# 月度票房
# 获取单月电影票房数据，默认为上一月，可输入月份参数获取指定月度的数据。
df = ts.month_boxoffice('2016-12')
print(df)


# 影院日度票房
# 获取全国影院单日票房排行数据，默认为上一日，可输入日期参数获取指定日期的数据。
df = ts.day_cinema('2015-12-24')
print(df)