'''

filename: circleArea.py             
                                                     
This program asks the user to input a               
number for the radius of a circle.  The program     
then calculates and output the area of the circle.
import math
import sys
radius = float(input( "Enter radius in feet : " )) 
area = math.pi * radius * radius 
sys.stdout.write("The radius you provided was " + format(radius,'.2f') +
                " feet and the area is about " + format(area,'.2f') + " sq feet" )
Write a function called computeArea() which will compute the area of a circle
given the radius. The function should receive the radius in a parameter list
and return the computed area as the function returns value. A sample call to the
function would be as follows:
area = computeArea(radius)

Modify the program circleArea.py given above to make use of this function.
'''
import math
import sys
def computeArea(radius)
  return math.pi * radius ** 2
radius = float(input( "Enter radius in feet : " )) 
area = math.pi * radius ** 2
sys.stdout.write("The radius you provided was " + format(radius,'.2f') +
                " feet and the area is about " + format(computeArea(radius),'.2f') + " sq feet" )
