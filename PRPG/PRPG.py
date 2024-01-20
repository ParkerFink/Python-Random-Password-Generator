import random
import time

library = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']


random.shuffle(library)

shuffleLibrary = library
newPassword = ''.join(shuffleLibrary)

with open('password.txt', 'w') as outFile:
    outFile.write("Password: " + newPassword)
    print("Password: " + newPassword)

print("Password Generated: Program will close in 10 seconds")
time.sleep(10)