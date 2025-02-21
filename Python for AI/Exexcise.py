import time
mytime = time.strftime('%H:%M:%S')
print(mytime)
hour = int(time.strftime('%H'))
print(hour)
if(hour > 4 and hour < 12):
    print('Good Morning Sir')
elif(hour >= 13 and hour < 17):
    print('Good Afternoon Sir')
elif(hour >= 17 and hour < 22):
    print('Good Evening Sir')
else:
    print('Good Night Sir')