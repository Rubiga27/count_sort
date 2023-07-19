def countSort(A):
    max_val = max(A)
    count = [0] * (max_val + 1)

    for num in A:
        count[num] += 1

    cum_count = [0] * (max_val + 1)
    cum_count[0] = count[0]

    for i in range(1, max_val + 1):
        cum_count[i] = cum_count[i - 1] + count[i]

    sorted_arr = [0] * len(A)

    for num in reversed(A):
        pos = cum_count[num] - 1
        sorted_arr[pos] = num
        cum_count[num] -= 1

    return sorted_arr
A=list(map(int,input().split()))
print(countSort(A))


"""
Input 1:
A = [1, 3, 1]
Input 2:
A = [4, 2, 1, 3]


Output 1:
[1, 1, 3]
Output 2:
[1, 2, 3, 4]
"""
