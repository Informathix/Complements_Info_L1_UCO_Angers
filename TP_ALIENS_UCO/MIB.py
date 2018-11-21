# -*- coding: utf-8 -*-

import glob
# The glob module finds all the pathnames matching a specified pattern according to the rules used by the Unix shell
from pathlib import Path
# The final path component, without its suffix


mon_chemin = input('Quel est le chemin relatif du répertoire contenant les fichiers csv ?\n')
#"./MIB_Files/"

mon_alias = input('Alias du fichier py créé (sera ./MaBase_alias.py) ?\n')

mon_fic = "MaBase_%s.py" % mon_alias
 
mes_csv_file = {Path(f).stem:open(f,"r") for f in glob.glob(mon_chemin + "*.csv")}

mes_csv = {Path(f).stem:open(f,"r").readlines() for f in glob.glob(mon_chemin + "*.csv")}

mon_py = open(mon_fic,"w+")


def creer_classes():
    for b in mes_csv:
        mon_py.write("class " + b[4:-1] + ":\n\tdef __init__(self")
        lignes = mes_csv[b]
        attributs = lignes[0].split()[0].split(',')
        for a in attributs:
            mon_py.write(", " + a)
        mon_py.write("):\n\t\t")
        for a in attributs:
            mon_py.write("self.%s = %s\n\t\t" % (a,a))
        mon_py.write("\n\n")
        
            
def creer_bases():
    for b in mes_csv:
        nom = b[4:-1]
        mon_py.write(b + " = { ")
        lignes = mes_csv[b]
        for index,ligne in enumerate(lignes[1:]):
            ligne = ligne.split()[0].split(',')
            debut = '' if index == 0 else ', '
            mon_py.write(debut + nom + "(")
            for att in ligne[:-1]:
                mon_py.write("'" + att + "', ")
            mon_py.write("'" + ligne[-1] +"')")
        mon_py.write(" }\n\n")
        

def ferme():
    for b in mes_csv_file:
        mes_csv_file[b].close()
    mon_py.close()


creer_classes()
creer_bases()
ferme()
