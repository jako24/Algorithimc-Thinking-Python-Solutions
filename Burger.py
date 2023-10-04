def burger_max(m, n, t):
    # Initialize the values
    max_burgers_count = 0
    reamining_time = t
    
    #Check all the combinations 
    for i in range(t//m + 1): # number of m burgers
        for j in range(t//n + 1): # number of n burgers 
            total_time = i*m + j*n 
            if total_time <= t: 
                if i + j > max_burgers_count:
                    max_burgers_count = i + j 
                    reamining_time = t - total_time
                    
    return max_burgers_count, reamining_time

# Read input and display time in minutes 
try: 
    while True: 
        m,n,t = map(int, input().split())
        burgers, beer_time = burger_max(m,n,t)
        if beer_time: 
            print(burgers, beer_time)
        else: 
            print(burgers)
except EOFError: 
    pass