#Дано**:** пользователь делает вклад в размере Х рублей сроком на Y лет под 10% годовых 
# (каждый год размер его вклада увеличивается на 10%, эти деньги прибавляются к сумме вклада, 
# и на них в следующем году тоже будут проценты).
#Задача: написать функцию bank, принимающую аргументы X и Y и возвращающую сумму,
#  которая будет на счету пользователя спустя Y лет.



def bank (x , y ):

    sum = x
    for f in range( 1, y ):
        sum1 = x * 0.1 + sum
        sum = sum1* 0.1 + sum1
        return(sum)
print(bank (50 ,2))


