# -*- coding: utf-8 -*-

"""
Fichier permettant de créer, à partir de fichiers csv, des tables sous formes d'ensembles
contenant des objets créés sous forme de dataclass (i.e. ayant la structure d'enregistrement)
"""

import glob
"""
Le module glob permet de trouver tous les chemins en filtrant à l'aide d'expressions régulières
"""
from pathlib import Path
"""
Permet d'obtenir le nom du fichier sans l'extension
"""

mon_chemin = input('Quel est le chemin relatif du répertoire contenant les fichiers csv ?\n')
# eg ./MIB_Files/

mon_alias = input('Alias du fichier py créé (sera ./MaBase_alias.py) ?\n')
# eg MIB

mon_fic = "MaBase_%s.py" % mon_alias
 
mes_csv_file = {Path(f).stem:open(f,"r") for f in glob.glob(mon_chemin + "*.csv")}
"""
Les fichiers csv encapsulés 
"""

mes_csv = {Path(f).stem:open(f,"r").readlines() for f in glob.glob(mon_chemin + "*.csv")}
"""
Les fichiers csv sous forme de listes de chaque ligne donnée sous forme de chaîne de caractères
"""


mon_py = open(mon_fic,"w+")
"""
mon_py est le fichier python construit qui contiendra les tables
"""

mon_py.write('# -*- coding: utf-8 -*-\n"""\nModule généré automatiquement par le fichier MIB.py\nIl crée des tables sous forme d\'ensembles contenant des objets\ncréés sous forme de dataclass (i.e. ayant la structure d\'enregistrement)\n"""\n\nfrom dataclasses import dataclass\n\n')
"""
Crée l'en-tête du fichier python
"""

def creer_classes():
    """
    Crée les dataclasses avec la liste des attributs et leur type (str)
    Par exemple:

    @dataclass(frozen=True)
    class Cabine:
	NoCabine: str
	NoAllee: str
    """
    for b in mes_csv:
        mon_py.write("@dataclass(frozen=True)\nclass " + b[4:-1] + ":\n\t")
        lignes = mes_csv[b]
        attributs = lignes[0].split()[0].split(',')
        for a in attributs:
            mon_py.write("%s: str\n\t" % a)
        mon_py.write("\n")
        
            
def creer_bases():
    """
    Crée lees tables sous forme d'ensemble des éléments de chaque dataclass créée
    Par exemple:

    BaseResponsables = {
	Responsable('1', 'Seldon'),
	Responsable('2', 'Pelorat') 
    }
    """
    for b in mes_csv:
        nom = b[4:-1]
        mon_py.write(b + " = {\n\t")
        lignes = mes_csv[b]
        for index,ligne in enumerate(lignes[1:]):
            ligne = ligne.split()[0].split(',')
            debut = '' if index == 0 else ',\n\t'
            mon_py.write(debut + nom + "(")
            for att in ligne[:-1]:
                mon_py.write("'" + att + "', ")
            mon_py.write("'" + ligne[-1] +"')")
        mon_py.write(" \n}\n\n")
        

def ferme():
    """
    Ferme les fichiers csv encapsulés
    """
    for b in mes_csv_file:
        mes_csv_file[b].close()
    mon_py.close()


if __name__ == '__main__':
    """
    Lance les différentes fonctions créées 
    """
    creer_classes()
    creer_bases()
    ferme()
