
# Raport z Projektu: Generator Dźwięku na Zajęcia z Technik Multimedialnych
## Wprowadzenie
Celem tego projektu było stworzenie narzędzia, które generuje dźwięki na podstawie zdefiniowanych parametrów oraz listy nut, tworząc w ten sposób prostą melodię. Projekt wykorzystuje bibliotekę pyaudio do generowania dźwięków oraz bibliotekę numpy do obliczeń matematycznych potrzebnych do generacji różnych kształtów fali dźwiękowej.

## Opis Projektu
### Plik Wejściowy
Projekt pobiera informacje z pliku tekstowego song.txt, który zawiera zarówno definicje parametrów dźwięku, jak i sekwencję nut, które mają być zagrane. Plik tekstowy ma następującą strukturę:

- Parametry dźwięku: W postaci zmienna: wartość, gdzie zmienna to nazwa parametru, a wartość to jego wartość. Parametry obejmują attack, decay, sustain, release oraz wave.
- Nuty: Każda linia reprezentuje jedną nutę do zagrania.
Przykładowa zawartość pliku `song.txt`:

```
attack: 0.05
decay: 0.05
sustain: 0.5
release: 0.05
wave: triangle
C
E
G
A
F
```
### Klasa Sound
Klasa Sound jest odpowiedzialna za generowanie dźwięku na podstawie podanych parametrów. Klasa ta implementuje obwiednię ADSR (Attack, Decay, Sustain, Release) oraz różne typy fali dźwiękowej (sinusoidalna, kwadratowa, trójkątna, piłokształtna).

#### Metody Klasy Sound:
- `__init__`: Inicjalizuje obiekt dźwięku z podanymi parametrami.
- `play`: Generuje dźwięk o określonej częstotliwości, stosując obwiednię ADSR.
- `stop`: Kończy odtwarzanie dźwięku i pokazuje wygenerowaną falę dźwiękową.
- `_decay`: Wewnętrzna metoda pomocnicza do obsługi fazy decay.
### Klasa SoundWave
Klasa `SoundWave` jest odpowiedzialna za wizualizację wygenerowanej fali dźwiękowej przy użyciu biblioteki matplotlib.

### Enum Wave
Enum Wave definiuje różne typy fali dźwiękowej, które mogą być używane:

- SIN
- SQUARE
- TRIANGLE
- SAWTOOTH
### Zarządzanie Nutami
Nuty są zarządzane za pomocą słownika, gdzie klucze to nazwy nut, a wartości to odpowiadające im częstotliwości w Hz:

```
notes = {"C": 65.41,
         "D": 73.42,
         "E": 82.41,
         "F": 87.31,
         "G": 98.00,
         "A": 110.00,
         "B": 123.47}
```
### Przykład Użycia
Po wczytaniu parametrów i nut z pliku song.txt, program odtwarza melodię, stosując zdefiniowane parametry dźwięku. Każda nuta jest odtwarzana przez zadaną ilość czasu, po czym następuje przejście do kolejnej nuty.

Prezentacja
Poniżej znajduje się miejsce na filmik prezentujący działanie projektu. Filmik pokazuje proces odczytywania pliku song.txt, generowania dźwięków oraz wizualizacji fal dźwiękowych.



https://github.com/1grzyb1/syntezator-studia/assets/15954815/d74366f1-384a-4c3a-b753-9451c01c9f1f

