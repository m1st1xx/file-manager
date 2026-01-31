try:
    arr=[]
    with open("numbs.txt","r") as file:
        rows=file.readlines()
    for row in rows:
        nu=int(row.strip())
        arr.append(nu)
except FileNotFoundError:
    print("ДУРА ФАЙЛ СОЗДАЙ")
except ValueError:
    print("ДУРА ТОЛЬКО ЦИФРЫ")
else:
    summ=sum(arr)
    print(summ)
finally:
    print("VSE")
