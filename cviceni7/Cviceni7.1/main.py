# Import the package
import elektrotechnicutils.ohm as ohm
import elektrotechnicutils.coulomb as coulomb

# Ohm's law calculations
print(ohm.vypocet_proudu(0.01, 1000))
print(ohm.vypocet_odporu(0.001, 3))
print(ohm.vypocet_napeti(0.020, 20))

# Coulomb's law calculation
q1 = 50e-9  # 50 nC to C
q2 = 70e-9  # 70 nC to C
r = 0.01    # 1 cm to m
epsilon_r = 1  # permitivita vzduchu

sila = coulomb.vypocet_sily(q1, q2, r, epsilon_r)
print(f"{sila:.6e} N")