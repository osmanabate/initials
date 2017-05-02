

#__author__: "osman abate"
#__version__: "1.0"
#date: 04/27/2017
#assignment: get_initials
#description: Given a users full name, return capitalized initials
#testcases..

def get_initials(fullname):
    name = (fullname)
    name_list = name.split()

    initials = ""

    for name in name_list:
        initials += name[0].upper()
    return initials


def main():
    print(get_initials(input('enter your name: \n\t')))
if __name__ == '__main__':
    main()
