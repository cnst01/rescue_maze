import random as rand
    
def get_rotation():
    return [rand.randint(0,360),rand.randint(0,360)]

def get_direction():
    return rand.randint(0,360)

def get_pitch():
    return rand.randint(0,360)

def move(m, q): #m = tipo do movimento, q = quantidade dele
    if m == 'front':
        return [q,q]
    elif m == "turn":
        return q
        

class robot:
    rotation = get_rotation
    direction = get_direction
    pitch = get_pitch

