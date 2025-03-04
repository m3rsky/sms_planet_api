import requests
from definition import api_key, password

def send_message(**kwargs):
    url = "https://api2.smsplanet.pl/sms"
    params = {
        'key': kwargs.get('api_key', ''),
        'password': kwargs.get('password', ''),
        'from': kwargs.get('sender_name', ''),
        'to': kwargs.get('number', ''),
        'msg': kwargs.get('message', ''),
        'test': 0,
        'subject': kwargs.get('subject', ''),
        'attachment': kwargs.get('attachment', '')
    }

    try:
        response = requests.post(url, data=params)
        response.raise_for_status()  # Sprawdza, czy nie było błędu HTTP
        return response.text
    except requests.exceptions.RequestException as e:
        return f"Błąd podczas wysyłania wiadomości: {e}"
    

message = "Przykładowy tekst wiadomości"
number = "788888888"

response = send_message(
    api_key=api_key,
    password=password,
    message=f"{message}",
    sender_name='Test',
    number=number,
)

print(f'Odpowiedź serwera: {response}')