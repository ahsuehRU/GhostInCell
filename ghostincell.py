import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
class graph:
    def __init__(self):
        self.nodes = []
        self.edges  = {}
    
    def add_node(self, node_id):
        self.nodes.append(node_id)
    
    def add_edge(self, node1, node2, distance):
        if node1 in self.edges:
            self.edges[node1][node2] = distance
        else:
            self.edges[node1] = {node2: distance}
        
        if node2 in self.edges:
            self.edges[node2][node1] = distance
        else:
            self.edges[node2] = {node1: distance}
            
    def __repr__(self):
        return "graph()"
    def __str__(self):
        return "Edges:{} ".format(self.edges)        

class Node:

    def __init__(self, factoryID):
        self.ID = factoryID
        self.team = 0
        self.production = 0
        self.cyborgs = 0
    def __repr__(self):
        return "Node()"
    def __str__(self):
        return "ID:{} Team: {} Prod: {} Count: {}".format(self.ID, self.team, self.production, self.cyborgs)
    
    #def add_neighbor(self, neighbor, distance):
    #    self.adj_neighbors.append(neighbor)
    #    self.dist.append(distance)
    def updateStats(self, team, cyborgs, production):
        self.team = team
        self.production = production
        self.cyborgs = cyborgs

class gameState:
    
    def __init__(self, factory_count):
        self.factory = {i: [] for i in range(factory_count)}
        self.troops = {}
        self.bombs = {}
                
    def updateFactory(self, factory_id, argsArr):       
        self.factory[factory_id] = argsArr
    def updateBomb(self, team, origin, target, remaining_turns):
        return None
    def updateTroops(self, team, origin, target, cyborgs, remaining_turns):
        return None
    def target(gameMap):
        neutral = []
        enemy = []
        maxProd = -1
        targetId = -1
        for i,x in enumerate(gameMap):
            if gameMap[i].team == 0:
                neutral.append(i)
            elif gameMap[i].team == -1:
                enemy.append(i)
    
        if neutral:
            for j in neutral:
                if gameMap[j].production > maxProd:
                    maxProd = gameMap[j].production
                    targetId = j
            return targetId, gameMap[targetId].cyborgs        
        elif enemy:
            return enemy[0], gameMap[enemy[0]].cyborgs
        else:
            return None, None
            
    def attackInProgress(nodeId, team, troopDict):
        if nodeId not in troopDict:
            return False
        else:
            tempArr = troopDict[nodeId]
            for i in tempArr:
                if i[0] == team:
                    return True
            return False
    
    def sendBomb():
        return False




    
factory_count = int(input())  # the number of factories
link_count = int(input())  # the number of links between factories      

gameGraph = graph()

for i in range(factory_count):
    gameGraph.add_node(i)

for i in range(link_count):
    factory_1, factory_2, distance = [int(j) for j in input().split()] 
    gameGraph.add_edge(factory_1, factory_2, distance)

print(gameGraph, file=sys.stderr)





# game loop
game_stats = gameState(factory_count)
while True:
    troopDict = {}
    myBases = []
    cyborgCount = 0
    homeBase = -1
    outputStr = "WAIT"

    
    
    entity_count = int(input())  # the number of entities (e.g. factories and troops)
    for i in range(entity_count):
        entity_id, entity_type, arg_1, arg_2, arg_3, arg_4, arg_5 = input().split()
        entity_id = int(entity_id)
        arg_1 = int(arg_1)
        arg_2 = int(arg_2)
        arg_3 = int(arg_3)
        arg_4 = int(arg_4)
        arg_5 = int(arg_5)
        if entity_type == "FACTORY":
            game_stats.updateFactory(entity_id, [arg_1, arg_2, arg_3])
        elif entity_type == "BOMB":
            game_stats.updateBomb(arg_1, arg_2, arg_3, arg_4)
            ##arg1 = Team, arg2 = cyborgs, arg 3 = Production
            #gameGraph.nodes[entity_id].updateStats(arg_1, arg_2, arg_3)
            #if arg_1 == 1:
            #    myBases.append(entity_id)
            #    if arg_2 > cyborgCount:
            #        cyborgCount = arg_2
            #        homeBase = entity_id
                    
            #elif arg_1 == -1 and entity_id in myBases:
            #    myBases.remove(entity_id)
        else:
            game_stats.updateTroops(arg_1, arg_2, arg_3, arg_4, arg_5)
            #if arg_3 in troopDict:
            #    troopDict[arg_3].append([arg_1, arg_2, arg_4, arg_5])
            #else:
            #    troopDict[arg_3] = [[arg_1, arg_2, arg_4, arg_5]]
    
    
    #print(myBases, homeBase, file=sys.stderr)
    #print(gameMap[j], file=sys.stderr)
    #tempTarget, tempCyborgCount = target(gameGraph)
    
    #if tempTarget is not None:
    #    if gameMap[homeBase].cyborgs > tempCyborgCount and not attackInProgress(tempTarget, 1, troopDict):
    #        print("MOVE", homeBase, tempTarget, tempCyborgCount+1)
    #    else:
    #        print("WAIT")
    #else:
    #    print("WAIT")
    #print(tempTarget, tempCyborgCount, file=sys.stderr)

            
    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr)


    # Any valid action, such as "WAIT" or "MOVE source destination cyborgs"
    print("MOVE 1 5 24")
