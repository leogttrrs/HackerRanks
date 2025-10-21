import requests


def getCompetitionWinnerByYear(competition: str, year: int):
    competitionsUrl = 'https://jsonmock.hackerrank.com/api/football_competitions'
    params = {
        'year': year,
        'name': competition,
    }
    try:
        response = requests.get(competitionsUrl, params=params)
        if response.status_code != 200:
            print("Error getting competitions info")
            return None

        data = response.json()
        results_list = data['data']

        if results_list:
            return results_list[0]['winner']
        else:
            print(f"Competição '{competition}' do ano {year} não encontrada.")
            return None

    except Exception as e:
        print(f'Erro na função getCompetitionWinnerByYear: {e}')
        return None

def fetch_all_matches(base_url: str, params: dict) -> list:
    current_page = 1
    total_pages = 1
    all_matches = []

    while current_page <= total_pages:
        params['page'] = current_page
        try:
            response = requests.get(base_url, params=params)
            if response.status_code != 200:
                print("Error getting matches info")
                break
            data = response.json()
            total_pages = data['total_pages']
            all_matches.extend(data['data'])
            current_page += 1
        except Exception as e:
            print('Loop error')
            break
    return all_matches


def getWinnerTotalGoals(competition: str, year: int) -> int:
    winner = getCompetitionWinnerByYear(competition, year)
    if not winner:
        print("Vencedor não encontrado, retornando 0.")
        return 0
    total_goals = 0

    baseUrl = 'https://jsonmock.hackerrank.com/api/football_matches'

    params = {
        'year': year,
        'competition': competition,
        'team1': winner,
    }
    team1matches = fetch_all_matches(baseUrl, params)
    for team1match in team1matches:
        total_goals += int(team1match['team1goals'])

    del params['team1']
    params['team2'] = winner
    team2matches = fetch_all_matches(baseUrl, params)

    for team2match in team2matches:
        total_goals += int(team2match['team2goals'])


    return total_goals




print(getWinnerTotalGoals('UEFA Champions League', 2015))