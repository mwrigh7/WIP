#this function takes in numerical input and stores it in a series of lists
def generateMatrix():
    i=0
    j=0
    n = input("What is the matrices' X dimension?"+ "\n")
    m = input("What is the matrices' Y dimension?"+ "\n")   
    matrixRow = []
    row = []
    while j < m:
        print "Row", j+1
        while len(matrixRow) != n:       
            value = input("Enter a value for the matrix" + "\n")
            matrixRow.append(value)
        #print matrixRow, len(matrixRow), n  
        row.append(matrixRow)
        matrixRow = []
        j+= 1
    return row

#this function prints the passed matrix
def printMatrix(M):
    print "Matrix ="
    for a in range(len(M)):
            print M[a]

#this function performs Matrix Row Addition when given two rows 
#and adds the first row to the second
def addRow(M,a,b):
    rowA = M[a]
    rowB = M[b]
    newB = []
    for i in range(len(rowA)):
            newB.append(rowA[i]+rowB[i])
    M[b] = newB
    return M

#multiplies the first row by a number and then adds to the second row
def scalarAdd(M,a,b,C):
    rowA = M[a]
    rowB = M[b]
    newB = []
    for i in range(len(rowA)):
            newB.append((C*rowA[i])+rowB[i])
    M[b] = newB
    return M    

#this swaps two rows
def rowSwap(M,a,b):
    rowA = M[a]
    rowB = M[b]  
    temp = rowA
    rowA = rowB
    rowB = temp
    M[a] = rowA
    M[b] = rowB
    return M
    
#shows the menu    
def displayMenu():
    print "Menu Options:"
    print "\t", "0) Generate Matrix"
    print "\t", "1) Show Matrix"
    print "\t", "2) Row Addition"
    print "\t", "3) Scalar Addition"
    print "\t", "4) Row Swap", "\n"
    print "\t", "-1) Exit", "\n"
    option = input("What would you like to do? Enter the associated number:" + "\n")
    return option
    
#::Main Code::
x= 0
while x != -1:
    x = displayMenu()
    if x == 0: 
        print "::Generate Matrix::"
        M = generateMatrix()
        print "\n"
    elif x ==1:
        print "::Show Matrix::"
        printMatrix(M)
        print "\n"
    elif x == 2:
        print "::Row Addition::"
        a,b = input("Select two rows to add. Enter as: x,y" + "\n")
        M= addRow(M,a-1,b-1)
        print "\n"
    elif x == 3:
        print "::Scalar Addition::"
        a,b = input("Select two rows to add. Enter as: x,y" + "\n")
        C = input("Multiply the first row by what number?" + "\n")
        M= scalarAdd(M,a-1,b-1,C)
        print "\n"
    elif x == 4:
        print "::Row Swap::"
        a,b = input("Select two rows to swap. Enter as: x,y" + "\n")
        M= rowSwap(M,a-1,b-1)
        print "\n"    
    elif x == -1:
        print "\n", "Final Matrix"
        printMatrix(M)
        print "\n", "Thanks, hope you had fun!"
        break
    x = 0
    
    
    #add in an "Undo" feature? maybe?