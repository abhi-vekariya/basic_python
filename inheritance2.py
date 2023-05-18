class Calc:
    #Class Vaiable
    num1 = 100
    #Constructor
    def __init__(self,a,b):
        #Instance Variable
        self.a = a
        self.b = b
    def calc_summary(self):
        return self.a + self.b + Calc.num1

    def calc_total(self):
        return self.a + self.b + self.calc_summary()
class ChildCalc(Calc):
    num2 = 100

    def child_summ(self):
        return self.calc_summary() + self.num2 + self.num1

# obj = Calc(10,20)
# print(obj.calc_summary())
# print(obj.calc_total())

obj2 = ChildCalc(10,20)
print(obj2.child_summ())