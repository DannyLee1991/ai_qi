import tushare as ts
#
#
# # 股票列表
# # 获取沪深上市公司基本情况。
# sb = ts.get_stock_basics()
#
#
# # 业绩报告（主表）
# # 按年度、季度获取业绩报表数据。
# rd = ts.get_report_data(2014,3)
# print(rd)
#
#
# # 盈利能力
# # 按年度、季度获取盈利能力数据
# pd = ts.get_profit_data(2014,3)
# print(pd)
#
#
# # 营运能力
# # 按年度、季度获取营运能力数据
# od = ts.get_operation_data(2014,3)
# print(od)
#
#
# # 成长能力
# # 按年度、季度获取成长能力数据
# gd = ts.get_growth_data(2014,3)
# print(gd)
#
#
# 偿债能力
# 按年度、季度获取偿债能力数据
dd = ts.get_debtpaying_data(2014,3)
print(dd)
#
# # 现金流量
# # 按年度、季度获取现金流量数据
# cd = ts.get_cashflow_data(2014,3)
# print(cd)
