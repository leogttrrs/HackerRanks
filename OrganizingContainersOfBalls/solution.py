# Complete the 'organizingContainers' function below.
# The function is expected to return a STRING.
# The function accepts 2D_INTEGER_ARRAY container as parameter.

def organizingContainers(arr):
    somas_containers = []
    somas_tipos = []
    colunas = zip(*arr)
    for coluna in colunas:
        somas_tipos.append(sum(coluna))
    somas_tipos.sort()

    for container in arr:
        somas_containers.append(sum(container))
    somas_containers.sort()

    for i in range(len(somas_tipos)):
        if somas_tipos[i] != somas_containers[i]:
            return 'Impossible'

    return 'Possible'