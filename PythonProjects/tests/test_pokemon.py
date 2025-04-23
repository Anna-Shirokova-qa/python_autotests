import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'eb42704be5c15a2168a34e7da727e6b9'
HEADER = {'Content-Type':'application/json','trainer_token': TOKEN}
TRAINER_ID = '30255'

def test_status_code():
    response = requests.get(url = f'{URL}/trainers', params = {'trainer_id' : TRAINER_ID})
    assert response.status_code == 200

def test_trainer_name():
    response_get = requests.get(url = f'{URL}/trainers', params = {'trainer_id' : TRAINER_ID})
    assert response_get.json()['data'][0]['trainer_name'] == 'Тренер'
      