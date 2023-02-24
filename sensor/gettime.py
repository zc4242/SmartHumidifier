import time


def time_str(time):
    return f'{time[0]}-{time[1]}-{time[2]} {time[3]}：{time[4]}：{time[5]}'


def time_now_str():
    current_time = time.localtime()
    return time_str(current_time)
