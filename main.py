from walls import check_walls
import time
import plotly.express as px

class Position:
    def __init__(self, pos, views):
        self.pos = pos
        self.views = views


intersections = list()
myMap = list()
myMap.append(Position([0,0],check_walls()))

class positions:  
    x = list()
    y = list()


while len(myMap) - 50:
    time.sleep(0.1)
    pose = myMap[-1] # pega o obj da posição atual
    msg = str(pose.pos) + "  " + str(pose.views)
    print(msg)
    if sum(pose.views) == 0: #checa se nao existe nenhuma parede
        myMap.append(Position([pose.pos[0],pose.pos[1]+1],check_walls())) #adiciona uma posição acima ao mapa
    elif sum(pose.views) == 1: #checa se é interseccao
        if pose.pos in intersections: #checa se já foi contabilizada
            if not myMap[-1].views[2]: #checa se havia o caminho da direita
                myMap[-1].views[2] == True #elimina o caminho da direita
            elif not myMap[-1].views[1]: #checa se havia caminho do meio
                myMap[-1].views[1] == True #elimina o caminho do meio
        else:
            intersections.append(pose) #grava nova interseccao
            if not pose.views[2]: #checa se ha caminho a direita
                myMap[-1].views[2] == True #elimina o caminho da direita
                myMap.append(Position([pose.pos[0]+1,pose.pos[1]],check_walls())) #cria nova posicao para direita
            else:
                myMap[-1].views[1] == True #elimina o caminho do meio
                myMap.append(Position([pose.pos[0],pose.pos[1]+1],check_walls())) #cria nova posicao para cima
    elif sum(pose.views) == 2: #checa se há caminho
        if not pose.views[2]:
            myMap.append(Position([pose.pos[0]+1,pose.pos[1]],check_walls())) #cria nova posicao para direita
        elif not pose.views[1]:
            myMap.append(Position([pose.pos[0],pose.pos[1]+1],check_walls())) #cria nova posicao para cima
        else:
            myMap.append(Position([pose.pos[0]-1,pose.pos[1]],check_walls())) #cria nova posicao para esquerda
    else:
        last_intersection = myMap.index(intersections[-1]) #recebe ultima interseccao
        i = len(myMap)-1 
        msg = str(myMap[-1].pos) + "  Sem saida"
        print(msg)
        while i > last_intersection:
            msg = str(myMap[-1].pos) + "  " + str(myMap[-1].views)
            print(msg)
            myMap.pop() #elimina todas as posicoes ate ela
            i-= 1
        print("voltei")

for points in myMap:
    positions.x.append(points.pos[0])
    positions.y.append(points.pos[1])
print(len(positions.x))
print(len(positions.y))
fig=px.scatter(x=positions.x, y=positions.y)
fig.show()