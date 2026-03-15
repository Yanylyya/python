class neuronMCP:
    def __init__(self):
        self.T = 0    # próg
        self.W = []   # waga

    def ustaw_prog(self, T):
        self.T = T

    def ustaw_wagi(self, W):
        self.W = W

    def suma_wazona(self, Xk):

        return Xk[0] * self.W[0]

    def odpowiedz(self, Xk):
        return 1 if self.suma_wazona(Xk) >= self.T else 0


NOT_bez_biasu = neuronMCP()
NOT_bez_biasu.ustaw_prog(0)        # próg = 0
NOT_bez_biasu.ustaw_wagi([-1])     # waga -1 dla NOT

print("X=1 -> Y=", NOT_bez_biasu.odpowiedz([1]))  # oczekiwane 0
print("X=0 -> Y=", NOT_bez_biasu.odpowiedz([0]))  # oczekiwane 1
