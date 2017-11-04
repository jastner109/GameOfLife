import numpy as np
from itertools import product
import matplotlib.pyplot as plt
import matplotlib.colors as color
import os
import time


def showgame(generation, color_scheme): # creates image of a particular generation
    
    if color_scheme == 0:
    
        fig = plt.imshow(generation, interpolation = None, cmap = color.ListedColormap([(0.0, 0.0, 1.0),(0.0, 1.0, 0.0)])) # (R,G,B)
        plt.grid(ls = "solid")
        plt.xticks(np.arange(0.5, generation.shape[0], 1))
        plt.yticks(np.arange(0.5, generation.shape[1], 1))
        plt.grid(color = "red", linewidth = 4, linestyle = "-")
        plt.tick_params(axis = "x", colors = (0,0,0,0))
        plt.tick_params(axis = "y", colors = (0,0,0,0))
    
    elif color_scheme == 1:
    
        fig = plt.imshow(generation, interpolation = None, cmap = color.ListedColormap(["white","black"])) # grayscale
        plt.grid(ls = "solid")
        plt.xticks(np.arange(0.5, generation.shape[0], 1))
        plt.yticks(np.arange(0.5, generation.shape[1], 1))
        plt.grid(color = "black", linewidth = 4, linestyle = "-")
        plt.tick_params(axis = "x", colors = (0,0,0,0))
        plt.tick_params(axis = "y", colors = (0,0,0,0))
    
    return fig

def seed(gridsize, number_of_seeds): # returns seed generation using provided parameters
    
    seed_matrix = np.full((gridsize, gridsize), False)
    seed_idx = list(zip(np.random.choice(range(1, gridsize-1), number_of_seeds, replace = True), np.random.choice(range(1, gridsize-1), number_of_seeds, replace = True)))
    for idx in seed_idx:
        seed_matrix[idx[0], idx[1]] = True
        
    return seed_matrix
 

def nextgen(game): # creates next generation using current generation
    
    newgen = np.full((game.shape[0], game.shape[1]), False)
    
    for i, j in product(range(game.shape[0]), range(game.shape[1])):
        
        potential = game[max(0, i-1):min(game.shape[0], i+1)+1, max(0, j-1):min(game.shape[1], j+1)+1]
        
        if game[i,j] == True:               # cell has life
            lives = sum(sum(potential))-1
            if lives == 2 or lives == 3:    # cell lives on
                newgen[i,j] = True
            elif lives < 2 or lives > 3:    # cell dies by underpopulation or overpopulation
                newgen[i,j] = False
        elif game[i,j] == False:            # cell is dead
            lives = sum(sum(potential))
            if lives == 3:
                newgen[i,j] = True          # cell is born
                
    return newgen
    
def comparegens(generations, backoff = 10):
	
	nogen = False	
	
	if len(generations) <= backoff:
		for i in range(len(generations)-2):
			if np.array_equal(generations[i], generations[-1]):
				nogen = True
				break				
	else:
		for i in range(len(generations)-backoff-1, len(generations)-1):
			if np.array_equal(generations[i], generations[-1]):
				nogen = True
				break
				
	return nogen
          
def life(gridsize = 25, number_of_seeds = 100, epochs = 100, color_scheme = 0): # the cycle of life
    
    if color_scheme != 0 and color_scheme != 1:
    	color_scheme = 0
    	print "Invalid color scheme provided. Using default..."
    
    if gridsize <= 10 or gridsize > 100:
        gridsize = 25
        print "Invalid size provided. Using default..."
    
    if number_of_seeds <= gridsize or number_of_seeds > gridsize**2/2: 
        number_of_seeds = gridsize**2/4
        print "Invalid seed number provided. Using default..."
     
    epochs = epochs-2 
       
    if epochs < 10 or epochs > 997:
        epochs = 100
        print "Invalid epochs provided. Using default..."
    
    generations = list()
    
    game = seed(gridsize, number_of_seeds)
    generations.extend([game, nextgen(game)])
    
    epoch = 0
    game = nextgen(game)
    while sum(sum(game)) != False and comparegens(generations) == False and epoch < epochs:
        game = nextgen(game)
        generations.append(game)
        epoch += 1
    
    # showing converged states
    convergence = epoch
    if convergence < epochs:    
    	while  epoch < convergence+(epochs/10) and epoch < epochs:
        	game = nextgen(game)
        	generations.append(game)
        	epoch += 1
     
    i = 0
    for generation in generations:
        i += 1
        fig = plt.figure(figsize=(16,16))
        fig = showgame(generation, color_scheme)
        plt.savefig("gifs/life"+"0"*(3-len(str(i))) + str(i)+".png", dpi = 30)
        plt.close()  
    
    os.system("convert -delay 12 -loop 1 gifs/*.png gifs/Game_Of_Life-" + str(gridsize) + "_" + str(number_of_seeds) + "_" + str(epochs+2) + "_" + str(time.strftime("%Y%m%d%H%M%S")) + ".gif")
    os.system("rm gifs/*.png")

answer = "y"
while answer == "y" or answer == "Y":
    
    print "Make sure you are running this on anaconda python2!\n"
        
    color_scheme = int(input("Enter the color scheme (0 for RGB, 1 for grayscale): "))
    gridsize = int(input("Enter the grid size: "))
    number_of_seeds = int(input("Enter the seed amount: "))
    epochs  = int(input("Enter the number of epochs: "))

    life(gridsize, number_of_seeds, epochs, color_scheme)
    print"\nDone...! (check the gifs subfolder)"

    answer = raw_input("\nDo you wish to run Game Of Life again? (y,n): ")