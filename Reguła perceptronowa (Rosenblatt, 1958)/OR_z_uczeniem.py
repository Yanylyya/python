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

    # jedna epoka uczenia
    def epoka_uczenia(self, X, D):
        for i in range(len(X)):
            Xk = X[i]
            Dk = D[i]
            Yk = self.odpowiedz(Xk)
            blad = Dk - Yk
            self.b += blad
            for j in range(len(Xk)):
                self.W[j] += Xk[j] * blad


# --- Testowanie OR ---
OR_z_uczeniem = perceptronProsty()
OR_z_uczeniem.ustaw_prog(0.5)
OR_z_uczeniem.ustaw_wagi([0,0])
OR_z_uczeniem.ustaw_bias(0)

X = [[0,0],[0,1],[1,0],[1,1]]
D = [0,1,1,1]  # oczekiwane wyniki OR

# uczenie przez kilka epok
for epoka in range(10):
    OR_z_uczeniem.epoka_uczenia(X,D)

# sprawdzenie wyników po uczeniu
print("=== OR z uczeniem ===")
for Xk in X:
    print("X=", Xk, "Y=", OR_z_uczeniem.odpowiedz(Xk))
print("Bias i wagi po uczeniu:", OR_z_uczeniem.b, OR_z_uczeniem.W)
