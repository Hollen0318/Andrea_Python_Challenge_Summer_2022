import time

currentTime = time.time() # Get current time

# Obtain the total second since midnight, Jan 1, 1970
totalSeconds = int(currentTime)

#Get the current second
currentSecond = totalSeconds % 60

#Obtain the total minutes
totalMinutes = totalSeconds//60

#Compute the current minute in the hour
currentMinute = totalMinutes % 60

#Obtain the total hours
totalhours = totalMinutes//60

#Compute the current houur
currentHour= totalhours % 24

#Display results
print("Current time is ",currentHour,":",
      currentMinute,":", currentSecond,"GMT")

