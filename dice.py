import random

def roll_two_d6() -> tuple[int, int]:
    # if seed:
    #     random.seed(seed)
    roll1 = random.randint(1, 6)
    roll2 = random.randint(1, 6)
    return (roll1 , roll2)

def is_bust(score: int) -> bool:
    return score > 100

def is_exact_100(score: int) -> bool :
    if score == 100:
        return "winner!"
    
def closer_to_target(a: int, b: int, target: int = 100) -> int |None:
    if a == b:
        return None
    sum_a = target - a
    sum_b = target - b
    if sum_a < sum_b:
        return 1
    if sum_a > sum_b:
        return 2
    
def tie_breaker() -> int :
    pass
    
def turn_decision(input_fn) -> str: 
    if input_fn == "r" or input_fn == "p":
        return input_fn
    else:
        while True:
            input_fn2 = input("enter p/r :")
            if input_fn2 != 'r' and input_fn2 != 'p':
                continue
            if input_fn2 == 'r':
                return input_fn2
            if input_fn2 == 'p':
                return input_fn2
            else:
                continue
                    
        
def play_game():
    arr1 = []
    arr2 = []
    while True:
        # dic_players = dict(player1_score = [], player2_score = [])
        
        print(arr1, arr2)
        player_1 = sum(roll_two_d6())
        arr1.append(player_1)
        if is_bust(sum(arr1)):
            print("player 1 is busted!!")
            break
        if is_exact_100(sum(arr1)) == "winner!":
            return "number 1 is the winner!!"
        ask_user1 = input("enter p/r :")
        if turn_decision(ask_user1) == 'r':
            continue
        elif ask_user1 == 'p':
            player_2 = sum(roll_two_d6())
            arr2.append(player_2)
            if is_bust(sum(arr2)):
                print("player 2 is busted!!")
                break
            if is_exact_100(sum(arr2)) == "winner!":
                return "number 2 is the winner!!"
            ask_user2 = input("enter p/r :")
            if ask_user2 == 'r':
                continue
            elif ask_user2 == 'p':
                if ask_user1 == 'p': 
                    closer_to = closer_to_target(sum(arr1), sum(arr2), 100)
                    print(arr1, arr2)
                    return f'player number {closer_to} is the winner!!!'
            else:
                continue
        
print(play_game())     
        
    
       
            
        
        
      
        
    

        
