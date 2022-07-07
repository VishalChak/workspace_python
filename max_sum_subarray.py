## Kadane’s Algorithm:

from sys import flags, maxsize


def max_sub_array_sum(arr):
    max_so_far = -maxsize-1
    max_ending_here = 0
    
    for val in arr:
        max_ending_here = max_ending_here + val
        
        if max_so_far < max_ending_here:
            max_so_far = max_ending_here
        if max_ending_here < 0 :
            max_ending_here = 0
            max_sub_array = [val]
    
    return max_so_far


if __name__ == "__main__":
    arr = [-2, -3, 4, -1, -2, 1, 5, -3]
    print(max_sub_array_sum(arr))