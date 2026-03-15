class neuronMCP:
    def __init__(self):
        self.T = 0       # próg
        self.W = []      # wagi
        self.b = 0       # bias

    def ustaw_prog(self, T):
        self.T = T

    def ustaw_wagi(self, W):
        self.W = W

    def ustaw_bias(self, b):
        self.b = b

    def suma_wazona(self, Xk):
        return self.b * 1 + Xk[0] * self.W[0]

    def odpowiedz(self, Xk):
        return 1 if self.suma_wazona(Xk) >= self.T else 0


NOT_z_biasem = neuronMCP()
NOT_z_biasem.ustaw_prog(0.5)
NOT_z_biasem.ustaw_wagi([-1])
NOT_z_biasem.ustaw_bias(1)

print("X=1 -> Y=", NOT_z_biasem.odpowiedz([1]))  # oczekiwane 0
print("X=0 -> Y=", NOT_z_biasem.odpowiedz([0]))  # oczekiwane 1
