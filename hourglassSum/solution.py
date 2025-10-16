# Complete the 'hourglassSum' function below.
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.

def hourglassSum(arr):
    somas = []
    for ilinha, linha in enumerate(arr[1:-1], start=1):
        for icoluna, numero in enumerate(linha[1:-1], start=1):
            soma = 0

            soma += numero

            soma += arr[ilinha - 1][icoluna - 1]
            soma += arr[ilinha - 1][icoluna]
            soma += arr[ilinha - 1][icoluna + 1]

            soma += arr[ilinha + 1][icoluna - 1]
            soma += arr[ilinha + 1][icoluna]
            soma += arr[ilinha + 1][icoluna + 1]

            somas.append(soma)
    return (max(somas))