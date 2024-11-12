class ZvysitelnaUrovenInterface:
    def zvysitUroven(self):
        raise NotImplementedError("This method must be implemented in the subclass")

class Archer(ZvysitelnaUrovenInterface):
    def __init__(self, accuracy):
        if type(accuracy) is not int or accuracy < 0 or accuracy > 5:
            raise Exception("Accuracy must be an integer between 0 and 5")
        self.accuracy = accuracy

    def zvysitUroven(self):
        if self.accuracy < 5:
            self.accuracy += 1
        else:
            print("Archer has reached maximum accuracy level")

class Healer(ZvysitelnaUrovenInterface):
    def __init__(self, healingPower, reviveAbility):
        if type(healingPower) is not bool:
            raise Exception("Healing power must be True/False")
        if type(reviveAbility) is not bool:
            raise Exception("Revive ability must be True/False")
        self.healingPower = healingPower
        self.reviveAbility = reviveAbility

    def zvysitUroven(self):
        if not self.healingPower:
            self.healingPower = True
        elif not self.reviveAbility:
            self.reviveAbility = True
        else:
            print("Healer already has both abilities")

# Testing
legolas = Archer(3)
legolas.zvysitUroven()
print(legolas.accuracy)  # Expected output: 4

elrond = Healer(False, False)
elrond.zvysitUroven()
print(elrond.healingPower)  # Expected output: True