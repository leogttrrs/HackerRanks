# Complete the 'buildPalindrome' function below.
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING a
#  2. STRING b

def buildPalindrome(a, b):
    palindromos = []
    for ia in range(len(a)):
        for j in range(ia + 1, len(a) + 1):
            substringA = a[ia:j]

            for ib in range(len(b)):
                for jb in range(ib + 1, len(b) + 1):
                    substringB = b[ib:jb]
                    candidato = substringA + substringB

                    if candidato == candidato[::-1]:
                        palindromos.append(candidato)

    if not palindromos:
        return '-1'
    else:
        maiorTamanho = 0
        indicemaior = 0
        for i, palindromo in enumerate(palindromos):
            if len(palindromo) > maiorTamanho:
                maiorTamanho = len(palindromo)
                indicemaior = i
            if len(palindromo) == maiorTamanho:
                if palindromo < palindromos[indicemaior]:
                    indicemaior = i
        return palindromos[indicemaior]



print(buildPalindrome('w', 'd'))


