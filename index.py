"""
CE_Computational_Project

Important Variable List:(Ones not included are not important in the overall outlook of the project)
    LengthOfBeam 
    SupportPositionCoordinates[]
    NumberOfForces
    NumberOfSupports
    ForcesActing[]
    ReactionForces[] 
    SumOfForces
    MomentOfForces - (from origin)
"""
# importing numpy(not now but can be considered with expansion of project)
import numpy as np

# Initial instructions & guidelines
print(
    "NOTE : The origin of the axis is taken at the left end of the beam and all the distances are measured from the origin. \n For the load acting on the beam, downwards direction is considered positive."
)

# Input length of beam
LengthOfBeam = int(input("Enter the length of the beam : "))

# Input number of supports
NumberOfSupports = int(input("Enter the number of supports:"))

# List of support co-ors
SupportPositionCoordinates = []

# Input the co-ors of supports
for i in range(0, NumberOfSupports):
     # Input Coordinates of Support
    SupportPositionInput = input(
        "Enter the coordinates of all the support positions(Single Spacing between the inputs) : "
    )
    SupportPositionCoordinates = SupportPositionInput.split(" ")
    # Converting data type from string to float in List
    for i in range(0, len(SupportPositionCoordinates)):
        SupportPositionCoordinates[i] = float(SupportPositionCoordinates[i])

NumberOfForces = int(input("Enter the number of forces acting on the beam : "))

# List Containing The coordinate and magnitude of acting forces respectively (2-D)
ForcesActing = []

for i in range(NumberOfForces):
    # input of coordinate and magnitude of force acting
    ForcesActingInput = input(
        "Enter the value of coordinate and force acting on the bar respectively (with a space in between each values) : "
    )
    # converting the string of input into list with 2 items - coordinate & magnitude of force
    ForcesActingInputList = ForcesActingInput.split(" ")
    # Updating the list ForcesActing with recent input
    ForcesActing.append(
        (float(ForcesActingInputList[0]), float(ForcesActingInputList[1]))
    )
        
# Initializing variable SumOfForces and calculating it
SumOfForces = 0.0
for i in range(0, len(ForcesActing)):
    SumOfForces = SumOfForces + ForcesActing[i][1]

# Initializing and calculating moment of forces from the origin
MomentOfForcesatA = 0.0
for i in range(0, len(ForcesActing)):
    MomentOfForcesatA = MomentOfForcesatA + ForcesActing[i][0] * ForcesActing[i][1]