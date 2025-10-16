#The function should print the result, not return

def miniMaxSum(arr):
    total = sum(arr)
    print(f'{total-max(arr)} {total-min(arr)}')