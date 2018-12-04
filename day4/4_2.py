import datetime
import re

def guard_watch(schedule):
    guards = {}
    guard_pattern = re.compile(r'^.*#(?P<guard_id>\d*)')
    minute_pattern = re.compile(r'^.*:(?P<minute>\d{2})\]')
    current_guard = []
    current_leader = None
    max_global_frequency = 0
    entries = sort_log(schedule)
    for entry in entries:
        if "begins shift" in entry:
            guards = tally_shift(current_guard, guards)
            current_guard = []
            current_guard.append(guard_pattern.search(entry).group('guard_id'))
        elif "falls asleep" in entry:
            current_guard.append(minute_pattern.search(entry).group('minute'))
        else:
            current_guard.append(minute_pattern.search(entry).group('minute'))
    guards = tally_shift(current_guard, guards)
    for k, v in guards.items():
        max_freq = max(v.values())
        if max_freq >= max_global_frequency:
            max_global_frequency = max_freq
            current_leader = k
            most_freq = [min for min, freq in v.items() if freq == max_freq][0]

    return int(current_leader) * most_freq

def sort_log(log):
    log = [line.split("]") for line in log]
    log = sorted(log, key=lambda x: datetime.datetime.strptime(x[0], "[%Y-%m-%d %H:%M"))
    return [line[0] + "]" + line[1] for line in log]

def tally_shift(current_guard, guards):
    try:
        previous_shift = current_guard.pop(0)
        if previous_shift not in guards.keys():
            guards[previous_shift] = dict((k, 0) for k in range(60))
    except IndexError:
        pass
    while len(current_guard) > 0:
        guard = guards[previous_shift]
        range_start = int(current_guard.pop(0))
        range_end = int(current_guard.pop(0))
        for m in range(range_start, range_end):
            guard[m] += 1
    return guards


print(guard_watch(open('input.txt', 'r')))
