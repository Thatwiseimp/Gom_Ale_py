roman_dict={
    'I':1,
    'V':5,
    'X':10,
    'L':50,
    'C':100,
    'D':500,
    'M':1000
    }

def numerize(symbol):
    Total=0
    symbol=symbol.upper()
    rev_symbol=symbol[::-1]
    for i in range(len(symbol)):
        if i<1:
            Total+=roman_dict[(rev_symbol[i])]
        else: 
            if (roman_dict[(rev_symbol[i])]>=roman_dict[(rev_symbol[i-1])]):
                Total+=roman_dict[(rev_symbol[i])]
            else:
                Total-=roman_dict[(rev_symbol[i])]
    return Total


def evaluate(symbols,option):
    compute_result=0   
    count=0 
    list=[]
    for symbol in symbols:
        ans=numerize(symbol)
        list.append(ans)
        if count==0:
            compute_result+=ans
            count+=1
        else:
            if option==2:
                compute_result+=ans
            elif option==3:
                compute_result-=ans
            elif option==4:
                compute_result*=ans
            elif option==5:
                compute_result/=ans

    if option==1:
        print(*list)
    else:
            print(compute_result)       


calc_option=int(input('Enter an operation: '))
romanNumeral=list(input('Enter the numbers:').split(','))
evaluate(romanNumeral,calc_option)