import modules.sko_calc as calc
import numpy.random as random

a=random.random_integers(1,1000,40)
print("Массив:",a)
print("\nСтандартное отклонение:", calc.sko(a))
