def calculate_compound_intrest(princial,rate,time):
    #convert rate from percentage to decimal
    rate_decimal=rate/100
    #caculate the compound intrest
    amount=principal*(1+rate_decimal)**time
    compound_intrest=amount-principal
    return compound_intrest
#input values
principal=float(input("entre the principal amount:"))
rate=float(input("entre the annual intrest rate(in percentage):"))
time=float(input("entre the number of periods:"))
#calculate the compound intrest
intrest=calculate_compound_intrest(principal,rate,time)
print(f"the compound intrest is :{intrest:2f}")
                                       
