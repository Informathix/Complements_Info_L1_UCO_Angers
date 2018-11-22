class Responsable:
        def __init__(self, NoAllee, Nom):
                self.NoAllee = NoAllee
                self.Nom = Nom
                
 
class Miam:
        def __init__(self, NomAlien, Aliment):
                self.NomAlien = NomAlien
                self.Aliment = Aliment
                
 
class Agent:
        def __init__(self, Nom, Ville):
                self.Nom = Nom
                self.Ville = Ville
                
 
class Gardien:
        def __init__(self, Nom, NoCabine):
                self.Nom = Nom
                self.NoCabine = NoCabine
                
 
class Alien:
        def __init__(self, Nom, Sexe, Planete, NoCabine):
                self.Nom = Nom
                self.Sexe = Sexe
                self.Planete = Planete
                self.NoCabine = NoCabine
                
 
class Cabine:
        def __init__(self, NoCabine, NoAllee):
                self.NoCabine = NoCabine
                self.NoAllee = NoAllee
                
 
BaseResponsables = { Responsable('1', 'Seldon'), Responsable('2', 'Pelorat') }
 
BaseMiams = { Miam('Zorglub', 'Bortsch'), Miam('Blorx', 'Bortsch'), Miam('Urxiz', 'Zoumise'), Miam('Zbleurdite', 'Bortsch'), Miam('Darneurane', 'Schwanstucke'), Miam('Mulzo', 'Kashpir'), Miam('Zzzzzz', 'Kashpir'), Miam('Arghh', 'Zoumise'), Miam('Joranum', 'Bortsch') }
 
BaseAgents = { Agent('Branno', 'Terminus'), Agent('Darell', 'Terminus'), Agent('Demerzel', 'Uco'), Agent('Seldon', 'Terminus'), Agent('Dornick', 'Kalgan'), Agent('Hardin', 'Terminus'), Agent('Trevize', 'Hesperos'), Agent('Pelorat', 'Kalgan'), Agent('Riose', 'Terminus') }
 
BaseGardiens = { Gardien('Branno', '1'), Gardien('Darell', '2'), Gardien('Demerzel', '3'), Gardien('Seldon', '4'), Gardien('Dornick', '5'), Gardien('Hardin', '6'), Gardien('Trevize', '7'), Gardien('Pelorat', '8'), Gardien('Riose', '9') }
 
BaseAliens = { Alien('Zorglub', 'M', 'Trantor', '1'), Alien('Blorx', 'M', 'Euterpe', '2'), Alien('Urxiz', 'M', 'Aurora', '3'), Alien('Zbleurdite', 'F', 'Trantor', '4'), Alien('Darneurane', 'M', 'Trantor', '4'), Alien('Mulzo', 'M', 'Helicon', '6'), Alien('Zzzzzz', 'F', 'Aurora', '7'), Alien('Arghh', 'M', 'Nexon', '8'), Alien('Joranum', 'F', 'Euterpe', '9') }
 

BaseCabines = { Cabine('1', '1'), Cabine('2', '1'), Cabine('3', '1'), Cabine('4', '1'), Cabine('5', '1'), Cabine('6', '2'), Cabine('7', '2'), Cabine('8', '2'), Cabine('9', '2') }

