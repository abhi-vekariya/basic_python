#Base Class
class Person():
    def __init__(self):
        pass

    def save(self):
        print("Parent's Save")

#Child Class
class Child(Person):
    def __init__(self):
        pass

    def save(self):
        print("Child's save")

#make one object
c = Child()
c.save()