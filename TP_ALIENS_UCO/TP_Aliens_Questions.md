Apres avoir cliqué sur la version [RAW](https://raw.githubusercontent.com/Informathix/Complements_Info_L1_UCO_Angers/master/TP_ALIENS_UCO/MaBase_MIB.py) du fichier `MaBase_MIB.py` présent sur ce répertoire, enregistrez-le sur votre répertoire personnel distant (sur github) et sur votre propre machine. 

Répondez ensuite aux questions suivantes en utilisant le fichier MaBase_MIB.py (des réponses sont donnéespour vous aider).
Pour cela créez un fichier MIB_exos.py qui commencera ainsi:

```python
# -*- coding: utf-8 -*-

from MaBase_MIB import *

### Question 1 : quel est l'ensemble des gardiens?
les_gardiens = {gardien.Nom for gardien in BaseGardiens}

```

On pourra travailler en Python par exemple dans l'environnement [Anaconda](https://medium.com/@Shreedharvellay/anaconda-jupyter-spyder-things-you-need-to-know-3c808d824739).


1- Créez une commande qui renvoie l'ensemble des gardiens. Par exemple, cela peut être:

```python
les_gardiens = {gardien.Nom for gardien in BaseGardiens}
```
2- l'ensemble des villes d'origine des agents:

```python
In [16]: les_villes_agents = {agent.Ville for agent in BaseAgents}

In [17]: les_villes_agents
Out[17]: {'Hesperos', 'Kalgan', 'Terminus', 'Uco'}
```

3- L'ensemble des triplets (no de cabine,alien,gardien) pour chaque cabine:

```python
In [18]: triples = { (alien.NoCabine, alien.Nom, gardien.Nom) for alien in BaseAliens  for gardien in BaseGardiens if gardien.NoCabine == alien.NoCabine}

In [19]: triples
Out[19]: 
{('1', 'Zorglub', 'Branno'),
 ('2', 'Blorx', 'Darell'),
 ('3', 'Urxiz', 'Demerzel'),
 ('4', 'Darneurane', 'Seldon'),
 ('4', 'Zbleurdite', 'Seldon'),
 ('6', 'Mulzo', 'Hardin'),
 ('7', 'Zzzzzz', 'Trevize'),
 ('8', 'Arghh', 'Pelorat'),
 ('9', 'Joranum', 'Riose')}
```
À vous de jouer:

4- l'ensemble des couples (alien,allée) pour chaque alien ;

5- l'ensemble de tous les aliens de l'allée 2 ;

6- l'ensemble de toutes les planètes dont sont originaires les aliens habitant une cellule de numéro pair ;

7- l'ensemble des aliens dont les gardiens sont originaires de Terminus ;

8- l'ensemble des gardiens des aliens féminins qui mangent du bortsch ;

9- l'ensemble des cabines dont les gardiens sont originaires de Terminus ou dont les aliens sont des filles ;

10- Y a-t-il des aliments qui commencent par la même lettre que le nom du gardien qui surveille l'alien qui les mange ?

11- Y a-t-il cdes aliens originaires d'Euterpe ?

12- Est-ce que tous les aliens ont un 'x' dans leur nom ?

13- Est-ce que tous les aliens qui ont un 'x' dans leur nom ont un gardien qui vient de Terminus ?

14- Existe-t-il un alien masculin originaire de Trantor qui mange du Bortsch ou dont le gardien vient de Terminus ?
