import time
import datetime

wrap_0 = lambda arg: "0" + str(arg) if (arg < 10) else arg

def todayStr():
    return date2str()

def date2str(t=time.localtime()):
    '''
    日期对象 转 日期字符串
    :param t:
    :return:
    '''
    return time.strftime("%Y-%m-%d", t)

def time2str(t=time.localtime()):
    '''
    时间对象 转 时间字符串
    :param t:
    :return:
    '''
    return time.strftime('%Y-%m-%d %H:%M:%S',t)


def str2date(datestr):
    '''
    日期字符串 转 日期对象
    :param datestr:
    :return:
    '''
    return time.strptime(datestr, "%Y-%m-%d")


def nextDayStr(datestr=date2str(), format='%Y-%m-%d'):
    '''
    获取下一天日期字符串
    :param datestr:
    :param format:
    :return:
    '''
    td = datetime.datetime.strptime(datestr, format)
    nd = td + datetime.timedelta(days=1)
    return nd.strftime(format)

def perDayStr(datestr=date2str(), format='%Y-%m-%d'):
    '''
    获取前一天日期字符串
    :param datestr:
    :param format:
    :return:
    '''
    td = datetime.datetime.strptime(datestr, format)
    nd = td - datetime.timedelta(days=1)
    return nd.strftime(format)

def perYearStr(datestr=date2str(), format='%Y-%m-%d'):
    '''
    获取前一天日期字符串
    :param datestr:
    :param format:
    :return:
    '''
    td = datetime.datetime.strptime(datestr, format)
    nd = td - datetime.timedelta(days=365)
    return nd.strftime(format)

def nextMinStr(datestr=time2str(), format='%Y-%m-%d %H:%M:%S'):
    '''
    获取下一分钟的时间字符串
    :param datestr:
    :param format:
    :return:
    '''
    td = datetime.datetime.strptime(datestr, format)
    nd = td + datetime.timedelta(seconds=60)
    return nd.strftime(format)

def getEveryDay(begin_date, end_date=date2str(), format="%Y-%m-%d"):
    '''
    获取指定两个日期之间的所有日期
    eg：
    getEveryDay('2016-01-01', '2016-01-11')

    ['2016-01-01', '2016-01-02', '2016-01-03', '2016-01-04', '2016-01-05', '2016-01-06', '2016-01-07', '2016-01-08', '2016-01-09', '2016-01-10', '2016-01-11']

    :param begin_date:
    :param end_date:
    :param format:
    :return:
    '''
    date_list = []
    begin_date = datetime.datetime.strptime(begin_date, format)
    end_date = datetime.datetime.strptime(end_date, format)
    while begin_date <= end_date:
        date_str = begin_date.strftime(format)
        date_list.append(date_str)
        begin_date += datetime.timedelta(days=1)
    return date_list
