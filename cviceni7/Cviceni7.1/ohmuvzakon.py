"""
Kalkulace proudu
"""

def vypocet_proudu(U, R):
    if U > 0 and R > 0:
        return U / R
    else:
        raise ValueError("Napětí a odpor musí být kladné číslo.")

"""
Kalulace napětí
"""
def vypocet_napeti(I, R):
    if I < 0 or R < 0:
        raise ValueError("Proud a odpor musí být kladné číslo.")
    return I * R

"""
Kalkulace odporu
"""

def vypocet_odporu(U, I):
    if U < 0 or I < 0:
        raise ValueError("Napětí a proud musí být kladné číslo.")
    return U / I

"""
Kalulace výkonu
"""


def vypocet_vykonu(U, I):
    if U < 0 or I < 0:
        raise ValueError("Napětí a proud musí být kladné číslo.")
    return U * I
