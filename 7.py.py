def maxScore(cardpoints, k):
    total_sum = sum(cardpoints)
    window_size = len(cardpoints) - k 
    min_subarray_sum = float('inf')
    current_window_sum = 0
    
    for i in range(window_size):
        current_window_sum += cardpoints[i]
    min_subarray_sum = current_window_sum
    
    for i in range(window_size, len(cardpoints)):
        current_window_sum += cardpoints[i] - cardpoints[i - window_size]
        min_subarray_sum = min(min_subarray_sum, current_window_sum)
    return total_sum - min_subarray_sum
     

cardpoints1 = [1,2,3,4,5,6,11]
k1 = 3
print(maxScore(cardpoints1,k1))
 