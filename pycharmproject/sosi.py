try:
    def dele(a, b):
        n=a/b
        print(n)
    a=int(input())
    b=int(input())
    dele(a, b)

except ValueError:
    print("DURA CHTOLI? CHISLA NADO")
except ZeroDivisionError:
    print("Dura na nol nelzya delit")
