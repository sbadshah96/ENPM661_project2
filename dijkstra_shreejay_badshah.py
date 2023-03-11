from queue import PriorityQueue
import time
import matplotlib.pyplot as plt
# from matplotlib.figure import Figure
# from matplotlib.backends.backend_agg import FigureCanvasAgg
# from PIL import Image
from matplotlib import animation

def project_map():
    rectangle_boundary = plt.Rectangle((0,0), 600, 250, color='#474749')
    rectangle = plt.Rectangle((5,5), 590, 240, color='#C9EEF8')
    rectangle1 = plt.Rectangle((95,0),60,105,color='#33B8FF')
    rectangle2 = plt.Rectangle((95,145),60,105,color='#33B8FF')
    points1 = [[455,3.78],[455,246.22],[515.61,125]]
    triangle = plt.Polygon(points1,closed=None,fill='#33B8FF')
    # points2 = [[300,50],[385,87.5],[385,162.5],[300,200],[215,162.5],[215,87.5]]
    points2 = [[300,41.34],[369.95,84.17],[369.95,164.93],[300,208.66],[230.03,164.93],[230.03,84.17]]
    hexagon = plt.Polygon(points2,closed=None,fill='#33B8FF')
    plt.gca().add_patch(rectangle_boundary)
    plt.gca().add_patch(rectangle)
    plt.gca().add_patch(rectangle1)
    plt.gca().add_patch(rectangle2)
    plt.gca().add_patch(triangle)
    plt.gca().add_patch(hexagon)

    plt.xlim(0,650)
    plt.ylim(0,250)
    # plt.autoscale(enable='True',axis='x')

    # plt.rcParams["figure.figsize"] = [650, 250]
    # plt.rcParams["figure.autolayout"] = True

    for val in explored_mapping:
        plt.scatter(val[0],val[1],marker='o', color='#F6F8C9', s=0.1)
       
    # plt.pause(2)
    for val in backtrack:
        plt.scatter(val[0],val[1],marker='o', color='red', s=0.3)

    plt.show()

def obstacles(x,y):
    if (x>=95 and x<=155 and y>=0 and y<=105):
        return False
    elif (x>=95 and x<=155 and y>=145 and y<=250):
        return False
    elif ((y-(0.61*x) >= -142.34) and (x <= 369.5) and (y+(0.62*x) <= 396.15) and (y-(0.62*x) <= 21.16) and (x >= 230.03) and (y+(0.62*x) >= 224.97)):
        return False
    elif ((y-(1.99*x) >= -906.21) and (y+(1.99*x) <= 1156.29) and (x >= 455)):
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
                    explored_nodes.queue[i][2] = new_node[2]
                    return None
                else:
                    return None
        explored_nodes.put(new_node)
        node_records[new_node[3]] = pop[3]
        explored_mapping.append(new_node[3])
        # plt.scatter(new_node[3][0],new_node[3][1],marker='o', color='#F6F8C9', s=1)

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
        # plt.scatter(key[0],key[1],marker='o', color='red', s=1.2)
    return backtrack[::-1]

init_pos = (160,220)
x_s = init_pos[0]
y_s = init_pos[1]

goal_pos = (8,8)
x_f = goal_pos[0]
y_f = goal_pos[1]

# init_pos = input('Initial position: ')
# init_pos = tuple(int(i) for i in init_pos.split(" "))
# x_s = init_pos[0]
# y_s = init_pos[1]

# goal_pos = input('Goal position: ')
# goal_pos = tuple(int(i) for i in goal_pos.split(" "))
# x_f = goal_pos[0]
# y_f = goal_pos[1]

explored_nodes = PriorityQueue()
explored_mapping = []
visited_nodes = []
backtrack = []
back_points = []
node_records = {}
pop = []
index = 0

if __name__ == '__main__' :
    start = time.time()

    if obstacles(x_s,y_s) and obstacles(x_f,y_f):
        print('Dijkstraring........')
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
                print('Explored Nodes size: ',explored_nodes.qsize())
                print('Visited Nodes length: ',len(visited_nodes))
                print('Last pop[3]: ',pop[3])
                print('Explored Mapping length: ',len(explored_mapping))
                # print('Backtracking: ',backtracking(pop[3]))
                back_points = backtracking(pop[3])
                end = time.time()
                print('Time: ',round((end - start),2),'s')
                project_map()
                break
    elif not obstacles(x_s,y_s):
        print('Cannot Dijkstrare, starting node in an obstacle space.')
    elif not obstacles(x_f,y_f):
        print('Cannot Dijkstrare, goal node in an obstacle space.')
        
     
