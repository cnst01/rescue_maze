class Move:
    def __init__(self, pos, move):
        self.pos = pos
        self.move = move

def goto(pos1, pos2):
    if pos1[0] < pos2[0]:
        # print("going right for:" + str(pos2[0] - pos1[0]))
        print("->")
        return Move(pos2, "right")
    elif pos1[0] > pos2[0]:
        # print("going left for:" + str(pos1[0] - pos2[0]))
        print("<-")
        return Move(pos2, "left")
    if pos1[1] > pos2[1]:
        # print("going down for:" + str(pos1[1] - pos2[1]))
        print("Down")
        return Move(pos2, "down")
    elif pos1[1] < pos2[1]:
        # print("going up for:" + str(pos2[1] - pos1[1]))
        print("Up")
        return Move(pos2, "up")
    return Move(pos2, None)
