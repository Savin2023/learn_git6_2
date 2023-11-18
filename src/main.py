import modules.sko_calc as calc
import numpy.random as random

a=random.random_integers(1,100,20)
print("Массив:",a)
print("\nСтандартное отклонение:", calc.sko(a))
