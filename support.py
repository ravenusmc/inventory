#This file will hold all of the functions which will support the program.

#This class will provide support methods for the program
class Support():

    #This method is what will allow the user to quit out of the program
    def quit(self):
        print('\033c')
        print('Program is now quitting')
        print('Thank you for using it!')
        input('Press enter to close the program ')

    #This method will explain the purpose of the program.
    def help(self):
        print('\033c')
        print('''
        The purpose of this program is to track the amount of Toilet
        paper in each bathroom in my house. I figure that it will be a good way
        to really practice with the Mongo DB. Other than that, there really is
        not anything that special about this program. ''')
        print()
        input('\tPress Enter to continue ')
