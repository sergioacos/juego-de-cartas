import random
class Baraja():
    def __init__(self):
        self.mazo = []
        self.monton = []
    def __str__(self):
        return print(f"{self.mazo}")
    def agregar_cartas(self, carta):
        for x in self.mazo:
            if x.palo == carta.palo and x.valor == carta.valor:
                raise Exception(" Carta existente")
        self.mazo.append(carta)
    def Barajar(self):
        #copia= list(self.mazo)
        random.shuffle(self.mazo)
    def Siguiente_carta(self):
        for x in (self.mazo):
            self.mazo.remove(x)
            self.monton.append(x)
            x.mostrar_carta()
            break
        #for x in (self.mazo):
    def Cartas_disponibles(self):
        print(f"Hay {len(self.mazo)} cartas en el mazo ")
    def Dar_cartas(self):
        dadas=0
        solicitadas=3
        while dadas != solicitadas:
            for x in (self.mazo):
                self.mazo.remove(x)
                self.monton.append(x)
                x.mostrar_carta()
                dadas+=1
                break
    def Cartas_Monton(self):
        if len(self.monton) == 0:
            print("Aun no han salido cartas")
        else:
            print("Las cartas que salieron son:")
            for x in (self.monton):
                x.mostrar_carta()
    def Mostar_baraja(self):
        if len(self.mazo)==0:
            print("No hay cartas en el mazo")
        else:
            print("Las cartas en el mazo son:")
            for x in self.mazo:
                x.mostrar_carta()
class carta():
    tipo_palo = ["basto", "espada", "copa", "oro"]
    tipo_valor = [1, 2, 3, 4, 5, 6, 7, 10, 11, 12, 13]

    def __init__(self, palo, valor):
        if palo not in self.tipo_palo:
            raise ValueError(f"{palo} no es un valor valido, debe selecionarse dentro de {self.tipo_palo}")
        elif valor not in self.tipo_valor:
            raise ValueError(f"{valor} no es un valor valido, debe selecionarse dentro de {self.tipo_valor}")
        else:
            self.valor = valor
            self.palo = palo
    def __str__(self):
        return print(f"{str(self.valor), self.palo}")
    def mostrar_carta(self):
        print(str(self.valor), self.palo)
mazo1 = Baraja()
carta1 = carta("basto",2)
carta2 = carta("basto",3)
carta3 = carta("espada",13)
carta4 = carta("espada",1)
carta5 = carta("oro",1)
#carta.mostrar_carta(carta1)
"""""
Baraja.agregar_cartas(mazo1)
Baraja.Cartas_disponibles(mazo1)
Baraja.Mostar_baraja(mazo1)
"""
mazo1.agregar_cartas(carta1)
mazo1.agregar_cartas(carta2)
mazo1.agregar_cartas(carta3)
mazo1.agregar_cartas(carta4)
mazo1.agregar_cartas(carta5)
mazo1.Cartas_disponibles()
mazo1.Mostar_baraja()
"""mazo1.Barajar()
mazo1.Mostar_baraja()
mazo1.Siguiente_carta()
mazo1.Mostar_baraja()
mazo1.Cartas_disponibles()"""
mazo1.Cartas_Monton()
mazo1.Dar_cartas()
mazo1.Mostar_baraja()
mazo1.Cartas_disponibles()
mazo1.Cartas_Monton()