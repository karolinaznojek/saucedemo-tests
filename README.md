# Saucedemo Tests — projekt testowy

Projekt demonstracyjny pokazujący moje podejście do testowania na przykładzie strony [saucedemo.com](https://www.saucedemo.com/).

## O projekcie

Przetestowałam funkcjonalność logowania oraz koszyka/checkout, wykorzystując różne konta testowe udostępnione przez stronę demonstracyjną (standard_user, locked_out_user, problem_user), żeby sprawdzić zarówno poprawne scenariusze, jak i przypadki błędów.

## Podsumowanie testów

- 8 przypadków testowych (logowanie, koszyk, checkout)
- 3 zidentyfikowane defekty
- 3 automatyczne testy w Playwright
- 3 testy API w Postmanie
- CI/CD: automatyczne uruchamianie testów przy każdym push (GitHub Actions)

## Zawartość

- [`test-cases.md`](./test-cases.md) — 8 przypadków testowych dla logowania oraz koszyka/checkout, w tym 3 zidentyfikowane defekty
- [`test_login.py`](./test_login.py) — 3 automatyczne testy w Playwright (Python), pokrywające scenariusze pozytywne i negatywne logowania
- [`JSONPlaceholder API Tests.postman_collection.json`](./JSONPlaceholder%20API%20Tests.postman_collection.json) — kolekcja testów API w Postmanie

## Jak uruchomić testy automatyczne

pip install pytest-playwright
playwright install
pytest test_login.py -v

## Testy API

Kolekcja testów API w Postmanie, testująca publiczne API [jsonplaceholder.typicode.com](https://jsonplaceholder.typicode.com/):
- Pobranie listy użytkowników
- Pobranie pojedynczego użytkownika
- Test negatywny — próba pobrania nieistniejącego użytkownika (weryfikacja kodu 404)

## Znalezione defekty

Podczas testów zidentyfikowałam 3 defekty, udokumentowane jako [GitHub Issues](https://github.com/karolinaznojek/saucedemo-tests/issues):

1. Pole "Last Name" w formularzu checkout nie przyjmuje wpisywanego tekstu (konto problem_user)
2. System pozwala złożyć zamówienie mimo pustego koszyka
3. Pole QTY w koszyku jest nieaktywne — nie można zmienić ilości produktu

## O mnie

Jestem testerką manualną z 3-letnim doświadczeniem w testowaniu systemów zintegrowanych w branży ubezpieczeniowej (testy funkcjonalne, regresyjne, integracyjne). Ten projekt to część mojego rozwoju w stronę szerszej praktyki testowej i podstaw automatyzacji.

[LinkedIn](https://linkedin.com/in/karolina-znojek-4240681b4)