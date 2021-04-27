
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
NumberOfLoads = int(
    input("Enter the number of loads acting on the beam : "))

# List Containing The type, coordinate and magnitude of acting Loads respectively (2-D)
LoadsActing = []

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

print(SumOfForces)
print(SumOfMoments)
'''
############################################################################
# [Coeff]


#    c1 = 0.0
#    c2 = 0.0
#    d1 = 0.0
#    d2 = 0.0

# If the unknowns are forces :
c1 = 1
#   c2 = 1

d1 = SupportPositionCoordinates[0]
#   d2 = SupportPositionCoordinates[1]

# ColumnToBeAdded = []

# Step 1
Coeff = np.array([[c1], [d1]])

# Step 2
for i in range(0, NumberOfSupports):
    NewCoefficient = SupportPositionCoordinates[i]**3
    Coeff = np.append(Coeff, [[NewCoefficient]], axis=0)
    i = i+1

# Step 3
for j in range(1, NumberOfSupports):
    ColumnToBeAdded = np.array([[c1], [SupportPositionCoordinates[j]]])
    for i in range(0, NumberOfSupports):
        if j < i:
            NewCoefficient = (
                SupportPositionCoordinates[i]-SupportPositionCoordinates[j])**3
            ColumnToBeAdded = np.append(
                ColumnToBeAdded, [[NewCoefficient]], axis=0)

        elif j >= i:
            NewCoefficient = 0
            ColumnToBeAdded = np.append(
                ColumnToBeAdded, [[NewCoefficient]], axis=0)

    i = i+1
    Coeff = np.append(Coeff, ColumnToBeAdded, axis=1)

# Step 4
ColumnToBeAdded = np.array([[0], [0]])
for i in range(0, NumberOfSupports):
    NewCoefficient = SupportPositionCoordinates[i]
    ColumnToBeAdded = np.append(
        ColumnToBeAdded, [[NewCoefficient]], axis=0)
    i = i + 1
Coeff = np.append(Coeff, ColumnToBeAdded, axis=1)

# Step 5
ColumnToBeAdded = np.array([[0], [0]])
for i in range(0, NumberOfSupports):
    NewCoefficient = 1
    ColumnToBeAdded = np.append(
        ColumnToBeAdded, [[NewCoefficient]], axis=0)
    i = i + 1
Coeff = np.append(Coeff, ColumnToBeAdded, axis=1)

print(Coeff)

###############################################################################
# [EqConstant]
EqConstant = np.array([[SumOfForces], [MomentOfForces]])

# NewCoefficient = 0.0
# print(EqConstant)
# print(ForcesActing[0][0])
# print(ForcesActing[1][0])
# print(ForcesActing[2][0])
# print(ForcesActing[3][0])
for i in range(0, NumberOfSupports):
    NewCoefficient = 0
    var2 = 0
    if SupportPositionCoordinates[i] > ForcesActing[var2][0]:
        while SupportPositionCoordinates[i] > ForcesActing[var2][0]:
            InstantaneousForceSum = ForcesActing[var2][1]*(
                (SupportPositionCoordinates[i] - ForcesActing[var2][0])**3)
            NewCoefficient = NewCoefficient + InstantaneousForceSum
            var2 = var2 + 1
            if (var2 >= len(ForcesActing)):
                break

    else:
        NewCoefficient = 0

    EqConstant = np.append(EqConstant, [[NewCoefficient]],  axis=0)

print(EqConstant)

    ##########################################################################################

    # Initializing list of the Reaction Forces
    # ReactionForces = []
    CoeffInverse = np.linalg.inv(Coeff)
    # print(CoeffInverse)
    Resultant = np.dot(CoeffInverse, EqConstant)

    print("resultant array", str(Resultant))


    # Calculating Reaction Force for support 1
    ReactionForce1 = (MomentOfForces - SupportPositionCoordinates[1] * SumOfForces) / (
        SupportPositionCoordinates[0] - SupportPositionCoordinates[1]
    )
    # Initializing list of the Reaction Forces
    ReactionForces = []
    # Updating the Reaction Forces list with both the reaction forces
    ReactionForces.append(ReactionForce1)
    ReactionForces.append((SumOfForces - ReactionForce1))
    # Test Run
    
else:
    print("Error")
    
    
    *********************************************
    -Ask for number of moment supports (n1)
    -Ask for number of vertical supports (n2)
    -Ask for internal release (n3)
    
    -If n2 = 0 -> say unstable
    -If n1+n2-n3 <2 -> say unstable
    
    (check for local indeterminacy in next part)
 
    -If n1+n2-n3 =2 -> solution case determinate
    -If n1+n2-n3 >2 -> solution case indeterminate
     -   indeterminacy = IN = n1+n2-n3-2
    
    Create matrix, S = [3,(n1+n2)]
    For i=1:n1, input location of moment support
            S(i)=(1,input,0)
    For i=n1:(n1+n2), input location of vertical support
            S(i)=(2,input,0)
            Note: sort by input to sort supports by distance
    
            (segment for internal release in next part)

note -  
support input is taken directly and not sorted. Sorting needs to be done according to the future needs.
'''
