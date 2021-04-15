#assumptions- all inputs are solvable for the code
#set of numebers given can be used multiple times

int_array = [ ]
target_int = 0

def solve_sum(int_array, target_int, index_list):
    # if the target_int hits zero, then we've found our solution
    if target_int == 0 and 0 not in int_array:
        return index_list
    elif target_int == 0 and 0 in int_array:
        return [int_array.index(0)]
    if target_int < 0:
        return 0
    
    largest_index = len(int_array)-1

    while sorted_int_array[largest_index] > target_int:
        largest_index -= 1
        print(largest_index, "line 36", target_int)
        if largest_index <= 0 and sorted_int_array[largest_index] != target_int :
            return 0
        
    largest_int = sorted_int_array[largest_index]
    new_target_int = target_int - largest_int
    
    return solve_sum(sorted_int_array[:largest_index], new_target_int, index_list+[largest_index]) or \
          solve_sum(sorted_int_array[:largest_index-1], new_target_int, index_list+[largest_index]) or \
          solve_sum(sorted_int_array[:len(int_array)-1], target_int, index_list) # NEW 
        

sorted_int_array = sorted(int_array)

index_map = {}
used_index_array = [] # NEW
for i in range(len(sorted_int_array)):
    for j in range(len(sorted_int_array)):
        if int_array[j] == sorted_int_array[i] and j not in used_index_array: # NEW
            index_map[i] = j
            used_index_array.append(j) # NEW
            break # NEW 

sorted_indices = solve_sum(sorted_int_array, target_int, [])

try:
    unsorted_indices = list(map(lambda index: index_map[index], sorted_indices))
except KeyError:
    print('No solution')
else:
    print(unsorted_indices)