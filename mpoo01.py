class TV:
    def __init__(self):
        self.ligada = False
        self.canal = 1
        self.volume = 10

    def ligar(self):
        self.ligada = True
        print("A TV foi ligada.")

    def desligar(self):
        self.ligada = False
        print("A TV foi desligada.")

    def trocarCanal(self, numero):
        if self.ligada:
            self.canal = numero
            print(f"Canal alterado para {numero}.")
        else:
            print("A TV está desligada. Ligue-a antes de trocar o canal.")

    def aumentarVolume(self):
        if self.ligada and self.volume < 100:
            self.volume += 10
            print(f"Volume aumentado para {self.volume}.")
        elif self.ligada and self.volume == 100:
            print("Volume no máximo.")

    def diminuirVolume(self):
        if self.ligada and self.volume > 0:
            self.volume -= 10
            print(f"Volume diminuído para {self.volume}.")
        elif self.ligada and self.volume == 0:
            print("Volume no mínimo.")


minha_tv = TV()
minha_tv.ligar()
minha_tv.trocarCanal(9)
minha_tv.aumentarVolume()
minha_tv.aumentarVolume()
minha_tv.diminuirVolume()
minha_tv.diminuirVolume()
minha_tv.desligar()
minha_tv.diminuirVolume()

