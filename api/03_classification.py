import tushare as ts

# 行业分类
# 本接口按照sina财经对沪深股票进行的行业分类，返回所有股票所属行业的信息
ic = ts.get_industry_classified()
print(ic)


# 概念分类
# sina财经提供的概念分类信息
cc = ts.get_concept_classified()
print(cc)


# 地域分类
# 按地域对股票进行分类，即查找出哪些股票属于哪个省份。
ac = ts.get_area_classified()
print(ac)


# 中小板分类
# 获取中小板股票数据，即查找所有002开头的股票
sc = ts.get_sme_classified()
print(sc)


# 创业板分类
# 获取创业板股票数据，即查找所有300开头的股票
gc = ts.get_gem_classified()
print(gc)


# 风险警示板分类
# 获取风险警示板股票数据，即查找所有st股票
st = ts.get_st_classified()
print(st)


# 沪深300成份及权重
# 获取沪深300当前成份股及所占权重
# FIXME 有bug
h3 = ts.get_hs300s()
print(h3)


# 上证50成份股
# 获取上证50成份股
# FIXME 有bug
ts.get_sz50s()


# 中证500成份股
# FIXME 有bug
ts.get_zz500s()


# 终止上市股票列表
t = ts.get_terminated()
print(t)


# 暂停上市股票列表
# 获取被暂停上市的股票列表，数据从上交所获取，目前只有在上海证券交易所交易被终止的股票。
s = ts.get_suspended()
print(s)