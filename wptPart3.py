import random

'''
function move_trainer
list of directions, selects and prints random direction
inputs: none
outputs: randomly picked direction, random value
'''
def move_trainer():   
    '''
    third draft of function that will be used to
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

'''
function run_one_simulation
run a simulation for a given grid & prob. value


input: grid -> 2 dim list to track position of trainer
       prob -> random num from (0, 1)

output: turn -> the number of turns made
'''
def run_one_simulation (grid, prob):
    '''
    function run_one_simulation
    run a simulation for a given grid & prob. value

    the start position of the trainer (x,y) is at
    (size//2, size//2)

    the cells of the grid holds the net pokemons caught
    (always start with zeros)
    
    as long as the trainer is within the grid
    call move_trainer()

    generate a movement based on the direction from the
    move_trainer call.

    make the move (called a turn) and increment the
    # of turns made till now.
    Also, check if value of our input probability
    is >= the seen value from the move_trainer call

    if input probability is >= the seen value,
    call the throw_pokeball function
    the start values for (F,T) to call the fuction is (3,1)
    If pokeball returns true, then
    a. increment the value of T for the next throw_pokeball call
    b. increment the grid[x][y] by 1 to indicate a caught pokemon

    if pokeball returns false, then
    a. decrement the grid[x][y] by 1 to indicate a failed catch

    check value of x and y. if values of x or y is 0 or grid-size
    that means our trainer is on the edge - time to stop simulation
    so, set the trainer_in_field flag to false
    
    the simulation stops when the trainer has reached the edge.
    return the # of turns made for the simulation  
    '''    
    
    temp = True
    rloc = grid_size//2
    cloc = grid_size//2
    location = (rloc, cloc)
    sfalse = 3
    strue = 1
    i = 0
    
    while temp:
        if location[0] == 0 or location[0] == (grid_size - 1) or location[1] == 0\
           or location[1] == (grid_size - 1):
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
            if tp == True:
                strue += 1
                grid[rloc][cloc] += 1
            else:
                grid[rloc][cloc] -= 1
                continue
    return(i)


        
grid_size = int(input("Enter the integer grid size => "))
print(grid_size)
    
user_prob = input("Enter a probability (0.0 - 1.0) => ")
print(user_prob)
user_prob = float(user_prob)
    
seed_value = 10*grid_size + grid_size
random.seed(seed_value)    

count_grid = []
for i in range(grid_size):
    count_grid.append( [0]*grid_size )

num_sims = int(input("Enter the number of simulations to run => "))
print(num_sims)
    
print()

num_turns = []
for i in range(num_sims):
    num_turns.append(run_one_simulation(count_grid, user_prob))

for grid in count_grid:
    for number in grid:
        print("{:5d}".format(number), end = '')
    print('')
        
avg_turns = sum(num_turns) / num_sims
print("Average number of turns in a simulation was {:.2f}".format(avg_turns))
    
max_turns = max(num_turns)    
max_turns_idx = num_turns.index(max_turns) + 1
print("Maximum number of turns was", max_turns, "in simulation", max_turns_idx)
    
min_turns = min(num_turns)    
min_turns_idx = num_turns.index(min_turns) + 1
print("Minimum number of turns was", min_turns, "in simulation", min_turns_idx)

best_net = max(max(row) for row in count_grid)
print("Best net missed pokemon versus caught pokemon is", best_net)

wrst_net = min(min(row) for row in count_grid)
print("Worst net missed pokemon versus caught pokemon is", wrst_net)

if __name__ == "__main__":

    pass