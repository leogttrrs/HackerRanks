
def encontrarIndicesSubstrings(texto, substring):
    indices = []
    inicio = 0
    while True:
        i = texto.find(substring, inicio)
        if i == -1:
            break
        indices.append(i)
        inicio = i + 1
    return indices

def gridSearch(G, P):
    for indexlinha, linha in enumerate(G):
        if P[0] in linha:
            indicesProcurados = encontrarIndicesSubstrings(linha, P[0])
            indicesCoincidentes = []
            for i in range(1, len(P)):
                if indexlinha + i < len(G) and P[i] in G[indexlinha + i]:
                    indicesAchados = encontrarIndicesSubstrings(G[indexlinha + i], P[i])
                    for indice in indicesAchados:
                        if indice in indicesProcurados:
                            indicesCoincidentes.append(indice)
                    for indiceCoincidente in indicesCoincidentes:
                        if indicesCoincidentes.count(indiceCoincidente) == len(P) - 1:
                            return "YES"
    return "NO"




print(gridSearch(["ab_ab", "cd_xx", "ef_ef"], ["ab", "cd", "ef"]))