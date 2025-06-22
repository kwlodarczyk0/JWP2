# Jak uruchomić projekt lokalnie

Aby uruchomić projekt lokalnie wymagane jest posiadanie:

1. Python 3+
2. Lokalnej bazy danych postgres

    username: postgres

    password: postgres

    port:5432

    dbName: flask_db
    

Tworzenie środowiska virtualnego

1. python -m venv moj_env
2. moj_env\Scripts\activate
3. pip install-r requirements.txt
4. python app.py

Aplikacja uruchamia się domyślnie pod adresem localhost:5000

Aby przetestować działanie gry należy utworzyć 2 konta użytkowników oraz uruchomić aplikację na dwóch różnych przeglądarkach lub w trybie incognito



# Jak uruchomić projekt za pomocą dockera

Aby aplikacja działała prawidłowo wymagana jest również baza danych postgres dlatego samo stworzenie obrazu z pliku Dockerfile nie będzie wystarczające. W pliku docker-compose.yaml zdefinowane są wszystkie serwisy niezbędne do uruchomienia aplikacji tzn:
1. uruchomienie z parametrami zdefiniowanego pliku Dockerfile

2. pobranie bazy danych oraz jej inicjalizacja

3. Dodatkowo pobierany jest również pgAdmin - narzędzie za pomocą którego możemy połączyć się do bazy danych i ją administrować

Aby uruchomić proces należy użyć polecenia 

docker-compose up 

za pomocą którego zostanie zbudowana aplikacja wraz z bazą danych



