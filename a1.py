#CPS109 - By: Roxie Reginold
#Having a hard time in Physics, specifically PCS110? Keep getting the wrong answer on your calculator?
#This program is a Physics Calculator that solves some of the challenging 3D Physics problems.
#This program will decrease the stress involved with Physics calculations and increase productivity.
#The user will enter a number that coorresponds with the problem they need to solve.

import math #import the math module to be able to square root and round numbers

def Physics_Topics(): #this is a function to display topics to user
    print("Physics topics: ")
    print("1. Finding a unit vector using r/|r|")
    print("2. Finding Vavg using deltar/deltat ")
    print("3. Finding the momentum using p = mv ")
    print("4. Using the Momentum Principle (deltap = Fnet*deltat)")
    print("5. Finding the future momentum of a system using pf = pi + Fnet*deltat ")
    print("6. Finding the vevtor force by a spring (Fspring = -ksL, L is a unit vector) ")
    print("7. Finding the gravitational force ")
    print("8. Finding the electric force ")
    print("Type 0 to exit") # the user will type 0 to exit the program 

input_value = False # set the imput to false until the user enters a value
Physics_Topics() # display topics
prompt = int(input("Which topic do you need help with today?: ")) # ask user for the topic number they want
print("\n") # newline 
    
def unitvector(): # this is a function for 1) that calculates the unitvector of a vector
    print("Finding a unit vector from a vector:") #ask user for user input for information needed
    xcomp = float(input("x-component of vector = "))
    ycomp = float(input("y-component of vector = "))
    zcomp = float(input("z-component of vector = "))
    magv = math.sqrt((xcomp**2) + (ycomp**2) + (zcomp**2)) # find magnitude of the vector
    print("vector = <", xcomp, ",", ycomp, ",", zcomp, "> [units]")
    print("|v| =", round(magv,12),"[units]")
    unitvx = xcomp / magv
    unitvy = ycomp / magv
    unitvz = zcomp / magv
    print("unit vector = <", round(unitvx,5), ",", round(unitvy,5), ",", round(unitvz,5), ">") #display answer


def Vaverage(): # this is a function for 2) that calculates the average velocity
    print("Finding average velocity from the change in postion / change in time") #ask user for user input for information needed
    rfinalx = float(input("x component of final position = "))
    rfinaly = float(input("y component of final position = "))
    rfinalz = float(input("z component of final position = "))
    rintialx = float(input("x component of intial position = "))
    rintialy = float(input("y component of intial position = "))
    rintialz = float(input("z component of intial position = "))
    
    tfinal = float(input("final time = "))
    tinitial = float(input("intial time = "))
    if tfinal <= tinitial: #the final time cannot be less than initial time, ask the user to try again
        print("Try again!")
        tfinal = float(input("final time = "))
        tinitial = float(input("intial time = "))
    #calulate values from imputed values that are needed to solve this Physics problem
    deltarx = rfinalx - rintialx
    deltary = rfinaly - rintialy
    deltarz = rfinalz - rintialz

    deltat = tfinal - tinitial
    vavgx = deltarx / deltat
    vavgy = deltary / deltat
    vavgz = deltarz / deltat

    print("Vavg = deltar / deltat") #display answer
    print("     = <",deltarx, ",",deltary, ",", deltarz, "> /",deltat)                   #units may vary for velocity
    print("     = <", round(vavgx,10), ",", round(vavgy,10), ",", round(vavgz,10), "> [unitPOSiTION/ unitTIME]") #answers are rounded to 10 decimal places
    

def Momentum(): #this is a function for 3) that calculates the momentum
    mass = float(input("Mass of the object in kilograms: ")) #ask user for user input for information needed
    vx = float(input("x component of velocity of the object in m/s: "))
    vy = float(input("y component of velocity of the object in m/s: "))
    vz = float(input("z component of velocity of the object in m/s: "))
    momentumx = mass * vx
    momentumy = mass * vy
    momentumz = mass * vz #display answer
    print("The momentum is: <", round(momentumx,10), ",", round(momentumy,10), ",", round(momentumz,10), "> [kg x m/s]" )


def M_Principle(): #this is a function for 4) that calcualtes the momentum using the momentum principle
    Fnetx = float(input("x component of Net force of the object in Newtons: ")) #ask user for user input for information needed
    Fnety = float(input("y component of Net force of the object in Newtons: "))
    Fnetz = float(input("z component of Net force of the object in Newtons: "))
    tfinal = float(input("final time = "))
    tinitial = float(input("intial time = "))
    if tfinal <= tinitial:
        print("Try again!")
        tfinal = float(input("final time = "))
        tinitial = float(input("intial time = "))
    deltat = tfinal - tinitial
    momentumx = Fnetx * deltat
    momentumy = Fnety * deltat
    momentumz = Fnetz * deltat #display answer
    print("The momentum is: <", round(momentumx, 10), ",", round(momentumy,10), ",", round(momentumz,10), "> [kg x m/s]" )

    
def futureMomentum(): #this is a function for 5) that calculates the future momentum of a object/system using a variation of the momentum principle
    pinitialx = float(input("x component of inital momentum = ")) #ask user for user input for information needed
    pinitialy = float(input("y component of inital momentum = "))
    pinitialz = float(input("z component of inital momentum = "))
    Fnetx = float(input("x component of Net force of the object in Newtons: "))
    Fnety = float(input("y component of Net force of the object in Newtons: "))
    Fnetz = float(input("z component of Net force of the object in Newtons: "))
    tfinal = float(input("final time = "))
    tinitial = float(input("intial time = "))
    if tfinal <= tinitial:
        print("Try again!")
        tfinal = float(input("final time = "))
        tinitial = float(input("intial time = "))
    deltat = tfinal - tinitial
    impulse_x = Fnetx * deltat
    impulse_y = Fnety * deltat
    impulse_z= Fnetz * deltat
    pfx = pinitialx + impulse_x
    pfy = pinitialy + impulse_y
    pfz = pinitialz + impulse_z #display answer
    print("The fimal momentum is: <", round(pfx,10), ",", round(pfy,10), ",", round(pfz,10), "> [kg x m/s]" )


def VectorSpringForce(): #this is a function for 6) that calculates for Spring Force
    k = float(input("Enter the spring constant = ")) #ask user for user input for information needed
    Lxcomp = float(input("Enter the x component of the current length = "))
    Lycomp = float(input("Enter the y component of the current length = "))
    Lzcomp = float(input("Enter the z component of the current length = "))
    relaxedL = float(input("Enter the relaxed length of the spring = "))
    magL = math.sqrt((Lxcomp**2) + (Lycomp**2) + (Lzcomp**2)) #use squareroot to find magnitude
    unitvLx = Lxcomp / magL #do neccesary internal calculations to solve problem
    unitvLy = Lycomp / magL
    unitvLz = Lzcomp / magL
    s = magL - relaxedL
    Fspringx = - k * s * unitvLx
    Fspringy = - k * s * unitvLy
    Fspringz = - k * s * unitvLz #display answer
    print("Fspring = <", round(Fspringx,10), ",", round(Fspringy,10), ",", round(Fspringz,10), "> N")


def GravitationalForce(): #this is function for 7) that calculates the Gravitational Force
    G = 6.7e-11 #define constant
    m1 = float(input("Mass of first object = ")) #ask user for user input for information needed
    m2 = float(input("Mass of second object = "))
    print("r is a vector that extends from the center of the first object to the center of the second object.")
    r2x = float(input("x component of second position = "))
    r2y = float(input("y component of second position = "))
    r2z = float(input("z component of second position = "))
    r1x = float(input("x component of first position = "))
    r1y = float(input("y component of first position = "))
    r1z = float(input("z component of first position = "))
    vector_rx = r2x - r1x #do neccesary calculations to find answer
    vector_ry = r2y - r1y
    vector_rz = r2z - r1z
    mag_r = math.sqrt((vector_rx**2) + (vector_ry**2) + (vector_rz**2))
    unitvectorx = -vector_rx / mag_r
    unitvectory = -vector_ry / mag_r
    unitvectorz = -vector_rz / mag_r
    Fmagnitude = (G * m1 *m2)/ mag_r**2
    Fg_2by1x = Fmagnitude * unitvectorx
    Fg_2by1y = Fmagnitude * unitvectory
    Fg_2by1z = Fmagnitude * unitvectorz 
    #display answer
    print("Fgrav on 2 by 1 = ",Fmagnitude, " x <",unitvectorx, ",", unitvectory, ",", unitvectorz ,",> N" )
    print("Fgrav on 2 by 1 = <", Fg_2by1x, ",", Fg_2by1y, ",", Fg_2by1z, "> N" )
    


def ElectricForce(): #this is a function for 8) to find the Electric force
    Uconstant = 9e9 #define constant
    q1 = float(input("Charge of first object = ")) #ask user for user input for information needed
    q2 = float(input("Charge of second object = "))
    print("r is a vector of postion 2 relative to postion 1.")
    r2x = float(input("x component of second position = "))
    r2y = float(input("y component of second position = "))
    r2z = float(input("z component of second position = "))
    r1x = float(input("x component of first position = "))
    r1y = float(input("y component of first position = "))
    r1z = float(input("z component of first position = "))
    vector_rx = r2x - r1x
    vector_ry = r2y - r1y
    vector_rz = r2z - r1z
    mag_r = math.sqrt((vector_rx**2) + (vector_ry**2) + (vector_rz**2)) #find magnitude by using squareroot
    unitvectorx = vector_rx / mag_r
    unitvectory = vector_ry / mag_r
    unitvectorz = vector_rz / mag_r
    Fmagnitude = (Uconstant * q1 *q2)/ mag_r**2
    Fe_2by1x = Fmagnitude * unitvectorx
    Fe_2by1y = Fmagnitude * unitvectory
    Fe_2by1z = Fmagnitude * unitvectorz
    #display answer
    print("Fgrav on 2 by 1 = ",Fmagnitude, " x <",unitvectorx, ",", unitvectory, ",", unitvectorz ,",> N" )
    print("Fgrav on 2 by 1 = <", Fe_2by1x, ",", Fe_2by1y, ",", Fe_2by1z, "> N" )

def topic_numbers(input_value): #this function is for calling the right functions accociated to a number
    #if the user enters number 1 through 8 inclusive the program will loop until the user exits with 0
    if prompt == 1: #if the user enters 1 call the unit_vector function 
        input_value = True
        unitvector()
    elif prompt == 2: #if the user enters 2 call the Vaverage function 
        input_value = True
        Vaverage()
    elif prompt == 3: #if the user enters 3 call the Momentum function 
        input_value = True
        Momentum()
    elif prompt == 4:#if the user enters 4 call the M_Principle function 
        input_value = True
        M_Principle()
    elif prompt == 5:#if the user enters 5 call the futureMomentum function 
        input_value = True
        futureMomentum()
    elif prompt == 6:#if the user enters 6 call the VectorSpringForce function 
        input_value = True
        VectorSpringForce()
    elif prompt == 7:#if the user enters 7 call the GravitationalForce function 
        input_value = True
        GravitationalForce()
    elif prompt == 8:#if the user enters 8 call the ElectricForce function 
        input_value = True
        ElectricForce()
    
    if prompt < 0 or prompt > 8 : #numbers less than 0 and greater than 8 will be errors
        input_value = False
        print("Error") 
    elif prompt == 0: #if the user enters 0 print Goodbye message
        input_value = False
        print("Goodbye!") 
    return input_value #return true if user enters numbers from 1 to 9

x = topic_numbers(input_value) #variable x stores True of False based off user input

while x == True: #if x returns true then loop the user input question again until user exits program
    input_value = True
    print("\n")
    Physics_Topics()
    prompt = int(input("Which other topic do you need help with today?: "))
    print("\n")
    x = topic_numbers(input_value) #store True/False 


thoughts = input("How do you feel about Physics? Type Easy, Challenging or Depressed: ")#ask user how they feel about Physics after exit
#if the user enters a certain word, print a message
if thoughts == "Easy" or thoughts == "easy" or thoughts == "EASY":
    print("Great! Hope you enjoyed it!")
elif thoughts == "Challenging" or thoughts == "challenging" or thoughts == "CHALLENGING":
    print("Yes it is! You will get the hang of it!")
elif thoughts == "Depressed" or thoughts == "depressed" or thoughts == "DEPRESSED":
    print("Honestly its fine! You will understand eventually! You got this!")
else:
    print("Thank you for your input! Have a good day!")


