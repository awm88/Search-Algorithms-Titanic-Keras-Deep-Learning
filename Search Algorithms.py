# -*- coding: utf-8 -*-
"""
Created on Sun Sep 26 11:19:15 2021

@author: awmna
"""

# Node with weight


def get_node(name, weight=None):

    node = {}
    node['name'] = name
    node['children'] = []
    node['weight'] = weight

    return node


def add_child(node, name, weight):
    node['children'].append(get_node(name, weight))

    return node['children'][-1]


tree = get_node('St. Marys')

# Children of St. Marys: Stratford, Michell
add_child(tree, 'Stratford', 30)
add_child(tree, 'Mitchell', 80)

# Children of Stratford: New Hamburg, Drayton
add_child(tree['children'][0], 'New Hamburg', 25)
add_child(tree['children'][0], 'Drayton', 200)
add_child(tree['children'][0], 'St. Marys', 30)

# Children of Mitchell: Listowel, St. Marys
add_child(tree['children'][1], 'Listowel', 100)
add_child(tree['children'][1], 'St. Marys', 80)

# Children of New Hamburg: Stratford, Woodstock, Kitchener
add_child(tree['children'][0]['children'][0], 'Kitchener', 90)
add_child(tree['children'][0]['children'][0], 'Woodstock', 100)
add_child(tree['children'][0]['children'][0], 'Stratford', 25)

# Children of Drayton: Minto, M Forst, Orangeville, Guelph, Listowel
add_child(tree['children'][0]['children'][1], 'Minto', 70)
add_child(tree['children'][0]['children'][1], 'M Forest', 50)
add_child(tree['children'][0]['children'][1], 'Orangeville', 100)
add_child(tree['children'][0]['children'][1], 'Guelph', 100)
add_child(tree['children'][0]['children'][1], 'Listowel', 100)

# Children of Listowel: Mitchell, Minto, Drayton
add_child(tree['children'][1]['children'][0], 'Mitchell', 100)
add_child(tree['children'][1]['children'][0], 'Minto', 45)
add_child(tree['children'][1]['children'][0], 'Drayton', 100)

# Children of Kitchener: Guelph, New Hamburg, Woodstock
add_child(tree['children'][0]['children'][0]['children'][0], 'Guelph', 30)
add_child(tree['children'][0]['children'][0]['children'][0], 'New Hamburg', 90)
add_child(tree['children'][0]['children'][0]['children'][0], 'Woodstock', 100)

# Children of Woodstock: Brantford, New Hamburg, Kitchener
add_child(tree['children'][0]['children'][0]['children'][1], 'Brantford', 110)
add_child(tree['children'][0]['children'][0]['children'][1], 'New Hamburg', 60)
add_child(tree['children'][0]['children'][0]['children'][1], 'Kitchener', 100)

# Children of Minto: M Forest, Listowel, Drayton
add_child(tree['children'][0]['children'][1]['children'][0], 'M Forest', 25)
add_child(tree['children'][0]['children'][1]['children'][0], 'Listowel', 45)
add_child(tree['children'][0]['children'][1]['children'][0], 'Drayton', 70)

# Children of M Forest: Orangeville, Drayton, Minto
add_child(tree['children'][0]['children'][1]['children'][1], 'Orangeville', 160)
add_child(tree['children'][0]['children'][1]['children'][1], 'Drayton', 50)
add_child(tree['children'][0]['children'][1]['children'][1], 'Minto', 70)

# Children of Orangeville: Newmarket, Vaughan, Halton Hills, M Forest,
# Drayton, Guelph
add_child(tree['children'][0]['children'][1]['children'][2], 'Newmarket', 200)
add_child(tree['children'][0]['children'][1]['children'][2], 'Vaughan', 140)
add_child(tree['children'][0]['children'][1]['children'][2], 'Halton Hills', 100)
add_child(tree['children'][0]['children'][1]['children'][2], 'M Forest', 160)
add_child(tree['children'][0]['children'][1]['children'][2], 'Drayton', 100)
add_child(tree['children'][0]['children'][1]['children'][2], 'Guelph', 120)

# Children of Guelph: Cambridge, Burlington, Halton Hills, Orangeville,
# Drayton, Kitchener
add_child(tree['children'][0]['children'][0]['children'][0]['children'][0],
          'Drayton', 100)
add_child(tree['children'][0]['children'][0]['children'][0]['children'][0],
          'Orangeville', 120)
add_child(tree['children'][0]['children'][0]['children'][0]['children'][0],
          'Halton Hills', 100)
add_child(tree['children'][0]['children'][1]['children'][3], 'Cambridge', 40)
add_child(tree['children'][0]['children'][1]['children'][3], 'Burlington', 120)
add_child(tree['children'][0]['children'][1]['children'][3], 'Halton Hills', 100)
add_child(tree['children'][0]['children'][1]['children'][3], 'Orangeville', 120)
add_child(tree['children'][0]['children'][1]['children'][3], 'Drayton', 100)
add_child(tree['children'][0]['children'][1]['children'][3], 'Kitchener', 30)

# Children of Brantford: Caledonia, Cambridge, Woodstock
add_child(tree['children'][0]['children'][0]['children'][1]['children'][0],
          'Caledonia', 40)
add_child(tree['children'][0]['children'][0]['children'][1]['children'][0],
          'Cambridge', 80)
add_child(tree['children'][0]['children'][0]['children'][1]['children'][0],
          'Woodstock', 110)

# Children of Newmarket: Richmond Hill, Oshawa, Orangeville, Vaughan
add_child(tree['children'][0]['children'][1]['children'][2]['children'][0],
          'Richmond Hill', 80)
add_child(tree['children'][0]['children'][1]['children'][2]['children'][0], 'Oshawa', 180)
add_child(tree['children'][0]['children'][1]['children'][2]['children'][0],
          'Orangeville', 200)
add_child(tree['children'][0]['children'][1]['children'][2]['children'][0], 'Vaughan', 80)

# Children of Vaughan: Brampton, Toronto, Orangeville, Richmond Hill, Newmarket
add_child(tree['children'][0]['children'][1]['children'][2]['children'][1], 'Brampton', 45)
add_child(tree['children'][0]['children'][1]['children'][2]['children'][1], 'Toronto', 45)
add_child(tree['children'][0]['children'][1]['children'][2]['children'][1],
          'Orangeville', 140)
add_child(tree['children'][0]['children'][1]['children'][2]['children'][1],
          'Richmond Hill', 30)
add_child(tree['children'][0]['children'][1]['children'][2]['children'][1],
          'Newmarket', 80)

# Children of Halton Hills: Missisauga, Guelph, Orangeville
add_child(tree['children'][0]['children'][1]['children'][2]['children'][2],
          'Missisauga', 40)
add_child(tree['children'][0]['children'][1]['children'][2]['children'][2],
          'Guelph', 100)
add_child(tree['children'][0]['children'][1]['children'][2]['children'][2],
          'Orangeville', 100)
add_child(tree['children'][0]['children'][0]['children'][0]['children'][0]['children'][2],
          'Missisauga', 35)
add_child(tree['children'][0]['children'][0]['children'][0]['children'][0]['children'][2],
          'Orangeville', 100)

# Children of Cambridge: Guelph, Brantford
add_child(tree['children'][0]['children'][0]['children'][1]['children'][0]['children'][1],
          'Guelph', 40)
add_child(tree['children'][0]['children'][0]['children'][1]['children'][0]['children'][1],
          'Brantford', 80)

# Children of Burlington: Hamilton, Oakville, Guelph
add_child(tree['children'][0]['children'][1]['children'][3]['children'][1], 'Hamilton', 15)
add_child(tree['children'][0]['children'][1]['children'][3]['children'][1], 'Oakville', 50)
add_child(tree['children'][0]['children'][1]['children'][3]['children'][1], 'Guelph', 120)

# Children of Caledonia: St Catharina, Brantford, Hamilton
add_child(tree['children'][0]['children'][0]['children'][1]['children'][0]['children'][0],
          'St Catharina', 200)
add_child(tree['children'][0]['children'][0]['children'][1]['children'][0]['children'][0],
          'Brantford', 40)
add_child(tree['children'][0]['children'][0]['children'][1]['children'][0]['children'][0],
          'Hamilton', 45)

# Children of Richmond Hill: Markham, Vaughan
add_child(tree['children'][0]['children'][1]['children'][2]['children'][0]['children'][0],
          'Markham', 30)
add_child(tree['children'][0]['children'][1]['children'][2]['children'][0]['children'][0],
          'Vaughan', 30)

# Children of Oshawa: Ajax, Newmarket
add_child(tree['children'][0]['children'][1]['children'][2]['children'][0]['children'][1],
          'Ajax', 35)
add_child(tree['children'][0]['children'][1]['children'][2]['children'][0]['children'][1],
          'Newmarket', 180)

# Children of Missisauga: Toronto, Brampton, Oakville
add_child(tree['children'][0]['children'][0]['children'][0]['children'][0]['children'][2]['children'][0], 'Toronto', 40)
add_child(tree['children'][0]['children'][0]['children'][0]['children'][0]['children'][2]['children'][0], 'Brampton', 45)
add_child(tree['children'][0]['children'][0]['children'][0]['children'][0]['children'][2]['children'][0], 'Oakville', 20)


def DFS(init_state, goal_name):
    """Depth-First Search (DFS)
    Arguments
    ---------
    init_state : the root node of a search tree
    goal_name : A string, the name of a node, e.g. tree.childrend[0].name
    """

    frontier = [init_state]
    explored = []

    while len(frontier):
        state = frontier.pop()  # dequeue

        if state['name'] == goal_name:
            return True

        for child in state['children']:
            if child['name'] not in explored:
                # add child node
                frontier.append(child)
                explored.append(state['name'])
    return False


print(DFS(tree, 'Richmond Hill'))


def get_node(name, heuristic=None):
    node = {}
    node['name'] = name
    node['children'] = []
    node['heuristic'] = heuristic
    node['path'] = []
    return node


def add_child(node, name, heuristic):
    node['children'].append(get_node(name, heuristic))


tree = get_node('Kitchener')
# children of Kitchener:Guelph and New Hamburg
add_child(tree, 'Guelph', 160,)
add_child(tree, 'New Hamburg', 110)

# children of Guelph: Drayton, Kitchener
add_child(tree['children'][0], 'Drayton', 100)
add_child(tree['children'][0], 'Kitchener', 130)

# children of New Hamburg: Stratford, Kitchener
add_child(tree['children'][1], 'Stratford', 100)
add_child(tree['children'][1], 'Kitchener', 130)

# children of Drayton: Listowel,Guelph
add_child(tree['children'][0]['children'][0], 'Listowel', 0)
add_child(tree['children'][0]['children'][0], 'Guelph', 160)

# children of Stratford: St. Marys, Drayton, and New Hamburg
add_child(tree['children'][1]['children'][0], 'St. Marys', 130)
add_child(tree['children'][1]['children'][0], 'Drayton', 100)
add_child(tree['children'][1]['children'][0], 'New Hamburg', 110)

# children of St.Marys: Mitchell,Stratford
add_child(tree['children'][1]['children'][0]['children'][0], 'Mitchell', 100)
add_child(tree['children'][1]['children'][0]['children'][0], 'Stratford', 100)

# children of Drayton: Stratford,Listowel
add_child(tree['children'][1]['children'][0]['children'][1], 'Stratford', 100)
add_child(tree['children'][1]['children'][0]['children'][1], 'Listowel', 0)

# children of Mitchell: St.Marys, Listowel
add_child(tree['children'][1]['children'][0]['children'][0]['children'][0], 'St.Marys', 130)
add_child(tree['children'][1]['children'][0]['children'][0]['children'][0], 'Listowel', 0)


# Greedy helper
def find_min_heuristic(frontier):
    # Helper func to find min of h (the heuristic function)
    min_h_i = 0
    if len(frontier) > 1:
        min_h = frontier[min_h_i]['heuristic']
        for i, state in enumerate(frontier):
            if state['heuristic'] < min_h:
                min_h_i = i
                min_h = state['heuristic']
    return min_h_i


def GreedySearch(init_state, goal_name):
    frontier = [init_state]
    explored = []

    while len(frontier):
        state = frontier.pop(find_min_heuristic(frontier))
        explored.append(state['name'])
        state['path'].append(state['name'])
        if state['name'] == goal_name:
            return state['path']

        for child in state['children']:
            if child['name'] not in explored:
                frontier.append(child)
            child['path'].extend(state['path'])
    return state['path']


print(GreedySearch(tree, 'Listowel'))




  



