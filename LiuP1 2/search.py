# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util
#from util import Stack
#from util import Queue

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    #util.raiseNotDefined()
    """
   Search the deepest nodes in the search tree first.

   Your search algorithm needs to return a list of actions that reaches the
   goal. Make sure to implement a graph search algorithm.

   To get started, you might want to try some of these simple commands to
   understand the search problem that is being passed in:

   print("Start:", problem.getStartState())
   print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
   print("Start's successors:", problem.getSuccessors(problem.getStartState()))
   """
    startingNode = problem.getStartState()
    if problem.isGoalState(startingNode):
        return []

    stack = util.Stack()
    visitedNodes = []
    stack.push((startingNode,[]))

    while not stack.isEmpty():
        currentNode, actions = stack.pop()
        if currentNode not in visitedNodes:
            visitedNodes.append(currentNode)
            if problem.isGoalState(currentNode):
                return actions
            for nextNode, action, cost in problem.getSuccessors(currentNode):
                nextAction = actions + [action]
                stack.push((nextNode, nextAction))

def breadthFirstSearch(problem):


    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    node = problem.getStartState()
    #print(node['state'])
    if problem.isGoalState(node):
        return []
    frontier = util.Queue()
    frontier.push((node,[]))
    explored = []
    while True:
        if frontier.isEmpty():
            raise Exception("No solution found")
        node, actions = frontier.pop()
        if node not in explored:
            explored.append(node)
            if problem.isGoalState(node):
                return actions
            successors = problem.getSuccessors(node) #list
            for successor in successors:
            #print(successor[0])
                cState, action, cost = successor
                cActions = actions + [action]
                frontier.push((cState,cActions))

    #util.raiseNotDefined()

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    node = problem.getStartState()
    if problem.isGoalState(node):
        return []
    explored = []
    frontier = util.PriorityQueue()
    frontier.push((node, [], 0), 0)

    while not frontier.isEmpty():
        curr, actions, oldCost = frontier.pop()
        if curr not in explored:
            explored.append(curr)
            if problem.isGoalState(curr):
                return actions
            for next, action, cost in problem.getSuccessors(curr):
                nextAction = actions + [action]
                priority = oldCost + cost
                frontier.push((next, nextAction, priority), priority)

    #util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    """Search the node of least total cost first."""
    node = problem.getStartState()
    if problem.isGoalState(node):
        return []
    explored = []
    frontier = util.PriorityQueue()
    frontier.push((node, [], 0), 0)

    while not frontier.isEmpty():
        curr, actions, oldCost = frontier.pop()
        if curr not in explored:
            explored.append(curr)
            if problem.isGoalState(curr):
                return actions
            for next, action, cost in problem.getSuccessors(curr):
                nextAction = actions + [action]
                cost = oldCost + cost
                heuristicPriority =cost + heuristic(next,problem)
                frontier.push((next, nextAction, cost), heuristicPriority)
   # util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
