#This file will hold all of the functions which will support the program.

#This class will provide support methods for the program
class Support():

    #This method is what will allow the user to quit out of the program
    def quit(self):
        print('\033c')
        print('Program is now quitting')
        print('Thank you for using it!')
        input('Press enter to close the program ')
