# Sztuczne Neurony – Podstawowe Funkcje Logiki

To repozytorium zawiera implementacje prostych sztucznych neuronów (perceptronów) w Pythonie, imitujących podstawowe funkcje logiki: **NOT** i **OR**. Każdy przykład pokazuje działanie neuronu **bez uczenia** lub z prostą regułą uczenia.

## Zawartość repozytorium

- `NOT_bez_biasu.py` – Neuron MCP realizujący negację (NOT) bez biasu.
- `NOT_z_biasem.py` – Neuron MCP realizujący negację (NOT) z biasem.
- `OR.py` – Neuron MCP realizujący funkcję OR bez uczenia, z dwoma wejściami i biasem.
- `OR_z_uczeniem.py` – Perceptron prosty uczący się funkcji OR za pomocą reguły perceptronowej.
- `NOT_z_uczeniem.py` – Perceptron prosty uczący się funkcji NOT za pomocą reguły perceptronowej.

## Jak działają neurony

### ## 1. Neuron MCP (McCulloch-Pitts)

Neuron MCP oblicza wyjście na podstawie **sumy ważonej wejść**:
s = W1*X1 + W2*X2 + ... + Wn*Xn + b

- `Xi` – wartości wejściowe (0 lub 1)  
- `Wi` – wagi połączeń  
- `b` – bias (stałe pobudzenie neuronu)  
- `s` – suma ważona  

**Odpowiedź neuronu:**
Y = 1 jeśli s >= T, w przeciwnym razie Y = 0

- `T` – próg neuronu  

### ## 2. NOT bez biasu i z biasem

- **NOT bez biasu**: jedno wejście `X`, waga `W=-1`, próg `T=0`.  
- **NOT z biasem**: jedno wejście `X`, waga `W=-1`, bias `b=1`, próg `T=0.5`.  

**Tabela prawdy NOT:**

| X | Y |
|---|---|
| 0 | 1 |
| 1 | 0 |

### ## 3. OR bez uczenia

Neuron MCP z dwoma wejściami i biasem:

- Wagi: `W = [1, 1]`  
- Bias: `b = 0`  
- Próg: `T = 0.5`  

**Tabela prawdy OR:**

| X0 | X1 | Y |
|----|----|---|
| 0  | 0  | 0 |
| 0  | 1  | 1 |
| 1  | 0  | 1 |
| 1  | 1  | 1 |

### ## 4. Perceptron prosty z uczeniem (OR i NOT)

Dodaje możliwość **uczenia się wag** na podstawie zbioru przykładów.  

**Reguła uczenia (epoka uczenia):**
blad = Dk - Yk
b += eta * blad
Wi += eta * blad * Xi


- `Dk` – oczekiwana wartość wyjściowa  
- `Yk` – aktualna odpowiedź neuronu  
- `eta` – współczynnik uczenia (tutaj 1)  
- Wagi i bias aktualizowane są iteracyjnie, aż neuron nauczy się funkcji logicznej.

### ## 5. Tabele prawdy dla perceptronów uczących się

**NOT z uczeniem**

| X | Y |
|---|---|
| 0 | 1 |
| 1 | 0 |

**OR z uczeniem**

| X0 | X1 | Y |
|----|----|---|
| 0  | 0  | 0 |
| 0  | 1  | 1 |
| 1  | 0  | 1 |
| 1  | 1  | 1 |

## Instrukcja użycia

1. Skopiuj plik `.py` do swojego środowiska Python.  
2. Uruchom plik, aby zobaczyć wyniki dla wszystkich przypadków wejściowych.  
3. Dla perceptronów z uczeniem wywołuj `epoka_uczenia(X, D)` wielokrotnie, aż wagi się ustabilizują.  

 **Wskazówka:**  

- Bias (`b`) pozwala neuronowi wytworzyć wyjście 1 nawet, gdy wszystkie wejścia są zerowe.  
- Próg (`T`) decyduje, kiedy neuron "odpali" i zwróci 1.  
- Wagi (`W`) określają, jak mocno każde wejście wpływa na sumę ważoną.







