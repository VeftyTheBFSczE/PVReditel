import math

required_number_of_plants = 14513
germination = 0.8
survival_after_germination = 0.08
seeds_in_package = 100

efficiency_of_germination = germination * seeds_in_package
required_number_of_seeds = efficiency_of_germination * survival_after_germination
probability = efficiency_of_germination - required_number_of_seeds
number_of_packages = required_number_of_plants / probability
number_of_packages_rounded = math.ceil(number_of_packages)

print(number_of_packages_rounded)


