from queue import PriorityQueue
import time

def obstacles(x,y):
    if (x>=95 and x<=155 and y>=0 and y<=105):
        return False
    elif (x>=95 and x<=155 and y>=145 and y<=250):
        return False
    elif ((y-(0.52*x) >= -113.27) and (x <= 372.5) and (y+(0.52*x) <= 363.27) and (y-(0.52*x) <= 55.86) and (x >= 227.98) and (y+(0.52*x) >= 199.14)):
        return False
    elif ((y-(1.99*x) >= -858.18) and (y+(1.9*x) <= 1108.18) and (x >= 455)):
        return False
    elif(x<=5 or x>=595 or y<=5 or y>=245):
        return False
    else:
        return True

def check_new_node(new_node):
    if new_node[3] not in visited_nodes:
        for i in range(explored_nodes.qsize()):
            if explored_nodes.queue[i][3] == new_node[3]:
                if explored_nodes.queue[i][0] > new_node[0]:
                    explored_nodes.queue[i][0] = new_node[0]
                    # explored_nodes.queue[i][1] = node[1]
                    explored_nodes.queue[i][2] = new_node[2]
                    return None
                else:
                    return None
        explored_nodes.put(new_node)
        node_records[new_node[3]] = pop[3]
        explored_mapping.append(new_node[3])

def action1(pop,index):
    c2c = pop[0]
    node_index = pop[1]
    x,y = pop[3]
    obs = obstacles(x+1,y)
    if obs:
        new_node = (round(c2c+1,2),index,node_index,(x+1,y))
        # print('new node from action1: ',new_node)
        # explored_nodes.put(new_node)
        check_new_node(new_node)

def action2(pop,index):
    c2c = pop[0]
    node_index = pop[1]
    x,y = pop[3]
    obs = obstacles(x-1,y)
    if obs:
        new_node = (round(c2c+1,2),index,node_index,(x-1,y))
        # print('new node from action2: ',new_node)
        # explored_nodes.put(new_node)
        check_new_node(new_node)

def action3(pop,index):
    c2c = pop[0]
    node_index = pop[1]
    x,y = pop[3]
    obs = obstacles(x,y+1)
    if obs:
        new_node = (round(c2c+1,2),index,node_index,(x,y+1))
        # print('new node from action2: ',new_node)
        # explored_nodes.put(new_node)
        check_new_node(new_node)

def action4(pop,index):
    c2c = pop[0]
    node_index = pop[1]
    x,y = pop[3]
    obs = obstacles(x,y-1)
    if obs:
        new_node = (round(c2c+1,2),index,node_index,(x,y-1))
        # print('new node from action2: ',new_node)
        # explored_nodes.put(new_node)
        check_new_node(new_node)

def action5(pop,index):
    c2c = pop[0]
    node_index = pop[1]
    x,y = pop[3]
    obs = obstacles(x+1,y+1)
    if obs:
        new_node = (round(c2c+1.4,2),index,node_index,(x+1,y+1))
        # print('new node from action2: ',new_node)
        # explored_nodes.put(new_node)
        check_new_node(new_node)

def action6(pop,index):
    c2c = pop[0]
    node_index = pop[1]
    x,y = pop[3]
    obs = obstacles(x-1,y+1)
    if obs:
        new_node = (round(c2c+1.4,2),index,node_index,(x-1,y+1))
        # print('new node from action2: ',new_node)
        # explored_nodes.put(new_node)
        check_new_node(new_node)

def action7(pop,index):
    c2c = pop[0]
    node_index = pop[1]
    x,y = pop[3]
    obs = obstacles(x+1,y-1)
    if obs:
        new_node = (round(c2c+1.4,2),index,node_index,(x+1,y-1))
        # print('new node from action2: ',new_node)
        # explored_nodes.put(new_node)
        check_new_node(new_node)

def action8(pop,index):
    c2c = pop[0]
    node_index = pop[1]
    x,y = pop[3]
    obs = obstacles(x-1,y-1)
    if obs:
        new_node = (round(c2c+1.4,2),index,node_index,(x-1,y-1))
        # print('new node from action2: ',new_node)
        # explored_nodes.put(new_node)
        check_new_node(new_node)

def backtracking(pops):
    backtrack.append(pops)
    # print('backtrack: ',backtrack)
    key = node_records[pops]
    backtrack.append(key)
    while key!=init_pos:
        key = node_records[key]
        backtrack.append(key)
    return backtrack[::-1]

init_pos = input('Initial Position: ')
init_pos = tuple(int(i) for i in init_pos.split(" "))
x_s = init_pos[0]
y_s = init_pos[1]

goal_pos = input('Enter the goal state : ')
goal_pos = tuple(int(i) for i in goal_pos.split(" "))
x_f = goal_pos[0]
y_f = goal_pos[1]

# init_pos = (6,6)
# x_s = init_pos[0]
# y_s = init_pos[1]

# goal_pos = (50,25)
# x_f = goal_pos[0]
# y_f = goal_pos[1]



explored_nodes = PriorityQueue()
explored_mapping = []
visited_nodes = []
backtrack = []
node_records = {}
pop = []
index = 0

if __name__ == '__main__' :
    start = time.time()

    if obstacles(x_s,y_s) and obstacles(x_f,y_f):
        print('Good to go.')
        init_node = (0,0,0,(x_s,y_s))
        explored_nodes.put(init_node)  #open list
        explored_mapping.append(init_node[3]) #mapping
        while not explored_nodes.empty():
            pop = explored_nodes.get()
            # print('pop: ',pop)
            visited_nodes.append(pop[3])
            
            if pop[3]!=goal_pos:
                index+=1
                action1(pop,index)
                index+=1
                action2(pop,index)
                index+=1
                action3(pop,index)
                index+=1
                action4(pop,index)
                index+=1
                action5(pop,index)
                index+=1
                action6(pop,index)
                index+=1
                action7(pop,index)
                index+=1
                action8(pop,index)

            else:
                # print('Explored Nodes: ',explored_nodes.queue)
                print('Visited Nodes: ', visited_nodes)
                print('Last pop[3]: ',pop[3])
                # print('Explored Mapping: ',explored_mapping)
                print('Backtracking: ',backtracking(pop[3]))
                end = time.time()
                print(end - start)
                break
    else:
        print('Not good to go.')