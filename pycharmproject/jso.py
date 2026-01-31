from datetime import date, datetime,time,timedelta
dt=datetime.now()
print("Введите вашу дату рождения:")
d=int(input("день : "))
m=int(input("Месяц : "))
y=int(input("Год(полностью) : "))
born=datetime(y,m,d)
age=dt.year-born.year
if dt.month<born.month:
    age-=1
    print(age)
else:
    print(age)
print(born)
