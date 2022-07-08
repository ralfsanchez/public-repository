social_graph = {
    "@bongolpoc":{"first_name":"Joselito",
                  "last_name":"Olpoc",
                  "following":[
                  ]
    },
    "@joaquin":  {"first_name":"Joaquin",
                  "last_name":"Gonzales",
                  "following":[
                      "@chums","@jobenilagan"
                  ]
    },
    "@chums" : {"first_name":"Matthew",
                "last_name":"Uy",
                "following":[
                    "@bongolpoc","@miketan","@rudyang","@joeilagan"
                ]
    },
    "@jobenilagan":{"first_name":"Joben",
                   "last_name":"Ilagan",
                   "following":[
                    "@eeebeee","@joeilagan","@chums","@joaquin"
                   ]
    },
    "@joeilagan":{"first_name":"Joe",
                  "last_name":"Ilagan",
                  "following":[
                    "@eeebeee","@jobenilagan","@chums"
                  ]
    },
    "@eeebeee":  {"first_name":"Elizabeth",
                  "last_name":"Ilagan",
                  "following":[
                    "@jobenilagan","@joeilagan"
                  ]
    },
}

def relationship_status(from_member, to_member, social_graph):

    
    #Statement1: from_member follows to_member
    hypothesis1 = to_member in social_graph[from_member]["following"]
    #Statement2: to_member follows from_member
    hypothesis2 = from_member in social_graph[to_member]["following"]

    if hypothesis1==0 and hypothesis2==0:
        return("no relationship")
    elif hypothesis1==0 and hypothesis2==1:
        return("followed by")
    elif hypothesis1==1 and hypothesis2==0:
        return("follower")
    elif hypothesis1==1 and hypothesis2==1:
        return("friends")
    
#Question 2

board1 = [
['X','X','O'],
['O','X','O'],
['O','','X'],
]

board2 = [
['X','X','O'],
['O','X','O'],
['','O','X'],
]

board3 = [
['O','X','O'],
['','O','X'],
['X','X','O'],
]

board4 = [
['X','X','X'],
['O','X','O'],
['O','','O'],
]

board5 = [
['X','X','O'],
['O','X','O'],
['X','','O'],
]

board6 = [
['X','X','O'],
['O','X','O'],
['X','',''],
]

board7 = [
['X','X','O',''],
['O','X','O','O'],
['X','','','O'],
['O','X','','']
]

def tic_tac_toe(board):

    #Conditions for winning
    x_wins=['X']*len(board)
    o_wins=['O']*len(board)
    
    #Get all possible line combinations (horizontal,diagonal,vertical) 
    #Add in list
    first_diagonal = []
    second_diagonal = []
    row = []
    combinations = []
    
    #Get horizontal line combinations and add to combinations list
    for i in board:
        combinations.append(i)
    
    #Get first_diagonal line combinations 
    i = 0
    while i < len(board):
        first_diagonal.append(board[i][i])
        i+=1
    combinations.append(first_diagonal)
    
    #Get second_diagonal line combinations
    i=0
    j=2

    while i < len(board):
        second_diagonal.append(board[i][j])
        i+=1
        j-=1
    combinations.append(second_diagonal)
    
    #Get vertical line combinations
    for i in board:
        row.extend(i)
    for i in range(len(board)):
        combinations.append(row[i::len(board)])
        
    #After getting all combinations, output result
    if x_wins in combinations:
        winner_chicken_dinner = 'X'
    elif o_wins in combinations:
        winner_chicken_dinner = 'O'
    else:
        winner_chicken_dinner = 'No winner'
        
    return winner_chicken_dinner

#Question 3

legs = {
     ("upd","admu"):{
         "travel_time_mins":10
     },
     ("admu","dlsu"):{
         "travel_time_mins":35
     },
     ("dlsu","upd"):{
         "travel_time_mins":55
     }
}

legs = {
    ('a1', 'a2'): {
        'travel_time_mins': 10
    },
    ('a2', 'b1'): {
        'travel_time_mins': 10230
    },
    ('b1', 'a1'): {
        'travel_time_mins': 1
    }
}

#3-Not Finished

legs = {
     ("upd","admu"):{
         "travel_time_mins":10
     },
     ("admu","dlsu"):{
         "travel_time_mins":35
     },
     ("dlsu","upd"):{
         "travel_time_mins":55
     }
}

legs = {
    ('a1', 'a2'): {
        'travel_time_mins': 10
    },
    ('a2', 'b1'): {
        'travel_time_mins': 10230
    },
    ('b1', 'a1'): {
        'travel_time_mins': 1
    }
}

def eta(first_stop, second_stop, route_map):

    #Code
    current_place = first_stop
    total_time = 0
    
    #Stop until current_place reaches the second-stop
    while current_place != second_stop:
        
        for i in route_map:
            if current_place == i[0]:
                current_place = i[1]
                total_time += route_map[i]["travel_time_mins"]
                break
    return total_time
