import random

'''
function move_trainer
list of directions, selects and prints random direction
inputs: none
outputs: directions, randomly picked direction, random value
'''
def move_trainer(): 
    
    '''
    first draft of function that will be used to
    a. select a direction at random
    b. select a random probability value between (0,1)
    '''
    
    direction = random.choice(['N', 'E', 'S', 'W'])
    value = "{:.2f}".format(random.random())
    str_dir = "Directions: ['N', 'E', 'S', 'W']"
    return (str_dir, direction, value)
 
'''
function throw_pokeball
first draft of the fucntion to generate list of T and F based on
a. the number of falses required and
b. the number of trues required

input: num_false -> number of falses required
       num_true  -> number of trues  required

output: list of booleans, the randomly selected boolean
'''   
def throw_pokeball(num_false, num_true): 
    
    '''
    first draft of function that will be used to
    a. generate a list of T and F
    b. make a random choice from the list generated
    c. print the list and value chosen
    '''    
    bool_list = []
    for i in range(num_false):
        bool_list.append(False)
    for i in range(num_true):
        bool_list.append(True)
    bool_picked = random.choice(bool_list)
    return (bool_list, bool_picked)

grid_size = int(input("Enter the integer grid size => "))
print(grid_size)

num_false = int(input("Enter the integer number of Falses => "))
print(num_false)

num_true = int(input("Enter the integer number of Trues => "))
print(num_true)

seed = grid_size * 11

print("Setting seed to", seed)

random.seed(seed)

for i in range(5):
    mt = move_trainer()
    print(mt[0] + "\n" + "Selected " + mt[1] + ",", "value " + mt[2])
    
for i in range(5):
    tp = throw_pokeball(num_false, num_true)
    print("Booleans: " + str(tp[0]) + "\n" + "Selected", tp[1])
    
if __name__ == "__main__":
    
    pass