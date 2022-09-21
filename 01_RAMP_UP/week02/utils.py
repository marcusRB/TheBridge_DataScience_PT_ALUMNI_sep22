from datetime import datetime

# Creamos la función
def get_average_age(birth_year):
    '''
    DocString:

    Parameter:
    --------
        birh_year: int o list int

    Return:
    ------

        average or list
    '''
    # Recogemos el valor YEAR actual desde datetime.today
    # .year sacará el valor anyo
    this_year = datetime.today().year # esta variable se llama local

    # Calculamos las edades
    ages = []
    for year in birth_year:
        # procedemos con el calculo de edad this_year - birth_year
        age = this_year - year
        # Procedemos con almacenar la variable anterior
        ages.append(age)
    print("***"*20)
    print(ages) # mostramos el resultado parcial en pantalla

    # calculamos el promedio
    age_sum = sum(ages)
    n_people = len(ages)
    age_mean = age_sum / n_people

    print("/#"*20)

    # print(ages)
    return age_mean


# Calculamos el cuadrado
def square_number(x):
    print(x**2)