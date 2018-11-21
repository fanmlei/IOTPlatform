from datetime import datetime, timedelta
from calendar import monthrange


def time_list(start_time, end_time):
    """
    根据起始时间和截至时间生成一个这个时间段的时间列表
    :param start_time: 起始时间 YYYY-MM-DD
    :param end_time: 终止时间 YYYY-MM-DD
    :return: list ['YYYY-MM-DD',.....]
    """
    dates = []
    dt = datetime.strptime(start_time, "%Y-%m-%d")
    date = start_time[:]
    while date <= end_time:
        dates.append(date)
        dt += timedelta(days=1)
        date = dt.strftime("%Y-%m-%d")
    dates.reverse()
    return dates


def day(time, days, method=1):
    """
    返回起始时间之前或之后的日期（默认之前）
    :param time: 截止日期 YYYY-MM-DD
    :param days: 天数
    :param method: 大于0返回起始日期之前的时间，小于0返回起始日期之后的时间
    :return: str  'YYYY-MM-DD'
    """
    dt = datetime.strptime(time, "%Y-%m-%d")
    if method > 0:
        dt -= timedelta(days=days)
    else:
        dt += timedelta(days=days)
    date = dt.strftime("%Y-%m-%d")
    return date


def apart(start_time, end_time):
    """
    返回两个时间段相隔天数
    :param start_time: 起始时间 YYYY-MM-DD
    :param end_time: 终止时间 YYYY-MM-DD
    :return: 相隔天数 int
    """
    start_dt = datetime.strptime(start_time, "%Y-%m-%d")
    end_dt = datetime.strptime(end_time, "%Y-%m-%d")
    return (end_dt - start_dt).days


def month(now, month):
    """
    获取前几个月或后几个月第一天和最后一天
    :param now: 当前时间
    :param month: 所隔月数,大于0 返回之前月份，小于0返回之后月份
    :return: list [start,end]
    """
    dt = datetime.strptime(now, "%Y-%m-%d")
    start = datetime(dt.year, dt.month-month, 1).strftime("%Y-%m-%d")
    end = datetime(dt.year, dt.month-month, monthrange(dt.year, dt.month-month)[1]).strftime("%Y-%m-%d")
    return [start, end]
