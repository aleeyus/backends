###########################################################################
# here is the begining may God help us                                    #
# please do make sure you left an explicit doumentation before commit     #
# do not jokes with any scope                                             #
###########################################################################


dynamic = 20
print("This is the first project\n"*10)

def classLess():
    for x in range(1,11):
        global dynamic
        x = x * dynamic
        dynamic = dynamic *10
        print(x)

classLess()
print()
print(dynamic)

class Call:
        def a(self):
                print('Im A of 65 keybord value')
        def b(self):
                print('Im B of 66 keybord value')
        def c(self):
                print('Im C of 67 keybord value')
                print('Im C of 67 keybord value')
print('')
#print("{.a:}, {0.b}, {0.c}".format(Call))
