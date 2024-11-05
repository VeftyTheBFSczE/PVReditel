epsilon_0 = 8.85e-12

def vypocet_sily(q1, q2, r, epsilon_r=1):
    if r <= 0:
        raise ValueError("Vzdálenost musí být kladné číslo.")
    epsilon = epsilon_0 * epsilon_r
    k = 1 / (4 * 3.14 * epsilon)
    return k * abs(q1 * q2) / (r ** 2)