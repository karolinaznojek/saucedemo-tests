\# Saucedemo Tests — projekt testowy



Projekt demonstracyjny pokazujący moje podejście do testowania manualnego na przykładzie strony \[saucedemo.com](https://www.saucedemo.com/).



\## O projekcie



Przetestowałam funkcjonalność logowania, wykorzystując różne konta testowe udostępnione przez stronę demonstracyjną (standard\_user, locked\_out\_user, problem\_user), żeby sprawdzić zarówno poprawne scenariusze, jak i przypadki błędów.



## Zawartość

- [`test-cases.md`](./test-cases.md) — 4 przypadki testowe dla funkcjonalności logowania, w tym jeden zidentyfikowany defekt
- [`test_login.py`](./test_login.py) — 3 automatyczne testy w Playwright (Python), pokrywające scenariusze pozytywne i negatywne logowania

## Jak uruchomić testy automatyczne

```
pip install pytest-playwright
playwright install
pytest test_login.py -v
```


## Testy API

Dodatkowo przygotowałam kolekcję testów API w Postmanie ([`JSONPlaceholder API Tests.postman_collection.json`](./JSONPlaceholder%20API%20Tests.postman_collection.json)), testującą publiczne API [jsonplaceholder.typicode.com](https://jsonplaceholder.typicode.com/):
- Pobranie listy użytkowników
- Pobranie pojedynczego użytkownika
- Test negatywny — próba pobrania nieistniejącego użytkownika (weryfikacja kodu 404)



\## O mnie


Jestem testerką manualną z 3-letnim doświadczeniem w testowaniu systemów zintegrowanych w branży ubezpieczeniowej (testy funkcjonalne, regresyjne, integracyjne). Ten projekt to część mojego rozwoju w stronę szerszej praktyki testowej i podstaw automatyzacji.



\[LinkedIn](https://linkedin.com/in/karolina-znojek-4240681b4)

