from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float, BIGINT
from sqlalchemy import create_engine

engine = create_engine('sqlite:///foo.db', echo=True)
Base = declarative_base()


def init_db():
    Base.metadata.create_all(engine)


def drop_db():
    Base.metadata.drop_all(engine)


# ----------------------------------------------------------------------------

class Stock(Base):
    '''
    股票
    相关接口 get_stock_basics、get_industry_classified、get_concept_classified、get_area_classified
    '''
    __tablename__ = 'Stock'
    id = Column(Integer, primary_key=True, autoincrement=True)
    # 代码
    code = Column(Integer, index=True)
    # 股票名
    name = Column(String)
    # 细分行业
    industry = Column(String)
    # 地区
    area = Column(String)
    # 概念名称
    c_name = Column(String)
    # 上市日期
    timeToMarket = Column(String)


class Stock_basic(Base):
    '''
    公司每日基本信息
    相关接口 get_stock_basics
    '''
    __tablename__ = 'Stock_basic'
    id = Column(Integer, primary_key=True, autoincrement=True)
    # 代码
    code = Column(Integer, index=True)
    # 股票名
    name = Column(String)
    # 日期 eg: 2017-11-24
    date = Column(String)
    # 市盈率 eg: 1033.02
    pe = Column(Float)
    # 流通股本 eg: 22.46
    outstanding = Column(Float)
    # 总股本(万) eg: 30.11
    totals = Column(Float)
    # 总资产(万) eg: 738695.50
    totalAssets = Column(Float)
    # 流动资产 eg: 375573.72
    liquidAssets = Column(Float)
    # 固定资产 eg: 108218.02
    fixedAssets = Column(Float)
    # 公积金 eg: 61736.45
    reserved = Column(Float)
    # 每股净资 eg: 2.11
    bvps = Column(Float)
    # 市净率 eg: 2.18
    pb = Column(Float)
    # 未分利润 eg: 259275.80
    undp = Column(Float)
    # 每股未分配 eg: 0.86
    perundp = Column(Float)
    # 收入同比( %) eg: -11.93
    rev = Column(Float)
    # 利润同比( %) eg: -5.31
    profit = Column(Float)
    # 毛利率( %) eg: 71.65
    gpr = Column(Float)
    # 净利润率(%) eg: 18.88
    npr = Column(Float)
    # 股东人数 eg: 71907.0
    holders = Column(Float)


# ------------------------------------------------------------------------------------------
#           交易相关接口
# ------------------------------------------------------------------------------------------

class Transaction(Base):
    '''
    个股历史交易记录
    相关接口： get_hist_data
    '''
    __tablename__ = 'transaction'
    id = Column(Integer, primary_key=True, autoincrement=True)
    # 代码
    code = Column(Integer, index=True)
    # 日期 eg: 2017-11-24
    date = Column(String, index=True)
    # 开盘价 eg: 24.10
    open = Column(Float)
    # 最高价 eg: 24.70
    high = Column(Float)
    # 收盘价 eg: 24.45
    close = Column(Float)
    # 最低价 eg: 24.09
    low = Column(Float)
    # 成交量 eg: 53160.52
    volume = Column(Float)
    # 价格变动 eg: 0.43
    price_change = Column(Float)
    # 涨跌幅 eg: 1.79
    p_change = Column(Float)
    # 5日均价 eg: 24.822
    ma5 = Column(Float)
    # 10日均价 eg: 26.441
    ma10 = Column(Float)
    # 20日均价 eg: 28.300
    ma20 = Column(Float)
    # 5日均量 eg: 80676.85
    v_ma5 = Column(Float)
    # 10日均量 eg: 117984.89
    v_ma10 = Column(Float)
    # 20日均量 eg: 175389.32
    v_ma20 = Column(Float)
    # 换手率 eg: 1.33
    turnover = Column(Float)


class Transaction_5min(Base):
    '''
    个股历史交易记录 5min
    相关接口： get_hist_data(dtype="5")
    '''
    __tablename__ = 'transaction_5min'
    id = Column(Integer, primary_key=True, autoincrement=True)
    # 代码
    code = Column(Integer, index=True)
    # 日期 eg: 2017-11-24
    date = Column(String, index=True)
    # 开盘价 eg: 24.10
    open = Column(Float)
    # 最高价 eg: 24.70
    high = Column(Float)
    # 收盘价 eg: 24.45
    close = Column(Float)
    # 最低价 eg: 24.09
    low = Column(Float)
    # 成交量 eg: 53160.52
    volume = Column(Float)
    # 价格变动 eg: 0.43
    price_change = Column(Float)
    # 涨跌幅 eg: 1.79
    p_change = Column(Float)
    # 5日均价 eg: 24.822
    ma5 = Column(Float)
    # 10日均价 eg: 26.441
    ma10 = Column(Float)
    # 20日均价 eg: 28.300
    ma20 = Column(Float)
    # 5日均量 eg: 80676.85
    v_ma5 = Column(Float)
    # 10日均量 eg: 117984.89
    v_ma10 = Column(Float)
    # 20日均量 eg: 175389.32
    v_ma20 = Column(Float)
    # 换手率 eg: 1.33
    turnover = Column(Float)


class Fuquan(Base):
    '''
    复权数据
    相关接口： get_h_data
    '''
    __tablename__ = 'fuquan'
    id = Column(Integer, primary_key=True, autoincrement=True)
    # 代码
    code = Column(Integer, index=True)
    # 复权类型 eg: qfq
    autype = Column(String)
    # 交易日期 eg: 2017-11-24
    date = Column(String, index=True)
    # 开盘价 eg: 13.11
    open = Column(Float)
    # 最高价 eg: 13.18
    high = Column(Float)
    # 收盘价 eg: 13.09
    close = Column(Float)
    # 最低价 eg: 12.93
    low = Column(Float)
    # 成交量 eg: 59612483.0
    volume = Column(Float)
    # 成交金额 eg: 7.776997e+08
    amount = Column(BIGINT)


class Tick_data(Base):
    '''
    分笔数据
    相关接口： get_tick_data
    '''
    __tablename__ = 'tick_data'
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


# ------------------------------------------------------------------------------------------
#           投资参考数据
# ------------------------------------------------------------------------------------------

class Report(Base):
    '''
    业绩报表
    相关接口：get_report_data
    '''
    __tablename__ = 'report'
    id = Column(Integer, primary_key=True, autoincrement=True)
    # 代码
    code = Column(Integer, index=True)
    # 股票名
    name = Column(String)
    # 年度
    year = Column(Integer)
    # 季度
    quarter = Column(Integer)
    # 每股收益
    eps = Column(Float)
    # 每股收益同比(%)
    eps_yoy = Column(Float)
    # 每股净资产
    bvps = Column(Float)
    # 净资产收益率(%)
    roe = Column(Float)
    # 每股现金流量(元)
    epcf = Column(Float)
    # 净利润(万元)
    net_profits = Column(Float)
    # 净利润同比(%)
    profits_yoy = Column(Float)
    # 分配方案
    distrib = Column(String)
    # 发布日期
    report_date = Column(String)


class Profit(Base):
    '''
    盈利能力数据
    相关接口：get_profit_data
    '''
    __tablename__ = 'profit'
    id = Column(Integer, primary_key=True, autoincrement=True)
    # 代码
    code = Column(Integer, index=True)
    # 股票名
    name = Column(String)
    # 年度
    year = Column(Integer)
    # 季度
    quarter = Column(Integer)
    # 净资产收益率( %)
    roe = Column(Float)
    # 净利率( %)
    net_profit_ratio = Column(Float)
    # 毛利率( %)
    gross_profit_rate = Column(Float)
    # 净利润(万元)
    net_profits = Column(Float)
    # 每股收益
    eps = Column(Float)
    # 营业收入(百万元)
    business_income = Column(Float)
    # 每股主营业务收入(元)
    bips = Column(Float)


class Operation(Base):
    '''
    营运能力数据
    相关接口：get_operation_data
    '''
    __tablename__ = 'operation'
    id = Column(Integer, primary_key=True, autoincrement=True)
    # 代码
    code = Column(Integer, index=True)
    # 股票名
    name = Column(String)
    # 年度
    year = Column(Integer)
    # 季度
    quarter = Column(Integer)
    # 应收账款周转率(次)
    arturnover = Column(Float)
    # 应收账款周转天数(天)
    arturndays = Column(Float)
    # 存货周转率(次)
    inventory_turnover = Column(Float)
    # 存货周转天数(天)
    inventory_days = Column(Float)
    # 流动资产周转率(次)
    currentasset_turnover = Column(Float)
    # 流动资产周转天数(天)
    currentasset_days = Column(Float)


class Growth(Base):
    '''
    成长能力数据
    相关接口：get_growth_data
    '''
    __tablename__ = 'growth'
    id = Column(Integer, primary_key=True, autoincrement=True)
    # 代码
    code = Column(Integer, index=True)
    # 股票名
    name = Column(String)
    # 年度
    year = Column(Integer)
    # 季度
    quarter = Column(Integer)
    # 主营业务收入增长率(%)
    mbrg = Column(Float)
    # 净利润增长率(%)
    nprg = Column(Float)
    # 净资产增长率
    nav = Column(Float)
    # 总资产增长率
    targ = Column(Float)
    # 每股收益增长率
    epsg = Column(Float)
    # 股东权益增长率
    seg = Column(Float)

# init_db()
