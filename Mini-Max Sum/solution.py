def miniMaxSum(arr):
    total = sum(arr)
    print(f'{total-max(arr)} {total-min(arr)}')

miniMaxSum([1, 3, 5, 7, 9])