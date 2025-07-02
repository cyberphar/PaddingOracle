"""Interface HTTP vers l’API cible."""
import requests

def query_oracle(url, data):
    response = requests.post(url, data=data)
    return response.status_code != 500  # Exemple simple : 500 = padding invalide
