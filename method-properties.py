
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
