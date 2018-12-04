import datetime
import re

def guard_watch(schedule):
    current_leader = None
    most_minutes_slept = 0
    minute_most_likely_asleep = 0
    for k, v in process_shifts(schedule).items():
        total_mins_asleep = sum(v.values())
        minute_most_slept_through = max(v.values())
        if total_mins_asleep >= most_minutes_slept:
            current_leader = k
            most_minutes_slept = total_mins_asleep
            minute_most_likely_asleep = [min for min, freq in v.items() if freq == minute_most_slept_through]

    return int(current_leader) * minute_most_likely_asleep.pop()

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

def process_shifts(entries):
    guard_pattern = re.compile(r'^.*#(?P<guard_id>\d*)')
    minute_pattern = re.compile(r'^.*:(?P<minute>\d{2})\]')
    guards = {}
    current_guard = []
    entries = sort_log(entries)
    for entry in entries:
        if "begins shift" in entry:
            guards = tally_shift(current_guard, guards)
            current_guard = []
            current_guard.append(guard_pattern.search(entry).group('guard_id'))
        elif "falls asleep" in entry:
            current_guard.append(minute_pattern.search(entry).group('minute'))
        else:
            current_guard.append(minute_pattern.search(entry).group('minute'))
    return tally_shift(current_guard, guards)


print(guard_watch(open('test_input.txt', 'r')))
