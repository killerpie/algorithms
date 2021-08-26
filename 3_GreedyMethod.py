'''
based on conditions, understand the constraints, to identify feasible solutions
understand the goal, to identify only one optimal solution

if either minimum or maximum reserve, there will be two optimal solutions, we call it optimization problem and it is what Greedy Method is to solve for
Tow other methods for solving optimiation problems are Dynamic Programming and Branch and Bound. 
'''

#Greedy Method.   look one by one, if a solution is feasible, include it in the next one and eventually find out the optimal solution  

'''
3.1  knapsack problem - a container
n = number of objects
w = weight capacity
'''

# Fractional Knapsack Greedy Method
class KnapsackPackage(object):
  """ Knapsack package data class """
  def __init__(self, weight, value):
    self.weight = weight
    self.value = value
    self.pervalue = round(value/weight,3)

  def __lt__(self, other):
    #less than operator(<). Return True or False. when sorted, it sorts by pervalue
    return self.pervalue < other.pervalue

def knapsackGreedy(W, V, M, n):
    packs = []
    print ("{:<8} {:<8} {:<8}".format("value", "weight", "pervalue"))
    for i in range(n):
      packs.append(KnapsackPackage(W[i], V[i]))
      #print("Value", packs[i].value,"Weight", packs[i].weight,"per Value", packs[i].pervalue)
      print ("{:<8} {:<8} {:<8}".format(packs[i].value, packs[i].weight, packs[i].pervalue))
      
    packs.sort(reverse = True) #Sort by pervalue?


    
    remain = M
    result = 0
    
    i = 0
    stopProc = False
    
    while(stopProc != True):
        while (packs[i].weight >= 1 and remain != 0):
            remain -= 1
            result += packs[i].pervalue
            packs[i].weight -= 1
            print("Pack ", i, " - Weight ", packs[i].weight, " - Value ", packs[i].value, " - perValue ", packs[i].pervalue)
        i += 1

        if (i == n):
            stopProc = True

    print("Max Value:\t", result)



'''
W = [15, 10, 2, 4]
V = [30, 25, 2, 6]
M = 37
n = 4
'''

W = [2, 3, 5, 7, 1, 4, 1]
V = [10, 5, 15, 7, 6, 18, 3]
M = 15
n = 7


knapsackGreedy(W, V, M, n)




      

  

