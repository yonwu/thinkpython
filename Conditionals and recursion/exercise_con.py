import time

time_epoch = time.time()

days_passed_till_today = time.time() / (60 * 60 * 24)
days_passed_till_yesterday = int(days_passed_till_today)
days_passed_today = days_passed_till_today - days_passed_till_yesterday

time_hours = days_passed_today * 24
time_minutes = (time_hours - int(time_hours)) * 60
time_seconds = (time_minutes - int(time_minutes)) * 60

print(time_hours)
print(time_minutes)
print(time_seconds)

print("the time is %d:%d:%d" % (int(time_hours), int(time_minutes), int(time_seconds)))
