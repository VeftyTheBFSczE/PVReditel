from shutil import Error


def calculate_I(u,r): #funkce pro vypocet proudu
    return u/r
def calculate_R(u,i): #funkce pro vypocet odporu
    if i and u < 0:
        raise TypeError("Zadej cislo ve spravnych jednotkach! ")
    return u/i
def calculate_U(i,r): #funkce pro vypocet napeti
    return i*r

def calculate_Epsilon(q1,q2,r,epsilon_r): #funkce pro vypocet sily
    epsilon_0 = 0.00000000000885
    epsilon = epsilon_0 * epsilon_r  # Celková permitivita prostředí
    sila = (1 / (4 * 3.14 * epsilon)) * abs(q1 * q2) / (r ** 2)  # Sila v Newtonech
    return sila