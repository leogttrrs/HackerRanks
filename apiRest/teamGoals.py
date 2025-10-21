import requests
import json

def fetchAllPages(base_url, params):
    current_page = 1
    total_pages = 1
    all_matches = []

    while current_page <= total_pages:
        params['page'] = current_page
        try:
            response = requests.get(base_url, params=params)
            if response.status_code != 200:
                print(f'Erro na requisição (Página {current_page}): {response.status_code}')
                break
            data = response.json()
            total_pages = data['total_pages']
            matches_on_this_page = data['data']

            if not matches_on_this_page:
                break

            all_matches.extend(matches_on_this_page)
            current_page += 1

        except Exception as e:
            print(f"Erro no loop de paginação: {e}")
            break

    return all_matches


def findTeamGoalsInYear(teamName: str, year: int) -> int:
    BASE_URL = 'https://jsonmock.hackerrank.com/api/football_matches'
    total_goals = 0

    params_team1 = {
        'year': year,
        'team1': teamName
    }
    matches_as_team1 = fetchAllPages(BASE_URL, params_team1)

    for match in matches_as_team1:
        total_goals += int(match['team1goals'])

    params_team2 = {
        'year': year,
        'team2': teamName
    }
    matches_as_team2 = fetchAllPages(BASE_URL, params_team2)

    for match in matches_as_team2:
        total_goals += int(match['team2goals'])

    return total_goals

total = findTeamGoalsInYear('Barcelona', 2011)
print(f"Total de gols do Barcelona em 2011: {total}")
