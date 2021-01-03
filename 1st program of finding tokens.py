n=input("Enter Expression \n =>")
opr = [42,43,45,47,61,94]
total_token,var,operater,const = 0,0,0,0
for i in range(len(n)):
    if n[i].isalpha():
        var+=1
    elif ord(n[i]) in opr :
        operater+=1
    elif n[i].isnumeric():
        try:
            if n[i-1].isnumeric():
                pass
            else:
                const+=1
        except:
            pass
print(f"operators = {operater}\nvariables = {var}\nConstant = {const}")
print(f"total Tokens = {operater+var+const}")
