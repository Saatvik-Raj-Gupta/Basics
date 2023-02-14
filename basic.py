graph = {
  '(0,0)' : ['(5,0)','(0,3)'],
  '(5,0)' : ['(2,3)', '(5,3)'],
  '(0,3)' : ['(3,0)'],
  '(2,3)' : ['(2,0)'],
  '(5,3)' : [' '],
  '(3,0)' : ['(3,3)'],
  '(2,0)' : ['(0,2)'],
  '(3,3)' : ['(5,1)'],
  '(0,2)' : ['(5,2)'],
  '(5,1)' : ['(0,1)'],
  '(5,2)' : ['(4,3)'],
  '(0,1)' : ['(1,0)'],
  '(4,3)' : ['(4,0)'],
  '(1,0)' : ['(1,3)'],
  '(1,3)' : ['(4,0)']
}

visited = [] 
queue = []     

def bfs(visited, graph, node): 
  visited.append(node)
  queue.append(node)

  while queue:          
    m = queue.pop(0) 
    print (m, end = "\t")
    for n in graph[m]:
      if n == ' ':
        pass
      elif n == '(4,0)':
        print(n, end = '\t')
      elif n not in visited:
        visited.append(n)
        queue.append(n)

print("BFS")
bfs(visited, graph, '(0,0)')


graph = {
  '(0,0)' : ['(5,0)','(0,3)'],
  '(5,0)' : ['(2,3)', '(5,3)'],
  '(0,3)' : ['(3,0)'],
  '(2,3)' : ['(2,0)'],
  '(5,3)' : [' '],
  '(3,0)' : ['(3,3)'],
  '(2,0)' : ['(0,2)'],
  '(3,3)' : ['(5,1)'],
  '(0,2)' : ['(5,2)'],
  '(5,1)' : ['(0,1)'],
  '(5,2)' : ['(4,3)'],
  '(0,1)' : ['(1,0)'],
  '(4,3)' : ['(4,0)'],
  '(1,0)' : ['(1,3)'],
  '(1,3)' : ['(4,0)']
}
visited = set() 

def dfs(visited, graph, node):  
    if node not in visited:
        print (node)
        visited.add(node)
        for n in graph[node]:
          if n == ' ':
            pass
          elif n == '(4,0)':
            print(n)
          else:
            dfs(visited, graph, n)

print("DFS")
dfs(visited, graph, '(0,0)')

from simpleai.search import SearchProblem, astar

GOAL = 'SAATVIK'


class HelloProblem(SearchProblem):
    def actions(self, state):
        if len(state) < len(GOAL):
            return list(' ABCDEFGHIJKLMNOPQRSTUVWXYZ')
        else:
            return []

    def result(self, state, action):
        return state + action

    def is_goal(self, state):
        return state == GOAL

    def heuristic(self, state):
        wrong = sum([1 if state[i] != GOAL[i] else 0
                    for i in range(len(state))])
        missing = len(GOAL) - len(state)
        return wrong + missing

problem = HelloProblem(initial_state='')
result = astar(problem)

print(result.state)
print(result.path())

from simpleai.search import astar, SearchProblem
class PuzzleSolver(SearchProblem):
    def actions(self, cur_state):
        rows = string_to_list(cur_state)
        row_empty, col_empty = get_location(rows, 'e')
        actions = []
        if row_empty > 0:
            actions.append(rows[row_empty - 1][col_empty])
        if row_empty < 2:
            actions.append(rows[row_empty + 1][col_empty])
        if col_empty > 0:
            actions.append(rows[row_empty][col_empty - 1])
        if col_empty < 2:
            actions.append(rows[row_empty][col_empty + 1])
        return actions
    def result(self, state, action):
        rows = string_to_list(state)
        row_empty, col_empty = get_location(rows, 'e')
        row_new, col_new = get_location(rows, action)
        rows[row_empty][col_empty], rows[row_new][col_new] = \
        rows[row_new][col_new], rows[row_empty][col_empty]
        return list_to_string(rows)
    def is_goal(self, state):
        return state == GOAL
    def heuristic(self, state):
        rows = string_to_list(state)
        distance = 0
        for number in '12345678e':
            row_new, col_new = get_location(rows, number)
            row_new_goal, col_new_goal = goal_positions[number]
            distance += abs(row_new - row_new_goal) + abs(col_new - col_new_goal)
        return distance
def list_to_string(input_list):
        return '\n'.join(['-'.join(x) for x in input_list])
def string_to_list(input_string):
        return [x.split('-') for x in input_string.split('\n')]
def get_location(rows, input_element):
        for i, row in enumerate(rows):
            for j, item in enumerate(row):
                if item == input_element:
                    return i, j
GOAL = '''1-2-3
4-5-6
7-8-e'''
INITIAL = '''1-e-2
6-3-4
7-5-8'''
goal_positions = {}
rows_goal = string_to_list(GOAL)
for number in '12345678e':
    goal_positions[number] = get_location(rows_goal, number)
result = astar(PuzzleSolver(INITIAL))
for i, (action, state) in enumerate(result.path()):
    print()
    if action == None:
        print('Initial configuration')
    elif i == len(result.path()) - 1:
        print('After moving', action, 'into the empty space. Goal achieved!')
    else:
        print('After moving', action, 'into the empty space')
        print(state)


from simpleai.search import CspProblem, backtrack
def constraint_func(names, values):
    return values[0] != values[1]
names = ('Mark', 'Julia', 'Steve', 'Amanda', 'Brian',
             'Joanne', 'Derek', 'Allan', 'Michelle', 'Kelly')
colors = dict((name, ['red', 'green', 'blue', 'gray']) for name
                  in names)
constraints = [
    (('Mark', 'Julia'), constraint_func),
(('Mark', 'Steve'), constraint_func),
(('Julia', 'Steve'), constraint_func),
(('Julia', 'Amanda'), constraint_func),
(('Julia', 'Derek'), constraint_func),
(('Julia', 'Brian'), constraint_func),
(('Steve', 'Amanda'), constraint_func),
(('Steve', 'Allan'), constraint_func),
(('Steve', 'Michelle'), constraint_func),
(('Amanda', 'Michelle'), constraint_func),
(('Amanda', 'Joanne'), constraint_func),
(('Amanda', 'Derek'), constraint_func),
(('Brian', 'Derek'), constraint_func),
(('Brian', 'Kelly'), constraint_func),
(('Joanne', 'Michelle'), constraint_func),
(('Joanne', 'Amanda'), constraint_func),
(('Joanne', 'Derek'), constraint_func),
(('Joanne', 'Kelly'), constraint_func),
(('Derek', 'Kelly'), constraint_func),
]
problem = CspProblem(names, colors, constraints)
output = backtrack(problem)
print('\nColor mapping:\n')
for k, v in output.items():
    print(k, '==>', v)


import numpy as np
import matplotlib.pyplot as plt
import skfuzzy as fuzz
x = np.arange(0, 10.1, 0.1)
mfx = fuzz.gauss2mf(x, 5,1,7,1) 
plt.plot(x, mfx, 'r',ls='-.')
x = np.arange(0, 10.1, 0.1)
mfx = fuzz.trapmf(x, [2, 5, 7, 10])
defuzz_centroid = fuzz.defuzz(x, mfx, 'centroid')  
print(defuzz_centroid)
xv=[defuzz_centroid]
ymax = [fuzz.interp_membership(x, mfx, i) for i in xv]
plt.plot(x, mfx, 'k')
plt.vlines(defuzz_centroid, 0, ymax, label='Centroid', color='r')
plt.ylabel('Fuzzy membership')
plt.xlabel('Universe variable (arb)')
plt.ylim(-0.1, 1.1)
plt.legend(loc=2)
plt.show()


import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
quality = ctrl.Antecedent(np.arange(0, 11, 1), 'quality')
service = ctrl.Antecedent(np.arange(0, 11, 1), 'service')
tip = ctrl.Consequent(np.arange(0, 26, 1), 'tip')
quality.automf(3)
service.automf(3)
tip['low'] = fuzz.trimf(tip.universe, [0, 0, 13])
tip['medium'] = fuzz.trimf(tip.universe, [0, 13, 25])
tip['high'] = fuzz.trimf(tip.universe, [13, 25, 25])
quality['average'].view()
service.view()
tip.view()
rule1 = ctrl.Rule(quality['poor'] & service['poor'], tip['low'])
rule2 = ctrl.Rule(service['average'], tip['medium'])
rule3 = ctrl.Rule(service['good'] | quality['good'], tip['high'])
rule1.view()
tipping_ctrl = ctrl.ControlSystem([rule1, rule2, rule3])
tipping = ctrl.ControlSystemSimulation(tipping_ctrl)
tipping.input['quality'] = 10
tipping.input['service'] = 10
tipping.compute()
print (tipping.output['tip'])
tip.view(sim=tipping)