class Heat_calculator:

    def __init__(self, lista):
        self.lista = lista
        self.ceo = self.heat_transfer_coefficient_k()
        self.heat = round(lista[5] * self.ceo * (lista[3] - lista[2]), 2)

    def __str__(self):
        return f"Ucieka Ci {self.heat} [W] ciepła..."

    def calculate_resistance(self):
        outside = {
            # materiał: [λ [W/mK], grubosc [m]]
            "cegła pełna": [0.77, 0.12],
            "cegła kratówka": [0.56, 0.12],
            "cegła dziurawka": [0.62, 0.12],
            "pustak ceramiczny": [0.31, 0.25]
            }
        inside = {
            # materiał: [λ [W/mK]]
            "wełna mineralna": "0.032",
            "styropian": "0.035"
            }

        grub_zew = outside[self.lista[0]][1]
        lambda_zew = outside[self.lista[0]][0]
        grub_wew = self.lista[4] - outside[self.lista[0]][1]
        lambda_wew = float(inside[self.lista[1]])
        r = (grub_wew/lambda_wew) + (grub_zew/lambda_zew)
        return r

    def heat_transfer_coefficient_k(self):
        r = self.calculate_resistance()
        coe_a1 = 7.692
        coe_a2 = 25
        coe_k = 1/((1/coe_a1) + r + (1/coe_a2))
        return coe_k

    @property
    def lista(self):
        return self._lista
    
    @lista.setter
    def lista(self, lista):
        self._lista = lista
