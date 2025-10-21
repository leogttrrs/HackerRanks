import requests
import json

def findTeamGoalsInYear(teamName: str, year: int) -> int:
    BASE_URL = 'https://jsonmock.hackerrank.com/api/football_matches'
    total_goals = 0

    current_page = 1
    total_pages = 1

    while current_page <= total_pages:
        query_params = {
            'year': year,
            'page': current_page,
            'team1': teamName,
        }
        try:
            response = requests.get(BASE_URL, params=query_params)
            if response.status_code == 200:
                data = response.json()
                total_pages = data['total_pages']
                for match in data['data']:
                    print(match)
                    total_goals += int(match['team1goals'])
                current_page += 1
            else:
                print(f'Erro na busca de team1 (Página {current_page}): {response.status_code}')
                break
        except Exception as e:
            print(e)
            break

    current_page = 1
    total_pages = 1
    while current_page <= total_pages:
        query_params = {
            'year': year,
            'page': current_page,
            'team2': teamName,
        }
        try:
            response = requests.get(BASE_URL, params=query_params)
            if response.status_code == 200:
                data = response.json()
                total_pages = data['total_pages']
                for match in data['data']:
                    print(match)
                    total_goals += int(match['team2goals'])
                current_page += 1
            else:
                print(f'Erro na busca de team2 (Página {current_page}): {response.status_code}')
                break
        except Exception as e:
            print(e)
            break

    return total_goals


print(findTeamGoalsInYear('Barcelona', 2011))