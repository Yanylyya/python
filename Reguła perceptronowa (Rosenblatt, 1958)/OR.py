class neuronMCP:
    def ustaw_prog(self, T):
        self.T = T

    def ustaw_wagi(self, W):
        self.W = W

    def ustaw_bias(self, b):
        self.b = b

    def suma_wazona(self, Xk):
        wynik = 1 * self.b
        for i in range(len(Xk)):
            wynik += Xk[i] * self.W[i]
        return wynik

    def odpowiedz(self, Xk):
        return 1 if self.suma_wazona(Xk) >= self.T else 0

# Tworzymy obiekt neuronu OR
OR = neuronMCP()
OR.ustaw_prog(0.5)        # próg ustawiony na 0.5
OR.ustaw_wagi([1, 1])     # wagi dla obu wejść
OR.ustaw_bias(0)           # bias 0

# Testujemy wszystkie przypadki wejściowe OR
X = [[0, 0], [0, 1], [1, 0], [1, 1]]
for Xk in X:
    print('X=', Xk, 'Y=', OR.odpowiedz(Xk))
