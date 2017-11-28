import tushare as ts


# 即时新闻
# 获取即时财经新闻，类型包括国内财经、证券、外汇、期货、港股和美股等新闻信息。
news = ts.get_latest_news()
print(news)

# 信息地雷
# 获取个股信息地雷数据
n = ts.get_notices('600000')
print(n)


# 新浪股吧
# 获取sina财经股吧首页的重点消息。股吧数据目前获取大概17条重点数据，可根据参数设置是否显示消息内容，默认情况是不显示。
gb = ts.guba_sina()
print(gb)
