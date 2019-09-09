import random

# Consider making this a class Domain
arrayOfTest = []
arrayOfTraining = []

numOfCorrect = 0
totalCount = 0




class array: 
  def __init__(self, test=None):
    self.test = test
  
  @staticmethod
  def loadFile(fileName):
      lines = [line.rstrip('\n') for line in open(fileName)]
      for line in lines: 
        line = line.replace("left_", "0,")
        line = line.replace("right_", "1,")
        line = line.replace("central", "0.5,0.5")
        line = line.replace("low", "0")
        line = line.replace("up", "1")
        # split into training and testing
        if (random.random() < .67):
          arrayOfTraining.append(array.createNode(line))
        else :
          arrayOfTest.append(array.createNode(line))
      print('Training set: ', len(arrayOfTraining), '\n')  
      print('Testing Set: ', len(arrayOfTest), '\n')


#X - min / Max - min 

  @staticmethod
  def createNode(line):
      attributes = line.split(',')
      #print(attributes)
      classify =  0 if attributes[0] == "no-recurrence-events" else 1
      
      age = attributes[1].split('-')[0]
      age = (int(age) - 20) / 50
      #actual value [20-70]
      menopause = attributes[2]

      tumorSize = attributes[3].split('-')[0]
      #Range 0-40, actual 
      tumorSize = int(tumorSize) / 50
      
      invNodes = attributes[4].split('-')[0]
      #Range 0-36 NOT actual 
      invNodes = int(invNodes) / 24
      nodeCaps = 0 if attributes[5] == "no" else 1 
      degMalign = int(attributes[6]) / 3.0
      breast = 0 if attributes[7] == "left" else 1
      breastQuadX = attributes[8]
      breastQuadY = attributes[9]
      irradiat = 0 if attributes[10] == "no" else 1
      
      return Node(classify,age,menopause,tumorSize,invNodes,nodeCaps,degMalign,breast,breastQuadX,breastQuadY,irradiat)

  


class Node:   
    
    def __init__(self,classify, age, menopause, tumorSize,invNodes, nodeCaps, degMalig, breast, breastQuadX, breastQuadY,irradiat, guess=None, distance=None):
        self.classify = classify
        self.age = age
        self.menopause = menopause
        self.tumorSize = tumorSize
        self.invNodes = invNodes
        self.nodeCaps = nodeCaps
        self.degMalig = degMalig
        #Left = 0, Right = 1
        self.breast = breast
        self.breastQuadX = breastQuadX
        self.breastQuadY = breastQuadY
        self.irradiat = irradiat
        self.guess = guess

        print(classify,age,menopause,tumorSize,invNodes,nodeCaps,degMalig,breast,breastQuadX,breastQuadY,irradiat)
    
    @staticmethod
    def createNode(line):
        attributes = line.split(',')
       # print(attributes)
        classify =  False if attributes[0] == "no-recurrence-events" else True
        return Node(classify,2,3,4,5,6,7,8,9,1)
    
    @classmethod
    def findDistance(testNode):
        pass
    
    @staticmethod
    def sortDistances(arrayOfNodes):
        pass
    
    def getKNN(arrayOfNodes, k):
        pass
    
    def getErrorRate():
        pass

    @staticmethod
    def loadFile(fileName):
      lines = [line.rstrip('\n') for line in open(fileName)]
      for line in lines: 
        arrayofNodes.append(Node.createNode(line))

    def start(k): 
        """
        load file, create node, find distance, sort, vote, get error rate
        """
        pass
        
    
array.loadFile("yugoslavia.txt")
