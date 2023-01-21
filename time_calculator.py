def add_time(start, duration, day = "Today"):
  time = start.split()[0]
  clock= start.split()[1]
  s_hour = int(time.split(':')[0])
  s_minute = int(time.split(':')[1])
  d_hour = int(duration.split(':')[0])
  d_minute = int(duration.split(':')[1])
  
  # print(time)
  # print(clock)
  # print(s_hour)
  # print(s_minute)
  # print(d_hour)
  # print(d_minute)

  if clock == "PM":
    s_hour += 12
  # print(s_hour)

  new_hour = s_hour + d_hour
  # print("hour", new_hour)

  new_minute = s_minute + d_minute
  if new_minute > 59:
    new_minute -= 60
    new_hour += 1
  # print("minute", new_minute)
  # print("hour", new_hour)

  new_day = 0
  if new_hour > 23 and new_hour != 24:
    new_hour -= 24
    new_day += 1

  # print("new hour", new_hour)
  # print("day", new_day)
  
  new_clock = ""
  if new_hour == 24 or (0 < new_hour < 12):
    new_clock = "AM"
  else:
    new_clock = "PM"
  
  if new_hour > 12:
    new_hour -= 12
  
  # print("new clock", new_clock)
  # print("new hour", new_hour)

  hour = str(new_hour).zfill(2)
  minute = str(new_minute).zfill(2)
  output = hour + ':' + minute + ' ' + new_clock
  print(output)

add_time("10:06 AM", "0:55")