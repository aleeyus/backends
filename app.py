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
        def a():
                print('Im A of 65 keybord value')
        def b():
                print('Im B of 66 keybord value')
        def c():
                print('Im C of 67 keybord value')

print("{0.a:}, {0.b}, {0.c}".format(Call))