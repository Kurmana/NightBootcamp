a = int(input('введите четырехзначное число - '))
pervoe_chislo = a//1000
vtoroe_chislo = a%1000//100
tretie_chislo = a%1000%100//10
chetvertoe_chislo = a%1000%10
if pervoe_chislo + chetvertoe_chislo == vtoroe_chislo - tretie_chislo:
    print('da')
else:
    print('net')
