import math
print("A ladder is put up right against a wall")
h = int(input("Enter the height of the ladder ")) 
angle = int(input("The ladder is inclined to the wall at an angle of ")) #angle in degrees
radians = (math.pi * angle)/180
sine = math.sin(radians)
l = round(h * sine,2)
print("The height reached by a ladder having height",h,"inclined at",angle,"is",l,"feet",sep=" ")

#output
#The height reached by a ladder having height 16 inclined at 75 is 15.45 feet
#The height reached by a ladder having height 20 inclined at 0 is 0.0 feet
#The height reached by a ladder having height 24 inclined at 45 is 16.97 feet
#The height reached by a ladder having height 24 inclined at 80 is 23.64 feet