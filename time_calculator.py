def changePeriod(p):
  if(p == "AM"):
    return "PM"
  else:
    return "AM"

def changeDate(dat):
  dates = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"];
  
  if(dat in dates):
    if(dates.index(dat) == 6):
      return "Monday"
    else:
      return dates[dates.index(dat)+1]
  return ""

def setDate(num):
  dates = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"];
  return dates[num]

def add_time(start, duration, *optional):
  count = 0;
  dates = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"];
  dat = ""
  #print(optional)
  if(optional != ()):
    if(optional[0].lower() in dates):
      dat = setDate(dates.index(optional[0].lower()))
  
  [tim, period] = start.split(" ")
  [h,m] = tim.split(":")
  [addh, addm] = duration.split(":")

  #Deals with hours
  for i in range(int(addh)):
    if(int(h) + 1 == 12):
      h = 12
    elif(int(h) + 1 > 12):
      h = 1
      if(period == "PM"):
        count += 1
        dat = changeDate(dat)
      period = changePeriod(period);     
    else:
      h = int(h) + 1
    

  #Deals with minutes
  if(int(m) + int(addm) > 60):
    m = int(m) + int(addm) - 60
    if(int(h) + 1 == 12):
      h = 12
      if(period == "PM"):
        count += 1;
        dat = changeDate(dat)
      period = changePeriod(period);
    else:
      h = int(h) + 1
  else:
    m = int(m) + int(addm)

  if(dat == ""):
    if(count > 0):
      if(count == 1):
        if(m < 10):
          return str(h) + ":" + "0"+str(m) + " " + period + " (next day)"
        else:
          return str(h) + ":" +str(m) + " " + period + " (next day)"
      else:
        if(m < 10):
          return str(h) + ":" + "0"+str(m) + " " + period + " ("+ str(count) + " days later)"
        else:
          return str(h) + ":" + str(m) + " " + period + " ("+ str(count) + " days later)"
    if(m < 10):
      return str(h) + ":" +"0"+str(m) + " " + period
    else:
      return str(h) + ":" + str(m) + " " + period
  else:
    if(count > 0):
      if(count == 1):
        if(m < 10):
          return str(h) + ":" + "0"+str(m) + " " + period + ", " + dat + " (next day)"
        else:
          return str(h) + ":" + str(m) + " " + period + ", " + dat + " (next day)"
      else:
        if(m < 10):
          return str(h) + ":" + "0"+str(m) + " " + period + ", " + dat + " ("+ str(count) + " days later)"
        else:
          return str(h) + ":" + str(m) + " " + period + ", " + dat + " ("+ str(count) + " days later)"
    if(m < 10):
      return str(h) + ":" + "0"+str(m) + " " + period + ", " + dat
    else:
      return str(h) + ":" + str(m) + " " + period + ", " + dat

