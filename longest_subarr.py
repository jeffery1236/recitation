'''
Find the length of the longest subarr with sum less or equal to k
'''

def get_subarr_length(arr, k):
    '''
    # Maintain start and end pointer (inclusive)

    # Generate negative sum from the right
    neg_sums = [0]
    for i in range(n - 1, -1, -1):
        neg_sum = neg_sums[-1] + arr[i]
        if neg_sum > 0:
            neg_sums.append(0)
        else:
            neg_sums.append(neg_sum)


    start, end = 0, 0
    max_len = 0
    cur_sum = arr[0]

    while start < n and end < n:
        if end == (n-1) and end - start < max_len:
            break

        # if cur_sum + neg_sum[end] <= k -> still got hope, incr end
        # else no hope of longer viable subarr -> incr start

        if cur_sum <= k:


    '''
