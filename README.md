# Automatyczne wysyłanie SMS-ów z SMSPlanet API

## 📌 Opis
Ten projekt umożliwia wysyłanie wiadomości SMS za pomocą API serwisu **SMSPlanet**. Program wykorzystuje bibliotekę `requests` do wysyłania żądań HTTP `POST`, co pozwala na automatyczne powiadomienia SMS.

## ⚙ Funkcjonalności
- Wysyłanie SMS na wskazany numer telefonu.
- Obsługa autoryzacji poprzez API Key i hasło.
- Obsługa błędów podczas wysyłania wiadomości.

## 🛠 Wymagania
Przed uruchomieniem upewnij się, że masz zainstalowaną bibliotekę `requests`. Możesz ją zainstalować komendą:
```sh
pip install requests
```

Dodatkowo, należy utworzyć plik `definition.py` i dodać do niego dane logowania do API:
```python
api_key = "TWÓJ_KLUCZ_API"
password = "TWOJE_HASŁO"
```

## 🚀 Instalacja i uruchomienie
1. Sklonuj repozytorium:
   ```sh
   git clone https://github.com/twoj-projekt.git](https://github.com/m3rsky/sms_planet_api.git)
   cd twoj-projekt
   ```
2. Zainstaluj wymagane biblioteki:
   ```sh
   pip install -r requirements.txt
   ```
3. Uruchom program:
   ```sh
   python main.py
   ```

## 📜 Kod programu
```python
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
        response.raise_for_status()
        return response.text
    except requests.exceptions.RequestException as e:
        return f"Błąd podczas wysyłania wiadomości: {e}"

message = "Przykładowy tekst wiadomości"
number = "788888888"

response = send_message(
    api_key=api_key,
    password=password,
    message=message,
    sender_name='Test',
    number=number,
)

print(f'Odpowiedź serwera: {response}')
```

## 📌 Przykładowe wyjście
```
Odpowiedź serwera: OK
```
