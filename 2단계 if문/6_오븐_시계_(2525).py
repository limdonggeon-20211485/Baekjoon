hour, minute = map(int, input().split())
time = int(input())
time_hour = time // 60
time_minute = time - (time_hour * 60)

hour += time_hour
minute += time_minute

if minute >= 60:
    hour += 1
    minute -= 60

if hour >= 24:
    hour -= 24

print(hour, minute)