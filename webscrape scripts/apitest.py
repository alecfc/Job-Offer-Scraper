import requests

shots_url = 'https://content.linkit.nl/vacancies?'

# request the URL and parse the JSON
response = requests.get(shots_url)
response.raise_for_status() # raise exception if invalid response
shots = response.json()['resultSets'][0]['rowSet']

# do whatever we want with the shots data
do_things(shots)