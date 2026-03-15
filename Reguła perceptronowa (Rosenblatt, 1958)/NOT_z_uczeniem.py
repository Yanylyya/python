class perceptronProsty:
    def __init__(self):
        self.T = 0
        self.W = []
        self.b = 0

    def ustaw_prog(self, T):
        self.T = T

    def ustaw_wagi(self, W):
        self.W = W

    def ustaw_bias(self, b):
        self.b = b

    def suma_wazona(self, Xk):
        wynik = self.b
        for i in range(len(Xk)):
            wynik += Xk[i] * self.W[i]
        return wynik

    def odpowiedz(self, Xk):
        return 1 if self.suma_wazona(Xk) >= self.T else 0

    def epoka_uczenia(self, X, D):
        for i in range(len(X)):
            Xk = X[i]
            Dk = D[i]
            Yk = self.odpowiedz(Xk)
            blad = Dk - Yk
            self.b += blad
            for j in range(len(Xk)):
                self.W[j] += Xk[j] * blad


# --- Testowanie NOT ---
NOT_z_uczeniem = perceptronProsty()
NOT_z_uczeniem.ustaw_prog(0.5)
NOT_z_uczeniem.ustaw_wagi([0])
NOT_z_uczeniem.ustaw_bias(0)

X = [[0],[1]]
D = [1,0]  # oczekiwane wyniki NOT

# uczenie przez kilka epok
for epoka in range(5):
    NOT_z_uczeniem.epoka_uczenia(X,D)

# sprawdzenie wyników po uczeniu
print("\n=== NOT z uczeniem ===")
for Xk in X:
    print("X=", Xk, "Y=", NOT_z_uczeniem.odpowiedz(Xk))
print("Bias i wagi po uczeniu:", NOT_z_uczeniem.b, NOT_z_uczeniem.W)
