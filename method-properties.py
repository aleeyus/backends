
# Create a class for travellers visiting defferent countries
# Tell something nice about the country


class Travellers:

    def __init__(self, fn, g, c, s):
        self.fullname = fn
        self.gender = g
        self.country = c
        self.state = s

    def bestThingAbout(self):
        gender = ['Mr.' if self.gender == 'Male' else '']
        if self.country == 'Nigeria':
            if self.state == 'Kaduna':
                print('{3} {0}, Welcome to {1} state, {2} the 3rd largest city in {2}'.format(self.fullname,self.state,self.country,gender))
        elif self.country == 'USA':
            if self.state == 'Califonia':
                print('Mr. {}, Welcome to {}, {} do make sure you visit HollyWood it\'s very nice place for tourist'.format(self.fullname,self.state,self.country))
print()
print()
dic = dict(fn='Aliyu Lawal',g='Male', c='USA', s='Califonia')
me = Travellers(**dic)

me.bestThingAbout()

class EmployeesData:
    # Our blueprint structure.
    def __init__(self, name):
        self.name = name
        self.email = self.name+'@'+'company.com'
    # Our blueprint datas
    def employeeProfile(self):
        mail = self.email
        print(self.name)
        print("".join(mail))

def outer(x):
    
    def nast(y):
        
        def nasted(z):
            return x * y * z
        return nasted(y)
    return nast(x)

print(outer(10))

"""def factorial(n):
    
    return n * factorial(n-1);

print(factorial(5))"""

#args

def arg(*args):
    acc = 0
    for x in args:
        acc += x
    return acc

print(arg(10,10))

# Reduce 

def mult(lst1):
    product = lst1[0]
    for i in range(1,len(lst1)):
        product *= lst1[i]
    return product

print(mult([1,2,3,4]))