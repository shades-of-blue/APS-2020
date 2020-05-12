def find_max_subarray(alist, start, end):
    max_ending_at_i = max_seen_so_far = alist[start]
    max_left_at_i = max_left_so_far = start
    max_right_so_far = start + 1
    for i in range(start + 1, end):
        if max_ending_at_i > 0:
            max_ending_at_i += alist[i]
        else:
            max_ending_at_i = alist[i]
            max_left_at_i = i
        if max_ending_at_i > max_seen_so_far:
            max_seen_so_far = max_ending_at_i
            max_left_so_far = max_left_at_i
            max_right_so_far = i + 1
    return max_left_so_far, max_right_so_far, max_seen_so_far

# number of elements 
n = int(input())  
# Below line read inputs from user using map() function  
a = list(map(int,input().strip().split()))[:n]
start, end, maximum = find_max_subarray(a, 0, len(a))
print(maximum)
del a[start:end]
try:
    st,en,maxi=find_max_subarray(a, 0, len(a))
    print(maxi)
except:
    print('0')