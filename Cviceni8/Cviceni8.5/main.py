class A:
    def __init__(self):
        self.a_variable = True

    def test(self):
        print("A's test method")

class B:
    def __init__(self):
        self.b_variable = True

    def test(self):
        print("B's test method")

class C(A, B):
    def __init__(self):
        A.__init__(self)
        B.__init__(self)

c_instance = C()
print(hasattr(c_instance, 'a_variable'))  # Check if a_variable is set
print(hasattr(c_instance, 'b_variable'))  # Check if b_variable is set