
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

    Using the equation : [Coeff][Resultant] = [EqConstant]
    [Resultant] = [CoeffInverse]*[EqConstant]
"""

import numpy as np
import sys

# Initial instructions & guidelines
print(
    "NOTE : The origin of the axis is taken at the left end of the beam and all the distances are measured from the origin. \n For the load acting on the beam, downwards direction is considered positive."
)

# Input length of beam
LengthOfBeam = int(input("Enter the length of the beam : "))

# Input number of supports
NumberOfSupports = int(input("Enter the number of supports:"))
NumberOfMomentSupports = int(input("Enter the number of moment supports:"))
NumberOfVerticalSupports = int(input("Enter the number of Vertical supports:"))
NumberOfInternalRelease = int(input("Enter the number of internal release:"))

# Indeterminacy in the system
SystemIndeterminacy = 0.0

# Check for Global Stability


def StabilityCheck(n1, n2, n3):
    if n2 == 0:
        print("System Unstable")
        sys.exit()
    elif n1+n2-n3 < 2:
        print("System Unstable")
        sys.exit()
    elif n1+n2-n3 == 2:
        SystemIndeterminacy = 0.0
    elif n1+n2-n3 > 2:
        SystemIndeterminacy = n1+n2-n3-2


StabilityCheck(NumberOfMomentSupports, NumberOfVerticalSupports,
               NumberOfInternalRelease)

# The support S matrix
SupportMatrix = []

for i in range(NumberOfSupports):
    SupportPositionInput = input(
        "Enter the value of support type and the coordinate at which the support is acting on the bar respectively (with a space in between each values)( 1- moment, 2- Force, 3- Internal Release : "
    )
    # converting the string of input into list with 2 items - type & coordinate of support
    SupportPositionInputList = SupportPositionInput.split(" ")
    # Updating the list SupportMatrix with recent input
    SupportMatrix.append(
        (float(SupportPositionInputList[0]),
         float(SupportPositionInputList[1]))
    )

# Converting to Numpy Array
SupportMatrix = np.array(SupportMatrix)

##################################-Force-Input-###################################
# No. of Forces Acting
NumberOfForces = int(input("Enter the number of forces acting on the beam : "))

ForcesActing = []
for i in range(NumberOfForces):
    # input of coordinate and magnitude of force acting
    ForcesActingInput = input(
        "Enter the value of coordinate and magnitude acting on the bar respectively (with a space in between each values) : ")
    # converting the string of input into list with 2 items - coordinate & magnitude of force
    ForcesActingInputList = ForcesActingInput.split(" ")
    # Updating the list ForcesActing with recent input
    ForcesActing.append(
        (float(ForcesActingInputList[0]), float(ForcesActingInputList[1])))

NumberOfMoments = int(
    input("Enter the number of Moments acting on the beam : "))

# List Containing The coordinate and magnitude of acting moments respectively (2-D)
MomentsActing = []

for i in range(NumberOfMoments):
    # input of coordinate and magnitude of force acting
    MomentsActingInput = input(
        "Enter the value of coordinate and moment acting on the bar respectively (with a space in between each values) : "
    )
    # converting the string of input into list with 2 items - coordinate & magnitude of force
    MomentsActingInputList = MomentsActingInput.split(" ")
    # Updating the list Moments Acting with recent input
    MomentsActing.append(
        (float(MomentsActingInputList[0]), float(MomentsActingInputList[1]))
    )
###############################################################################
# Initializing variable SumOfForces and calculating it
SumOfForces = 0.0
for i in range(0, len(ForcesActing)):
    SumOfForces = SumOfForces + ForcesActing[i][1]

# Initializing and calculating moment of forces from the origin
MomentOfForces = 0.0
for i in range(0, len(ForcesActing)):
    MomentOfForces = MomentOfForces + \
        ForcesActing[i][0] * ForcesActing[i][1]

# Initializing variable SumOfMoments and calculating it
SumOfMoments = 0.0
for i in range(0, len(ForcesActing)):
    SumOfMoments = SumOfMoments + MomentssActing[i][1]

SumOfMoments = MomentOfForces + SumOfMoments

z = np.zeros((NumberOfSupports, 1), int)
SupportMatrix = np.append(SupportMatrix, z, axis=1)

# S13 = (-F*S22^(S21-1)+M*(S21-1)) / ((S11-1)*S22^(S21-1)-(S21-1)*S12^(S11-1))
SupportMatrix[0][2] = (-SumOfForces*SupportMatrix[1][1]**(SupportMatrix[1][0]-1) + SumOfMoments*(
    SupportMatrix[1][0]-1)) / ((SupportMatrix[0][0]-1)*SupportMatrix[1][1]**(SupportMatrix[0][0]-1) - (SupportMatrix[1][0]-1)*SupportMatrix[0][1]**(SupportMatrix[0][0]-1))

# S23 = (-F*S12^(S11-1)+M*(S11-1)) / ((S21-1)*S12^(S11-1)-(S11-1)*S22^(S21-1))
SupportMatrix[1][2] = (-SumOfForces*SupportMatrix[0][1]**(SupportMatrix[0][0]-1) + SumOfMoments*(
    SupportMatrix[0][0]-1)) / ((SupportMatrix[1][0]-1)*SupportMatrix[0][1]**(SupportMatrix[0][0]-1) - (SupportMatrix[0][0]-1)*SupportMatrix[1][1]**(SupportMatrix[1][0]-1))

for i in range(SystemIndeterminacy):


'''
for i in range(NumberOfLoads):
    # input of coordinate and magnitude of force acting
    LoadsActingInput = input(
        "Enter the type of external load (1 for moment, 2 for force), the value of coordinate and magnitude acting on the bar respectively (with a space in between each values) : "
    )
    # converting the string of input into list with 3 items - type, coordinate & magnitude of load
    LoadsActingInputList = LoadsActingInput.split(" ")
    # Updating the list LoadsActing with recent input
    LoadsActing.append(
        (int(LoadsActingInputList[0]), float(
            LoadsActingInputList[1]), float(LoadsActingInputList[2]))
    )

###############################################################################
# Initializing variable SumOfForces and calculating it
SumOfForces = 0.0
for i in range(0, len(LoadsActing)):
    SumOfForces = SumOfForces + (LoadsActing[i][0]-1)*(LoadsActing[i][2])
SumOfForces = SumOfForces*(-1)

# Initializing variable SumOfMoments and calculating it
SumOfMoments = 0.0
for i in range(0, len(LoadsActing)):
    SumOfMoments = SumOfMoments + \
        ((LoadsActing[i][2])*((LoadsActing[i][1])**(LoadsActing[i][0]-1)))
SumOfMoments = SumOfMoments*(-1)
'''
