import random

def flag_choice():
    flag = random.choice([True, False])
    return flag

def computer_motion(conf):
    if conf <= 28:
            motion = conf
    elif conf ==30:
            motion = 1
    elif conf ==31:
            motion = 2 
    elif conf ==32:
            motion = 3
    elif conf ==33:
            motion = 4
    elif conf ==34:
            motion = 5
    else:
            motion = random.randint(1,28)
    return motion