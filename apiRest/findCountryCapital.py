import requests

def findCountryCapital(country: str):

    BASE_URL = "https://jsonmock.hackerrank.com/api/countries"
    query_params = {'name': country}

    try:
        response = requests.get(BASE_URL, params=query_params)

        if response.status_code == 200:
            data = response.json()
            results = data['data']
            print(results)
            if results:
                capital = data['data'][0]['capital']
                return capital
            else:
                print(f"País '{country}' não encontrado.")
                return None

        else:
            print(f"Erro na requisição: {response.status_code}")
            return None

    except requests.exceptions.RequestException as e:
        print(f"Erro de conexão: {e}")
        return None

capital_br = findCountryCapital('North Korea')
print(f"A capital do Brazil é: {capital_br}") # Saída: Brasília

print("-" * 20)

# 2. Teste do "edge case" (país não existe)
capital_fake = findCountryCapital('FakeCountry123')
print(f"A capital de FakeCountry123 é: {capital_fake}")