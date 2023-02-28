"""Guess a number
A computer imagines a number and tries to find out which one, within 20 tries"""

import numpy as np

def random_predict(number: int = 1)->int:
    """random number prediction

    Args:
        number (int, optional): supposed number. Defaults to 1.

    Returns:
        int: Number of tries
    """
    count = 0
    
    lower_limit = 1
    upper_limit = 101
    
    while True:
        
        count += 1
        predict_number = np.random.randint(lower_limit, upper_limit)
        
        if predict_number == number:
            break
        
        elif predict_number < number:
            lower_limit = predict_number
        
        else:
            upper_limit = predict_number
            
    return(count)

def game_score(random_predict)->int:
    """average number of tries after 1000 rounds

    Args:
        random_predict (_type_): guessing function

    Returns:
        int: average number of tries
    """
    count_ls = []
    np.random.seed(1)
    random_array = np.random.randint(1, 101, size = (1000)) 

    for number in random_array:
        count_ls.append(random_predict(number))
        
    score = int(np.mean(count_ls))
    print(f"Your algorhytm needs in average {score} tries.")
    return score

if __name__ == "__main__": 
    game_score(random_predict)
      
    
