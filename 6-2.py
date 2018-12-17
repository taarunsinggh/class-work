#6-2. Favorite Numbers: Use a dictionary to store people’s favorite numbers.
#Think of five names, and use them as keys in your dictionary. Think of a favorite
#number for each person, and store each as a value in your dictionary. Print
#each person’s name and their favorite number. For even more fun, poll a few
#friends and get some actual data for your program.


numbers={
    'ankit':2,
    'vibhor':5,
    'aniket':7,
    'hitesh':8,
    'udit':3,   

    }
    
num = numbers['ankit']
print("ankit's favorite number is " + str(num))

num = numbers['vibhor']
print("vibhor's favorite number is " + str(num)  )

num = numbers['aniket']
print("aniket's favorite number is " + str(num)  )

num = numbers['hitesh']
print("hitesh's favorite number is " + str(num)  )

num = numbers['udit']
print("udit's favorite number is " + str(num)  )