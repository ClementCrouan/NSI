import save as s

class Rewards:
    def __init__(self, fb, b) -> None:
        """Initialise les variables de la classe"""
        self.flashbacks = fb
        self.boussoles = b


    def add_flashbacks(self, nb) :
        """fonction qui prend en paramètre un entier nb, qui permet d'ajouter/enlever des flashbacks"""
        self.flashbacks += nb
        self.save()
        #enlever argent
    def add_boussoles(self, nb) :
        """fonction qui prend en paramètre un entier nb, qui permet d'ajouter/enlever des boussoles"""
        self.boussoles += nb
        self.save()
        #enlever argent
    def save(self):
        """Met à jour la base de donné lorsque une variable est modifié"""
        s.Save("money.csv").write([str(self.flashbacks), str(self.boussoles)])