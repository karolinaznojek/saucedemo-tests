\# Przypadki testowe — Logowanie (saucedemo.com)



\## TC-01: Logowanie problem\_user i uzupełnienie danych w checkout

\*\*Kroki:\*\*

1\. Zaloguj się jako problem\_user

2\. Dodaj produkt do koszyka

3\. Przejdź do checkout

4\. Wpisz First Name

5\. Wpisz Last Name



\*\*Oczekiwany wynik:\*\* Wszystkie pola formularza przyjmują wpisany tekst

\*\*Rzeczywisty wynik:\*\* BUG — pole Last Name nie przyjmuje wpisywanego tekstu



\---



\## TC-02: Logowanie z poprawnymi danymi

\*\*Kroki:\*\*

1\. Otwórz saucedemo.com

2\. Wpisz login: standard\_user

3\. Wpisz hasło: secret\_sauce

4\. Kliknij Login



\*\*Oczekiwany wynik:\*\* Użytkownik zostaje zalogowany i przekierowany do listy produktów

\*\*Rzeczywisty wynik:\*\* Zgodnie z oczekiwaniem ✅



\---



\## TC-03: Logowanie z błędnym hasłem

\*\*Kroki:\*\*

1\. Otwórz saucedemo.com

2\. Wpisz login: standard\_user

3\. Wpisz hasło: secret\_sauce1

4\. Kliknij Login



\*\*Oczekiwany wynik:\*\* Komunikat błędu: "Epic sadface: Username and password do not match any user in this service"

\*\*Rzeczywisty wynik:\*\* Zgodnie z oczekiwaniem ✅



\---



\## TC-04: Logowanie na zablokowane konto

\*\*Kroki:\*\*

1\. Otwórz saucedemo.com

2\. Wpisz login: locked\_out\_user

3\. Wpisz hasło: secret\_sauce

4\. Kliknij Login



\*\*Oczekiwany wynik:\*\* Komunikat błędu: "Epic sadface: Sorry, this user has been locked out."

\*\*Rzeczywisty wynik:\*\* Zgodnie z oczekiwaniem ✅

