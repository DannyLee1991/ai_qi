from sqlalchemy import create_engine

global _engine

support_db_types = ["sqlite", "mysql"]

db_config = {
    'engine_type': 'sqlite',
    'db_name': 'tu',
    'user_name': 'root',
    'pass_word': 'root'
}


def get_conn():
    '''
    获取数据库连接对象
    :return:
    '''
    if db_config['engine_type'] == 'mysql':
        conn = 'mysql+mysqlconnector://%s:%s@localhost:3306/%s?charset=utf8' % (
            db_config['user_name'], db_config['pass_word'], db_config['db_name'])
    else:
        conn = 'sqlite:///%s.db' % db_config['db_name']
    return conn


def set_db_config(engine_type, db_name, user_name, pass_word):
    db_config['engine_type'] = engine_type
    db_config['db_name'] = db_name
    db_config['user_name'] = user_name
    db_config['pass_word'] = pass_word

    global _engine
    _engine = create_engine(get_conn(), echo=False)


def get_engine():
    '''
    获取数据库引擎
    :return:
    '''
    global _engine
    return _engine
