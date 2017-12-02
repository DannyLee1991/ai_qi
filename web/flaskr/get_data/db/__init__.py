from sqlalchemy import create_engine

# 股票基本信息表
TABLE_STOCK = "stock"
# 股票行业表
TABLE_STOCK_INDUSTRY = "stock_industry"
# 股票地区表
TABLE_STOCK_AREA = "stock_area"
# 股票概念表
TABLE_STOCK_CONCEPT = "stock_concept"
# 股票每日基本信息表
TABLE_STOCK_BASICS_DAILY = "stock_basics_daily"
# 交易数据 - 每日
TABLE_TRANSACTION_D = 'transaction_d'
# 交易数据 - 每五分钟
TABLE_TRANSACTION_5MIN = 'transaction_5min'
# 复权数据
TABLE_FUQUAN = 'fuquan'
# 分笔数据
TABLE_TICK = 'tick'

USER_NAME = 'root'
PASS_WORD = 'root'
DB_NAME = 'tu'

conn_mysql = 'mysql+mysqlconnector://%s:%s@localhost:3306/%s?charset=utf8' % (USER_NAME, PASS_WORD, DB_NAME)
conn_sqlite = 'sqlite:///%s.db' % DB_NAME

engine = create_engine(conn_sqlite, echo=False)
