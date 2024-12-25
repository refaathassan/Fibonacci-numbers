in_number=int(input("please enter your number:   "))
def fobin_num(inde):
    if inde<=0 : 
        return 0
    elif inde ==1 or inde==2 : 
        return 1
    else : 
        return fobin_num(inde-1)+fobin_num(inde-2)

for i in range(in_number+1):
    print(fobin_num(i))