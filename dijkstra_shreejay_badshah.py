from queue import PriorityQueue
import time
import pygame

def pygame_plot():
    pygame.init()
    display_size = [600, 250]
    canvas = pygame.display.set_mode(display_size)
    pygame.display.set_caption("Map Exploration")

    done = False
    clock = pygame.time.Clock()
    
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
        canvas.fill("white")

        x, y = convert_to_pycoord((95,0),105)
        pygame.draw.rect(canvas, "#B11F1D", [x, y, 60, 105], 0)

        x, y = convert_to_pycoord((100,0),100)
        pygame.draw.rect(canvas, "#F8C9F4", [x, y, 50, 100], 0)

        x, y = convert_to_pycoord([95, 145],105)
        pygame.draw.rect(canvas, "#B11F1D", [x, y, 60, 105], 0)

        x, y = convert_to_pycoord([100, 150],100)
        pygame.draw.rect(canvas, "#F8C9F4", [x, y, 50, 100], 0)

        x1,y1 = convert_to_pycoord([300,41.3])
        x2,y2 = convert_to_pycoord([370,84.6])
        x3,y3 = convert_to_pycoord([370,165.3])
        x4,y4 = convert_to_pycoord([300,208.6])
        x5,y5 = convert_to_pycoord([230,165.3])
        x6,y6 = convert_to_pycoord([230.05,84.6])
        pygame.draw.polygon(canvas, "#E40D06", [[x1,y1],[x2, y2],[x3,y3],[x4,y4],[x5,y5],[x6,y6]],0)

        pygame.draw.polygon(canvas, "#ED26F0", ((300, 50),(365, 87.5),(365, 162.5),(300, 200),(235, 162.5),(235, 87.5)))

        x1,y1 = convert_to_pycoord([455,20])
        x2,y2 = convert_to_pycoord([463,20])
        x3,y3 = convert_to_pycoord([515.6,125])
        x4,y4 = convert_to_pycoord([463,230])
        x5,y5 = convert_to_pycoord([455,230])
        pygame.draw.polygon(canvas, "#932CF5", ([x1,y1],[x2, y2],[x3,y3],[x4,y4],[x5,y5]),0)

        x1,y1 = convert_to_pycoord([460,25])
        x2,y2 = convert_to_pycoord([460,225])
        x3,y3 = convert_to_pycoord([510,125])
        pygame.draw.polygon(canvas, "#AE6BF5", [[x1,y1],[x2, y2],[x3,y3]],0)

        for val in visited_nodes:
            pygame.draw.circle(canvas,(50,137,131),convert_to_pycoord(val),1)
            pygame.display.flip()
            clock.tick(100)

        for val in backtrack:
            pygame.draw.circle(canvas,(255,255,0),convert_to_pycoord(val),1)
            pygame.display.flip()
            clock.tick(100)

        pygame.display.flip()
        pygame.time.wait(3000)
        done = True
    pygame.quit()

def obstacles(x,y):
    if (95<=x<=155 and 0<=y<=105):
        return False
    elif (95<=x<=155 and 145<=y<=250):
        return False
    elif (int((y-(0.61*x)) >= -142.34) and (x <= 369.5) and (int(y+(0.62*x)) <= 396.15) and (int(y-(0.62*x)) <= 21.16) and (x >= 230.03) and (int(y+(0.62*x)) >= 224.97)):
        return False
    elif (int((y-(1.99*x)) >= -906.21) and (int(y+(1.99*x)) <= 1156.29) and (x >= 455) and (y<=230) and (y>=20)):
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

def convert_to_pycoord(coord,height=0):
        return coord[0], 250 - coord[1] - height

init_pos = input('Initial position (separated by a comma, no space): ')
init_pos = tuple(int(i) for i in init_pos.split(","))
x_s = init_pos[0]
y_s = init_pos[1]

goal_pos = input('Goal position (separated by a comma, no space): ')
goal_pos = tuple(int(i) for i in goal_pos.split(","))
x_f = goal_pos[0]
y_f = goal_pos[1]

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
             #closed list
            if pop[3]!=goal_pos:
                if pop[3] not in visited_nodes:
                    visited_nodes.append(pop[3])

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
                print('Backtracking: ',backtracking(pop[3]))
                end = time.time()
                print('Time: ',round((end - start),2),'s')
                pygame_plot()
                break

    elif not obstacles(x_s,y_s):
        print('Cannot Dijkstrare, starting node in an obstacle space.')
    elif not obstacles(x_f,y_f):
        print('Cannot Dijkstrare, goal node in an obstacle space.')

    