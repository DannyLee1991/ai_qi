from sqlalchemy import create_engine

# 股票基本信息表名
TN_STOCK = "stock"
# 股票行业表名
TN_STOCK_INDUSTRY = "stock_industry"
# 股票地区表名
TN_STOCK_AREA = "stock_area"
# 股票概念表名
TN_STOCK_CONCEPT = "stock_concept"
# 股票每日基本信息表名
TN_STOCK_BASICS_DAILY = "stock_basics_daily"
# 交易数据表名 - 每日
TN_TRANSACTION_D = 'transaction_d'
# 交易数据表名 - 每五分钟
TN_TRANSACTION_5MIN = 'transaction_5min'
# 复权数据表名
TN_FUQUAN = 'fuquan'
# 分笔数据表名
TN_TICK = 'tick'

table = lambda table, name: {"table": table, "name": name}

# 相关表
T_STOCK = table(TN_STOCK, "股票基本信息表")
T_STOCK_INDUSTRY = table(TN_STOCK_INDUSTRY, "股票行业表")
T_STOCK_AREA = table(TN_STOCK_AREA, "股票地区表")
T_STOCK_CONCEPT = table(TN_STOCK_CONCEPT, "股票概念表")
T_STOCK_BASICS_DAILY = table(TN_STOCK_BASICS_DAILY, "股票每日基本信息表")
T_TRANSACTION_D = table(TN_TRANSACTION_D, "交易数据 - 每日")
T_TRANSACTION_5MIN = table(TN_TRANSACTION_5MIN, "交易数据 - 每五分钟")
T_FUQUAN = table(TN_FUQUAN, "复权数据")
T_TICK = table(TN_TICK, "分笔数据")

TABLE_LIST = [
    T_STOCK,
    T_STOCK_INDUSTRY,
    T_STOCK_AREA,
    T_STOCK_CONCEPT,
    T_STOCK_BASICS_DAILY,
    T_TRANSACTION_D,
    T_TRANSACTION_5MIN,
    T_FUQUAN,
    T_TICK
]

USER_NAME = 'root'
PASS_WORD = 'root'
DB_NAME = 'tu'

conn_mysql = 'mysql+mysqlconnector://%s:%s@localhost:3306/%s?charset=utf8' % (USER_NAME, PASS_WORD, DB_NAME)
conn_sqlite = 'sqlite:///%s.db' % DB_NAME

engine = create_engine(conn_sqlite, echo=False)
