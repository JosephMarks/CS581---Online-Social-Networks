# Author: Joseph Marks
# Processes a csv file with nodes or vertices listed and edge weight of positive or negative,
# and builds a graph. Program further calculates the number of triangles, edges used, trusts
# edges, distrust edges, the number of the different combinations of trianges, as well as then
# probability % p that an edge will be positive or negative. Finally, an Expected Distribution
# as well as the Actual Distribution is computed for each triangle type.

# To run from terminal window:   python3 Marks.py
# To run from Anaconda terminal window: python Marks.py
# Then follow prompt to enter file name and press enter. Make sure file is saved in same folder/path.
# Please note external packages have been used including networkx, and os.path
# Please ensure these external packages have been downloaded prior to running program
# Installing external packages can be accomplished by typing in terminal: pip install [package name]


# networkx package is used to build complex graphs - used for efficiency
import networkx as nx
# os.path package used to identify if file provided by user via input actually exists
import os.path
# Included to show run start end and duration times per assignment instructions
from datetime import datetime
start_time = datetime.now()
print("START TIME: {}".format(start_time))


### This section is all Functions I have defined - Program below calls my defined functions

# Function to read in the file data and returns a nodes list
def buildNodesList(fileName):
    # open the csv file in read only mode
    f = open(fileName, "r")
    # create a list from the csv file - this file will need to be further sanitized below
    initialNodesList = f.read().splitlines()
    # close file
    f.close()
    # initialize a new list - this will represent a clean version of each line from the csv file
    nodesList = []
    # iterate through initialNodesList - appending to a new cleaner list splitting on the commas from first list
    for i in initialNodesList:
        nodesList.append(i.split(','))
    return nodesList

# Function that builds a graph with nodesList as parameter
def buildGraph(nodesList):

    # Build a graph using networkx library
    nodesGraph = nx.Graph()
    # Iterate through each line of the node list adding the nodes, and edges with assigned weights
    for line in nodesList:
        nodesGraph.add_node(line[0])
        nodesGraph.add_node(line[1])
        nodesGraph.add_edge(line[0], line[1], weight=line[2])
    # return a node graph after processing entire list
    return nodesGraph

# Function that computes and returns number of trust edges
def calculateTrustEdges(nodesList):
    # Calculate the number of trust edges
    trustEdge_counter = 0


    for line in nodesList:
        if int(line[2]) == 1:
            trustEdge_counter = trustEdge_counter + 1
        else:
            continue

    return trustEdge_counter

# Calculate the number of trust edges
def calculateDistrustEdges(nodesList):

    distrustEdge_counter = 0

    for line in nodesList:
        if int(line[2]) == -1:
            distrustEdge_counter = distrustEdge_counter + 1
        else:
            continue
    return distrustEdge_counter

# Function to calculate the number of total edges
def calculateNumEdges(nodesGraph):
    numEdges = nodesGraph.number_of_edges()
    return numEdges
# Function to help identify if any edges are not part of a triangle
def calculateNumSelfLoops(nodesGraph):
    numSelfLoops = nx.nodes_with_selfloops(nodesGraph)
    return len(list(numSelfLoops))
# Function to calculate the positive probability (trust edges / total edges)
def calculatePosProb(trustEdge_counter, numEdges):
    positive_probability = (trustEdge_counter / numEdges)
    return positive_probability
# Function to calculate the negative probability (1 - positive probability)
def calculateNegProb(positive_probability):
    negative_probability = 1 - positive_probability
    return negative_probability
# Function to calculate the total number of triangles
def calculateNumTriangles(nodesGraph):
    numTriangles = sum(nx.triangles(nodesGraph).values())/3
    return numTriangles
# Function to calculate TTT Expected Ratio
def calculateTTTExpRatio(positive_probability):
    TTT_Exp_Ratio = (positive_probability ** 3)
    return TTT_Exp_Ratio
# Function to calculate TTT Expected Number
def calculateTTTExpNum(TTT_Exp_Ratio, numTriangles):
    TTT_Exp_Number = (TTT_Exp_Ratio * numTriangles)
    return TTT_Exp_Number
# Function to calculate TTD Expected Ratio
def calculateTTDExpRatio(positive_probability, negative_probability):
    TTD_Exp_Ratio = ((positive_probability ** 2) * negative_probability * 3)
    return TTD_Exp_Ratio
# Function to calculate TTD Expected Number
def calculateTTDExpNum(TTD_Exp_Ratio, numTriangles):
    TTD_Exp_Number = (TTD_Exp_Ratio * numTriangles)
    return TTD_Exp_Number
# Function to calculate TDD Expected Ratio
def calculateTDDExpRatio(positive_probability, negative_probability):
    TDD_Exp_Ratio = ((negative_probability ** 2) * positive_probability * 3)
    return TDD_Exp_Ratio
# Function to calculate TDD Expected Number
def calculateTDDExpNum(TDD_Exp_Ratio, numTriangles):
    TDD_Exp_Number = (TDD_Exp_Ratio * numTriangles)
    return TDD_Exp_Number
# Function to calculate DDD Expected Ratio
def calculateDDDExpRatio(negative_probability):
    DDD_Exp_Ratio = (negative_probability ** 3)
    return DDD_Exp_Ratio
# Function to calculate DDD Expected Number
def calculateDDDExpNum(DDD_Exp_Ratio, numTriangles):
    DDD_Exp_Number = (DDD_Exp_Ratio * numTriangles)
    return DDD_Exp_Number



# Ask the user to input file name for processing - checks if file is present in directory
while True:
    fileName = input("Please enter the name of the file to process.")
    if(os.path.isfile(fileName)):
        break
    else:
        print("Please enter a valid file. File entered does not exist in the directory.")
        continue


## Storing variables to be used in computations by calling my above defined functions
# Build a node list by calling the buildNodesList function
nodesList = buildNodesList(fileName)
# Build a nodes graph by calling the buildGraph function
nodesGraph = buildGraph(nodesList)
# Build a dictionary of attributes (weight of edges, ie, positive or negative) of my node graph
graphAttributes = nx.get_edge_attributes(nodesGraph, "weight")
# I need to use function to return a iterator for analyzing nodes
graphDataIterator = nx.enumerate_all_cliques(nodesGraph)

# Total Number of triangles stored in numTriangles by calling calculateNumTriangles function
numTriangles = calculateNumTriangles(nodesGraph)
# Total number of edges stored in numEdges by calling numEdges function
numEdges = calculateNumEdges(nodesGraph)

numSelfLoops = calculateNumSelfLoops(nodesGraph)
# Number of trust edges stored in numTristEdges variable by calling calculateTrustEdges function
numTrustEdges = calculateTrustEdges(nodesList)
# Positive probability stored in positiveProbability variable by calling calculatePosProb function
positiveProbability = calculatePosProb(numTrustEdges,numEdges)
# Number of distrust edges stored in numDistrustEdges variable by calling calculateDistrustEdges function
numDistrustEdges = calculateDistrustEdges(nodesList)
# Negative probability stored in negativeProbability variable by calling calculateNegProb function
negativeProbability = calculateNegProb(positiveProbability)
# Call calculateTTTExpRatio to compute and store TTT expected ratio
TTT_Exp_Ratio = calculateTTTExpRatio(positiveProbability)
# Call calculateTTTExpNum to compute and store TTT expected number
TTT_Exp_Number = calculateTTTExpNum(TTT_Exp_Ratio,numTriangles)
# Call calculateTTDExpRatio to compute and store TTD expected ratio
TTD_Exp_Ratio = calculateTTDExpRatio(positiveProbability, negativeProbability)
# Call calculateTTDExpNum to compute and store TTD expected number
TTD_Exp_Number = calculateTTDExpNum(TTD_Exp_Ratio,numTriangles)
# Call calculateTDDExpRatio to compute and store TDD expected ratio
TDD_Exp_Ratio = calculateTDDExpRatio(positiveProbability, negativeProbability)
# Call calculateTDDExpNum to compute and store TDD expected ratio
TDD_Exp_Number = calculateTDDExpNum(TDD_Exp_Ratio,numTriangles)
# Call calculateDDDExpRatio to compute and store DDD expected ratio
DDD_Exp_Ratio = calculateDDDExpRatio(negativeProbability)
# Call calculateDDDExpNum to compute and store DDD expected ratio
DDD_Exp_Number = calculateDDDExpNum(DDD_Exp_Ratio,numTriangles)

# Initialize a new list for triangles, and use graphDataIterator to identify these
trianglesList = []
for edges in graphDataIterator:
    if len(edges) == 3:
        trianglesList.append(edges)

#create some counters to track the different types of triangles
TTT_Act_Number = 0
TTD_Act_Number = 0
TDD_Act_Number = 0
DDD_Act_Number = 0

# Iterate through triangleList with for loop
for i in range(len(trianglesList)):
    # initialize new lists for the 3 edges
    edge1List = []
    edge2List = []
    edge3List = []
    # capture the 3 nodes in variables
    node1 = trianglesList[i][0]
    node2 = trianglesList[i][1]
    node3 = trianglesList[i][2]

    # append my 3 edgeLists for nodes captured above
    edge1List.append(node1)
    edge1List.append(node2)
    edge2List.append(node1)
    edge2List.append(node3)
    edge3List.append(node2)
    edge3List.append(node3)

    # Cast these lists to tuples (because the dictionary key is a tuple)
    edge1Tuple = tuple(edge1List)
    edge2Tuple = tuple(edge2List)
    edge3Tuple = tuple(edge3List)

    # Use these dictionary key tuples to obtain the weight of each edge of triangle from my attributes dictionary created previously
    edge1Weight = graphAttributes.get(edge1Tuple)
    edge2Weight = graphAttributes.get(edge2Tuple)
    edge3Weight = graphAttributes.get(edge3Tuple)

    # Cast these weights to integers and get the sum of the 3 edge weights
    mySum = int(edge1Weight) + int(edge2Weight) + int(edge3Weight)

    # Depending on the sum value determines the type of triangle. Appropriate counter iterated pursuant to the sum value
    if mySum == 3:
        TTT_Act_Number = TTT_Act_Number + 1
    elif mySum == 1:
        TTD_Act_Number = TTD_Act_Number + 1
    elif mySum == -1:
        TDD_Act_Number = TDD_Act_Number + 1
    elif mySum == -3:
        DDD_Act_Number = DDD_Act_Number + 1
    else:
        continue

# After above process, have total of each type of triangle, calculate actual ratios of each
TTT_Act_Ratio = (TTT_Act_Number / numTriangles)
TTD_Act_Ratio = (TTD_Act_Number / numTriangles)
TDD_Act_Ratio = (TDD_Act_Number / numTriangles)
DDD_Act_Ratio = (DDD_Act_Number / numTriangles)


#### NOW LETS PRINT EVERYTHING OUT TO THE CONSOLE AFTER ALL CALCULATIONS ARE COMPLETE

print("RESULTS FOR FILE: {}".format(fileName)) # File name provided by user via input
print("\n")
print("triangles: {}".format(int(numTriangles))) # Give user total number of triangles
# Provide total number of edges in graph - dont want to count a self loop though
print("TTT: {}\t\t Edges used: {}".format(TTT_Act_Number, (numEdges-numSelfLoops)))
# TTT actual number, Trust edges, probability of positive
print("TTD: {}\t\t Trust Edges: {}\t\t Probability % p that an edge will be positive : {:0.2f}".format(TTD_Act_Number, numTrustEdges,positiveProbability*100))
# Total TDD Triangles, Distrust edges, and probability edge is negative
print("TDD: {}\t\t Distrust Edges: {}\t\t Probability % that an edge will be negative: {:0.2f}".format(TDD_Act_Number, numDistrustEdges,negativeProbability*100))
# Total DDD triangles and number of edges
print("DDD: {}\t\t Total: {}".format(DDD_Act_Number,numEdges))
print("\n")


###this is the main table printed EXPECTED and ACTUAL - Using formatting to make a more legible user friendly table
print("------------------------------------------------------------")
print(f"{'EXPECTED DISTRIBUTION' : <30}{'ACTUAL DISTRIBUTION' : ^30}")
print("------------------------------------------------------------")
print(f"{'Type' : <}{'Percent' : ^11}{'Number' : <11}{'  ' : ^10}{'Type' : <}{'Percent' : ^11}{'Number' : ^11}")
print("------------------------------------------------------------")
print(f"{'TTT' : <}{round(TTT_Exp_Ratio*100,2) : ^11}{round(TTT_Exp_Number,2) : ^11}{'  ' : ^11}{'TTT' : <}{round(TTT_Act_Ratio*100,2) : ^11}{TTT_Act_Number : ^10}")
print(f"{'TTD' : <}{round(TTD_Exp_Ratio*100,2) : ^11}{round(TTD_Exp_Number,2) : ^11}{'  ' : ^11}{'TTD' : <}{round(TTD_Act_Ratio*100,2) : ^11}{TTD_Act_Number : ^10}")
print(f"{'TDD' : <}{round(TDD_Exp_Ratio*100,2) : ^11}{round(TDD_Exp_Number,2) : ^11}{'  ' : ^11}{'TDD' : <}{round(TDD_Act_Ratio*100,2) : ^11}{TDD_Act_Number : ^10}")
print(f"{'DDD' : <}{round(DDD_Exp_Ratio*100,2) : ^11}{round(DDD_Exp_Number,2) : ^11}{'  ' : ^11}{'DDD' : <}{round(DDD_Act_Ratio*100,2) : ^11}{DDD_Act_Number : ^10}")
print("------------------------------------------------------------")
print(f"{'Total' : <}{round((TTT_Exp_Ratio+TTD_Exp_Ratio+TDD_Exp_Ratio+DDD_Exp_Ratio)*100,2) : ^11}{round(TTT_Exp_Number+TTD_Exp_Number+TDD_Exp_Number+DDD_Exp_Number,2) : ^10}{'  ' : ^10}{'Total' : <}{round((TTT_Act_Ratio+TTD_Act_Ratio+TDD_Act_Ratio+DDD_Act_Ratio)*100,2) : ^11}{TTT_Act_Number+TTD_Act_Number+TDD_Act_Number+DDD_Act_Number : ^10}")
print("------------------------------------------------------------")

# Included to show run start end and duration times per assignment instructions
end_time = datetime.now()

print("END TIME: {}".format(end_time))
print("DURATION: {}".format(end_time - start_time))
