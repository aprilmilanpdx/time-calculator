def add_time(start, duration, day = "today"):
  time = start.split()[0]
  clock= start.split()[1]
  s_hour = int(time.split(':')[0])
  s_minute = int(time.split(':')[1])
  d_hour = int(duration.split(':')[0])
  d_minute = int(duration.split(':')[1])
  
  if clock == "PM":
    s_hour += 12
  
  new_hour = s_hour + d_hour
  
  new_minute = s_minute + d_minute
  if new_minute > 59:
    new_minute -= 60
    new_hour += 1
  
  day_count = new_hour // 24
  new_hour = new_hour % 24

  new_clock = ""
  if new_hour == 24 or (0 <= new_hour < 12):
    new_clock = "AM"
  else:
    new_clock = "PM"
  
  if new_hour == 0:
    new_hour = 12
  elif new_hour > 12:
    new_hour -= 12
  
  day_string = ""
  if day_count == 1:
    day_string = "(next day)"
  elif day_count > 0:
    day_string = f"({day_count} days later)"

  day_lwr = day.lower()
  days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']

  if day_lwr == "today":
    pass
  else:
    day_index = days.index(day_lwr)
    new_index = day_count + day_index
    if new_index > 6:
      new_index = new_index % 7 
    new_day = days[new_index].capitalize()
      
  hour = str(new_hour)
  minute = str(new_minute).zfill(2)
  time = hour + ':' + minute + ' ' + new_clock

  spacer = ' ' if day_string != '' else ''
  
  if day_lwr == "today":
    new_time = time + spacer + day_string
  else:
    new_time = time + ', ' + new_day + spacer + day_string
  
  return new_time