print('Feature1')
print('Feature2')
print('Feature3')
print('Feature4')
a=10
b=20
print('The addition is', a+b)


def multiplication_or_addition(num1,num2):
    product = num1*num2
    if product <=1000:
        return product
    else:
        return num1+num2
    

result  = multiplication_or_addition(20,30)
print('The Result is', result)

result= multiplication_or_addition(40,50)
print('The result is', result)