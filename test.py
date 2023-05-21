"""
1. Creational design pattern
Verious ways to create object to increase flexibility and reuse of existing code
1.1 Abstract factory
create families of related objects without specifying concrete classes
1.2 Builder
Using same code construct complex obj step by step with diff types and representation
1.3 Factory method


"""
class Person:
    def __init__(self,pid,pnm,pag,pgen):
        self.personId = pid
        self.personName = pnm
        self.personAge = pag
        self.pergen = pgen
    def __str__(self):
        return f'''
                Person Id : {self.personId}
                Person Name : {self.personName}
                Person Age : {self.personAge}
                Person gender: {self.pergen}
        '''
    def __repr__(self):
        return str(self)


p1 = Person(101,"ABCD",22,"M")
p1.newprop = "ABC"
print(p1.__dict__)
# {'personId': 101, 'personName': 'ABCD', 'personAge': 22, 'pergen': 'M', 'newprop': 'ABC'}
del p1.newprop
print('After deletion-')
print(p1.__dict__)
# After deletion-
# {'personId': 101, 'personName': 'ABCD', 'personAge': 22, 'pergen': 'M'}
