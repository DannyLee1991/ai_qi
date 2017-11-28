import tushare as ts

# 存款利率
# 结构不规整
dr = ts.get_deposit_rate()
print(dr)


# 贷款利率
# 结构不规整
lr = ts.get_loan_rate()
print(lr)

# 存款准备金率
rrr = ts.get_rrr()
print(rrr)


# 货币供应量
ms = ts.get_money_supply()
print(ms)


# 货币供应量(年底余额)
ms = ts.get_money_supply_bal()
print(ms)


# 国内生产总值(年度)
gy = ts.get_gdp_year()
print(gy)


# 国内生产总值(季度)
gq = ts.get_gdp_quarter()
print(gq)


# 三大需求对GDP贡献
gf = ts.get_gdp_for()
print(gf)


# 三大产业对GDP拉动
gp = ts.get_gdp_pull()
print(gp)


# 三大产业贡献率
gc = ts.get_gdp_contrib()
print(gc)


# 居民消费价格指数
cpi = ts.get_cpi()
print(cpi)


# 工业品出厂价格指数
ppi = ts.get_ppi()
print(ppi)