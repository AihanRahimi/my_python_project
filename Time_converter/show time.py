#user enter second and this code show all days,hours,min,sec
seconds = int(input('enter seconds:'))
days = seconds//86400
x = seconds % 86400
hours = x //3600
y =hours % 3600
min = y // 60
p = min % 60 
sec= p
print(days,'days',hours,'hours',min,'min',sec,'seconds')