import random as rand
def check_walls(): 
    x = [rand.randint(0,255), rand.randint(0,255), rand.randint(0,255)]
    x = list(map(wall_recog, x))
    return x

def wall_recog(x):
    return x <= 80