# Program Rabin-Miller

Program o nazwie `rabinmiller` czyta plik `wejscie.txt` zawierający jeden, dwa lub trzy wiersze:
1. W pierwszym wierszu znajduje się liczba `n`.
2. Jeśli jest drugi wiersz, to zawiera on wykładnik uniwersalny, ułatwiający rozkład.
3. Jeśli jest trzeci wiersz, to wykładnikiem uniwersalnym jest iloczyn liczb w drugim i trzecim wierszu minus jeden.

## Wynik programu
Program zapisuje w pliku `wyjscie.txt` jedną z trzech wiadomości:
- „prawdopodobnie pierwsza” (jeśli prawdopodobieństwo, że liczba jest złożona jest mniejsze niż `2^−40`),
- „na pewno złożona”,
- lub liczbę będącą dzielnikiem liczby `n`.

## Opcja `-f`
Program wywołany z opcją `-f` dokonuje jedynie testu Fermata, tzn. bada jedynie ostatnią potęgę potencjalnego świadka pierwszości. W szczególności:
- Nie czyta dalszych wierszy w pliku wejściowym,
- Nie ma możliwości znalezienia rozkładu.

## Przykład testowy
Plik `wejscie.txt` zawierający liczby:
718548065973745507
3449
543546506135745129


Program powinien wyprodukować jeden z dwóch wyników:
740876531

lub
969862097


**Uwaga:** Iloczyn tych liczb wynosi `718548065973745507`. Podczas działania programu okaże się, że `576566739470926048` jest pierwiastkiem z 1 modulo `718548065973745507`.

## Test z liczbą Carmichaela
- Program wywołany z opcją `-f` **nie odkryje**, że `561` (liczba Carmichaela) jest liczbą złożoną.
- W pełnej wersji program odkryje, że `561 = 33 * 17`.