"""Guess a number"""

import numpy as np

number = np.random.randint(1, 101) # random number is chosen

# Number of tries

count = 0

while True:
    
    count += 1
    predict_number = int(input("Guess a number from 1 to 100!\n"))
    
    if predict_number > number:
        print("Lower!")
        
    elif predict_number < number:
        print("Higher!")
    
    else:
        print(f"Congratulation! It was number {number}. You got it in {count} tries!")
        break # End of the game