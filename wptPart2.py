import random

temp = True

'''
function move_trainer
list of directions, selects and prints random direction
inputs: none
outputs: randomly picked direction, random value
'''
def move_trainer():  
    
    '''
    second draft of function that will be used to
    a. select a direction at random
    b. select a random probability value between (0,1)
    '''    
    direction = random.choice(['N', 'E', 'S', 'W'])
    value = random.random()
    return (direction, value)
    
'''
function throw_pokeball
first draft of the fucntion to generate list of T and F based on
a. the number of falses required and
b. the number of trues required

input: num_false -> number of falses required
       num_true  -> number of trues  required

output: randomly selected boolean
'''     
def throw_pokeball(num_false, num_true):  
    
    '''
    second draft of function that will be used to
    a. generate a list of T and F
    b. make a random choice from the list generated
    c. print value chosen
    '''        
    bool_list = []
    for i in range(num_false):
        bool_list.append(False)
    for i in range(num_true):
        bool_list.append(True)
    bool_picked = random.choice(bool_list)
    return (bool_picked)

grid_size = int(input("Enter the integer grid size => "))
print(grid_size)

user_prob = input("Enter a probability (0.0 - 1.0) => ")
print(user_prob)
user_prob = float(user_prob)

seed_value = 10*grid_size + grid_size
random.seed(seed_value)

rloc = grid_size//2
cloc = grid_size//2
location = (rloc, cloc)
sfalse = 3
strue = 1
i = 0
pseen = 0
pcaught = 0


while temp == True:
    if location[0] == 0 or location[0] == (grid_size - 1) or location[1] == 0\
       or location[1] == (grid_size - 1):
        print("Trainer left the field at turn " + str(i) + ", location " +\
        str(location) + ".\n" + str(pseen), "pokemon were seen,", pcaught,\
        "of which were captured.")
        break
        
    mt = move_trainer()
    if mt[0] == 'N':
        rloc -= 1
        location = (rloc, cloc)
    elif mt[0] == 'S':
        rloc += 1
        location = (rloc, cloc)
    elif mt[0] == 'E':
        cloc += 1
        location = (rloc, cloc)
    elif mt[0] == 'W':
        cloc -= 1
        location = (rloc, cloc)
    i += 1

    if mt[1] <= user_prob:
        tp = throw_pokeball(sfalse, strue)
        print("Saw a pokemon at turn " + str(i) + ", location", location)
        pseen += 1
        if tp == True:
            strue += 1
            print("Caught it!")
            pcaught += 1
        else:
            print("Missed ...")
            continue
        
if __name__ == "__main__":
    
    pass