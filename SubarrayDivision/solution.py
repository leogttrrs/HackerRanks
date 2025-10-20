# Complete the 'birthday' function below.
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY s
#  2. INTEGER d
#  3. INTEGER m

def birthday(s, d, m):
    resultados = 0
    for i in range(len(s) - m + 1):
        if sum(s[i:i+m]) == d:
            resultados += 1
    return resultados
