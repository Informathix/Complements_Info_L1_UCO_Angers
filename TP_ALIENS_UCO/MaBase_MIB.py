from dataclasses import dataclass

@dataclass(frozen=True)
class Cabine:
	NoCabine: str
	NoAllee: str
	
@dataclass(frozen=True)
class Gardien:
	Nom: str
	NoCabine: str
	
@dataclass(frozen=True)
class Responsable:
	NoAllee: str
	Nom: str
	
@dataclass(frozen=True)
class Miam:
	NomAlien: str
	Aliment: str
	
@dataclass(frozen=True)
class Alien:
	Nom: str
	Sexe: str
	Planete: str
	NoCabine: str
	
@dataclass(frozen=True)
class Agent:
	Nom: str
	Ville: str
	
BaseCabines = { Cabine('1', '1'), Cabine('2', '1'), Cabine('3', '1'), Cabine('4', '1'), Cabine('5', '1'), Cabine('6', '2'), Cabine('7', '2'), Cabine('8', '2'), Cabine('9', '2') }

BaseGardiens = { Gardien('Branno', '1'), Gardien('Darell', '2'), Gardien('Demerzel', '3'), Gardien('Seldon', '4'), Gardien('Dornick', '5'), Gardien('Hardin', '6'), Gardien('Trevize', '7'), Gardien('Pelorat', '8'), Gardien('Riose', '9') }

BaseResponsables = { Responsable('1', 'Seldon'), Responsable('2', 'Pelorat') }

BaseMiams = { Miam('Zorglub', 'Bortsch'), Miam('Blorx', 'Bortsch'), Miam('Urxiz', 'Zoumise'), Miam('Zbleurdite', 'Bortsch'), Miam('Darneurane', 'Schwanstucke'), Miam('Mulzo', 'Kashpir'), Miam('Zzzzzz', 'Kashpir'), Miam('Arghh', 'Zoumise'), Miam('Joranum', 'Bortsch') }

BaseAliens = { Alien('Zorglub', 'M', 'Trantor', '1'), Alien('Blorx', 'M', 'Euterpe', '2'), Alien('Urxiz', 'M', 'Aurora', '3'), Alien('Zbleurdite', 'F', 'Trantor', '4'), Alien('Darneurane', 'M', 'Trantor', '4'), Alien('Mulzo', 'M', 'Helicon', '6'), Alien('Zzzzzz', 'F', 'Aurora', '7'), Alien('Arghh', 'M', 'Nexon', '8'), Alien('Joranum', 'F', 'Euterpe', '9') }

BaseAgents = { Agent('Branno', 'Terminus'), Agent('Darell', 'Terminus'), Agent('Demerzel', 'Uco'), Agent('Seldon', 'Terminus'), Agent('Dornick', 'Kalgan'), Agent('Hardin', 'Terminus'), Agent('Trevize', 'Hesperos'), Agent('Pelorat', 'Kalgan'), Agent('Riose', 'Terminus') }

b = Agent('Riose', '2')
print(b)
