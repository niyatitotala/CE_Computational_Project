
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
# importing numpy(not now but can be considered with expansion of project)
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

#Indeterminacy in the system
SystemIndeterminacy = 0.0

#Check for Global Stability
def StablitiyCheck(n1, n2, n3):
    if n2 == 0:
        print("System Unstable")
        sys.exit()
    elif n1+n2-n3 <2:
        print("System Unstable")
        sys.exit()
    elif n1+n2-n3 ==2: 
        SystemIndeterminacy = 0.0
    elif n1+n2-n3 >2: 
        SystemIndeterminacy = n1+n2-n3-2

StabilityCheck (NumberOfMomentSupports, NumberOfVerticalSupports, NumberOfInternalRelease)

# Input Coordinates of Support
SupportPositionInput = input(
    "Enter the coordinates of the support positions(Single Spacing between the inputs) : "
)

# Converting String of Coordinates into List
SupportPositionCoordinates = SupportPositionInput.split(" ")

# Converting data type from string to float in List
for i in range(0, len(SupportPositionCoordinates)):
    SupportPositionCoordinates[i] = float(SupportPositionCoordinates[i])
##################################-Force-Input-###################################
# No. of Forces Acting
NumberOfForces = int(
    input("Enter the number of forces acting on the beam : "))

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
###################################################################################
###################################-Moment-Input-##################################
# No. of Moments Acting
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

#ColumnToBeAdded = []

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

#NewCoefficient = 0.0
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
    #ReactionForces = []
    CoeffInverse = np.linalg.inv(Coeff)
    # print(CoeffInverse)
    Resultant = np.dot(CoeffInverse, EqConstant)

    print("resultant array", str(Resultant))


'''
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

