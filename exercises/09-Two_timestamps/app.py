#Complete the funtion to compute how many seconds passed between the two timestamp.
def two_timestamp(hr1,min1,sec1,hr2,min2,sec2):
    hours_sec = (hr2 - hr1) * 3600
    minute_sec = (min2 - min1) * 60
    sec = (sec2 - sec1)

    return hours_sec + minute_sec + sec

#hours,minutes,seconds
#Invoke the fuction and pass two timestamps(6 intergers) as its argument.
print(two_timestamp(1,1,1,2,2,2))