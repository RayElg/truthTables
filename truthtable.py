def twoVals(x,y,op): #Returns boolean value of (x op y)
    #x,y are booleans
    #op is a string
    if op == "AND":
        return x and y
    if op == "OR":
        return x or y
    if op == "NAND":
        return not (x and y)
    if op == "NOR":
        return not (x or y)
    if op == "XOR":
        return (x and not y) or (not x and y)
    if op == "XNOR":
        return not((x and not y) or (not x and y))

def notTable(L): #Returns the inverse of a list
    N = [] #Notted list
    for i in L: #Go through list
        N.append(not i) #Append the inverse of the element
    return N

def twoTables(X,Y,op): #Returns list of boolean vals of (X op Y):
    #X,Y are lists of booleans, equal length
    #op is a string
    L = [] #Where we'll store the list of T,F
    for i in range(len(X)): #Use twoVals over lists
        L.append(twoVals(X[i],Y[i],op))
    return L

def genVals(length,spot): #Generates T,F list for initial variables, with intention of having all combinations of T,F
    #Spot 0 (first) will switch from placing T/F every 2^0 over length
    #Spot one (second) will switch from placing T/F every 2^1 over length
    #length will be 2^n, where n is number of variables
    L = [] #Where we'll store the list of T,F
    toPlace = True #What we'll add to the list
    for i in range(length): #The length the list needs to be
        if(i % pow(2,spot)) == 0: #Change what we're placing, based off of how often we should switch(from place)
            toPlace = not toPlace
        L.append(toPlace)
    return L

def simpleExpression(L): #Evaluate an expression consisting of a list made only of operators and lists of T/F
    #Eg of L:
    #[[T,F],"AND",[F,F],"OR",[T,T]]

    #Base cases:
    #One operator:
    if len(L) == 3: #L of length 3 indicates there is one operator and 2 lists
        return twoTables(L[0],L[2],L[1])
    #No operator:
    if len(L) == 1:
        return L[0]

    #Non base cases...
    adjustedList = L.copy() #List we make a change to and recurse on...
    
    #First, deal with any NOTs
    for i in range(len(L)):
        if L[i] == "NOT":
            adjustedList[i + 1] = notTable(L[i+1]) #NOT the list after the NOT operator
            adjustedList.pop(i) #Remove NOT operator
            return simpleExpression(adjustedList) #Recurse

    #After we've gotten rid of all NOTs...
    #Precedence of operators:
    #NOT, XNOR, XOR, NAND, AND, NOR, OR
    opsOrder = ("XNOR","XOR","NAND","AND","NOR","OR")

    for operation in opsOrder:
        for i in range(len(L)):
            if L[i] == operation: #Look for operators, starting with the beginning of list and with the first in the order
                adjustedList[i] = twoTables(L[i-1],L[i+1],L[i]) #Replace operator with new lists in adjustedList
                adjustedList.pop(i + 1) #Remove surrounding operands from adjustedList
                adjustedList.pop(i - 1)
                return simpleExpression(adjustedList) #Recurse

    
def expression(L): #Evaluate an expression that may contain parantheses

    #Base case: No parantheses:
    if "(" not in L:
        return simpleExpression(L) #No parantheses found, so we run simple expression

    #Non base cases...
    leftParenIndex = -1 #Index of the right-most left bracket
    rightParenIndex = -1
    #Search right to left for open parantheses...
    for i in range(len(L)-1,0,-1):
        if L[i] == "(":
            leftParenIndex = i
            break

    if leftParenIndex > -1: #If we found a left bracket
        #Now, starting at where the left bracket is, look for it's corresponding right bracket
        for i in range(leftParenIndex,len(L)):
            if L[i] == ")":
                rightParenIndex = i
                break

    
    if rightParenIndex > -1: #If we've found both left and right brackets
        #Replace left bracket's spot with value of expression inside the brackets...
        L[leftParenIndex] = simpleExpression(L[leftParenIndex + 1:rightParenIndex])

        #Remove what was previously inside the brackets, plus the right bracket
        for i in range(rightParenIndex,leftParenIndex,-1):
            L.pop(i)
        
        return expression(L)

import string

def printTable(L,title): #Print's list of T/F lists & their names (e.g A,B), uses title in header
    print(title)
    lineStr = "|"
    for i in L: #Go through each name,list pair
        lineStr = lineStr + i[0] + "|" #Append their labels and dividers to string to be printed
    print(lineStr) #Print the line
    for j in range(len(L[0][1])): #Iterate throught the T/F through list
        lineStr = "|"
        for i in L:
            if i[1][j] == True:
                lineStr = lineStr + "T|"
            else:
                lineStr = lineStr + "F|"
        print(lineStr)

        
A = genVals(8,2)
B = genVals(8,1)
C = genVals(8,0)
D = expression([A,"AND","NOT","(",B,"OR",C,")"])

varList = [
["A",A],
["B",B],
["C",C],
["=",D]
]


printTable(varList,"A AND NOT (B OR C)")
            

