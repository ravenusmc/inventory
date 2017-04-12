#This file will be what creates the admin user into the program. I normall would
#not do this if I was using this program in a real world situation.

#importing files which will be used in this files
import bcrypt

#This class will create the user and encrpy the admin password
class Create():

    #This method will encrpy the passwood. In a real world example this would
    #actually be hidden so that a bad person AKA a hacker, does not use the
    #password. The main purpose of this code is just to see how to use bcrypt.
    def encrypt_pass(self):
        password = b"AdminTest"
        hashed = bcrypt.hashpw(password, bcrypt.gensalt())
        return password, hashed
