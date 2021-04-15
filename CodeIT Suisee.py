#assumptions- all inputs are solvable for the code
#set of numebers given can be used multiple times


import time

int_array = [1,2,6,3,17,82,23,234]
target_int = 26

def solve_sum(int_array, target_int, index_list):
    # if the target_int hits zero, then we've found our solution
    if target_int == 0:
        return index_list
    if target_int < 0:
        return 0
    
    largest_index = len(int_array)-1
    
    while sorted_int_array[largest_index] > target_int :
        largest_index -= 1
        
        largest_int = sorted_int_array[largest_index]
        new_target_int = target_int - largest_int

  
    
    
        
    return solve_sum(sorted_int_array[:largest_index], new_target_int, index_list+[largest_index]) or \
          solve_sum(sorted_int_array[:largest_index-1], new_target_int, index_list+[largest_index])
        

sorted_int_array = sorted(int_array)

index_map = {}
used_index_array = []
for i in range(len(sorted_int_array)):
    for j in range(len(sorted_int_array)):
        if int_array[j] == sorted_int_array[i] :
            index_map[i] = j
            

            
# index_map = {i: j for i in range(len(sorted_int_array)) for j in range(len(sorted_int_array)) if int_array[j] == sorted_int_array[i]}
sorted_indices = solve_sum(sorted_int_array, target_int, [])

try:
    unsorted_indices = list(map(lambda index: index_map[index], sorted_indices))
except KeyError:
    print('No solution')
else:
    print(unsorted_indices)

