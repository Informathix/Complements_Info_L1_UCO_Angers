import numpy as np
from math import *
from random import *
global n  #n:taille du plateau de jeu (carré de taille n)
n=10

def script():
    J=creation_plateau()
    J=melange(J,1000)
    K=J.copy()
    print('matrice mélangée de départ (après 1000 transpositions):')
    print(K)
    print('matrice rangée :')
    print(resolution_taquin_strategie_1(J)[0])
    print('nombre de coups pour résoudre avec la stratégie 1 :',\
     resolution_taquin_strategie_1(J)[1])
    print('nombre de coups pour résoudre avec la strategie 2 :',\
     resolution_taquin_strategie_2(J)[1])

def creation_plateau ():
#renvoie un plateau de jeu rangé sous forme de matrice
   J=np.array([[k for k in range (j*n+1,(j+1)*n+1)] for j in range(n)])
   J[n-1,n-1]=0
   return(J)


def direction ():
#renvoie la liste des 4 directions latérales dans lesquelles peuvent se déplacer
    #les numéros
    return ([[0,1],[1,0],[0,-1],[-1,0]])


def test_direction (J,i,j):
#J:matrice représentant le plateau de jeu
#(i,j):couple de coordonnées de la position d'un numéro
#renvoie la liste de couples des directions dans lesquelles le numéro de
    #coordonnées (i,j) peut se déplacer
    D=direction()
    P=[]
    for k in range (len(D)):
        (l,c)=D[k]
        if 0<=i+l<=n-1 and 0<=j+c<=n-1:
            P.append(D[k])
    return(P)


def melange(J,nb_melange):
#J:matrice représentant le plateau de jeu
#nb_melange: nombre de transpositions que l'on effectue pour mélanger le plateau
#renvoie le plateau de jeu mélangé sous forme de matrice
    for i in range (nb_melange):
        i0,j0=position_numero(J,0)
        P=test_direction(J,i0,j0)
        m=randint(0,len(P)-1)
        l,c=P[m]
        i1,j1=i0+l,j0+c
        a,b=J[i0,j0],J[i1,j1]
        J[i0,j0]=b
        J[i1,j1]=a
    return(J)


def position_numero(J,x):
#J:plateau de jeu sous forme de matrice
#x:numéro dont on cherche la position
#renvoie les coordonnées du numéro x dans le plateau de jeu
    for i in range (n):
        for j in range (n):
            if J[i,j]==x:
                return(i,j)


def position_finale_zero(J,x):
#J:plateau de jeu sous forme de matrice
#x:numéro que l'on veut déplacer
#renvoie les coordonnées de la position où le zéro doit se placer pour déplacer
    #le numéro x
    (i,j)=position_numero(J,x)
    l=(x-1)//n
    c=(x-1)%n
    if l<n-2 and (c<n-2 or (c==n-2 and i>l) or (c==n-1)):
        if i==l:
            i1,j1=i,j-1
        else :
            if j<=n-2:
                i1,j1=i,j+1
            else:
                i1,j1=i-1,j
    elif l<n-2 and c==n-2 and i==l:
        if j==c:
            (i1,j1)=(i,j+1)
        else:
            (i1,j1)=(i,j-1)
    else :
        if j<=n-2:
            i1,j1=i,j-1
        else:
            i1,j1=i-1,j
    return(i1,j1)



def trouve_chemins(J,option1,option2,liste_interdite):
#J:plateau de jeu (matrice)
#option1:position initiale (coordonnées)
#option2:position finale (coordonnées)
#liste_interdite: liste des numéros qui ne doivent pas être déplacés
#renvoie une liste de listes de couples représentant les chemins que le numéro
    #peut emprunter pour se déplacer
    i0,j0=option1
    i1,j1=option2
    L=[[(i0,j0)]]
    test=True
    if (i0,j0)==(i1,j1):
        chemins=[[(i0,j0)]]
    else:
        while test:
            M=[]
            for i in range (len(L)):
                N=L[i]
                xe,ye=L[i][-1]
                D=test_direction (J,xe,ye)
                for j in range (len(D)):
                    l,c=D[j]
                    xf,yf=xe+l,ye+c
                    if J[xf,yf] not in liste_interdite and (xf,yf) not in N:
                        NN=N+[(xf,yf)]
                        M.append(NN)
                        if (xf,yf)==(i1,j1):
                            test=False
            L=M
        chemins=[]
        for k in range(len(L)):
            [a,b]=L[k][-1]
            if [a,b]==[i1,j1]:
                chemins.append(L[k])
    return(chemins)



def test_position_finale(J,x):
#J:matrice représentant le plateau de jeu
#x:numéro que l'on veut déplacer
#(booléen) renvoie true si le numéro x est bien placé
    R=creation_plateau()
    i1,j1=position_numero(R,x)
    i2,j2=position_numero(J,x)
    return((i1,j1)==(i2,j2))


def translation_de_x(J,x,option1,option2,liste_interdite):
#J:matrice représentant le plateau de jeu
#x:numéro que l'on veut déplacer
#option1:position initiale (coordonnées)
#option2:position finale (coordonnées)
#liste_interdite: liste des numéros qui ne doivent pas être déplacés
#renvoie la matrice (plateau de jeu) après une translation du numéro x et le
    #nombre de coups effectués
    C=trouve_chemins(J,option1,option2,liste_interdite)
    X=randint(0,len(C)-1)
    chemin=C[X]
    compteur=0
    for i in range (0,len(chemin)-1):
        (i0,j0)=chemin[i]
        (i1,j1)=chemin[i+1]
        J[i0][j0],J[i1][j1]=J[i1][j1],J[i0][j0]
        compteur+=1
    (i1,j1)=position_numero(J,0)
    (i2,j2)=position_numero(J,x)
    J[i1][j1],J[i2][j2]=J[i2][j2],J[i1][j1]
    compteur+=1
    return(J,compteur)


def placement_final_premieres_lignes_strategie_1(J,x,liste_interdite):
#J:matrice représentant le plateau de jeu
#x:numéro que l'on veut déplacer
#liste_interdite: liste des numéros qui ne doivent pas être déplacés
#renvoie la matrice (plateau de jeu) avec le numéro x bien placé et le nombre de
    #coups effectués
    c=0
    while not test_position_finale(J,x):
        option1=position_numero(J,0)
        option2=position_finale_zero(J,x)
        J,compteur=translation_de_x(J,x,option1,option2,liste_interdite)
        c+=compteur
    return(J,c)


def position_provisoire_dernieres_colonnes (J,x):
#J:matrice représentant le plateau de jeu
#x:numéro que l'on veut déplacer
#renvoie la position provisoire du numéro (coordonnées)
    l=(x-1)//n
    c=(x-1)%n
    if c==n-2:
       (i1,j1)=(l,c+1)
    if c==n-1:
        (i1,j1)=(l+1,c)
    return(i1,j1)


def test_position_provisoire_dernieres_colonnes(J,x):
#J:matrice représentant le plateau de jeu
#x:numéro que l'on veut déplacer
#(booléen) renvoie true si x est bien à sa position provisoire
    (i1,j1)=position_provisoire_dernieres_colonnes(J,x)
    (i2,j2)=position_numero(J,x)
    return((i1,j1)==(i2,j2))



def placement_provisoire_dernieres_colonnes(J,x,liste_interdite):
#J:matrice représentant le plateau de jeu
#x:numéro que l'on veut déplacer
#liste_interdite: liste des numéros qui ne doivent pas être déplacés
#renvoie la matrice (le plateau de jeu) avec x dans sa position provisoire et
    #le nombre de coups
    c=0
    while not test_position_provisoire_dernieres_colonnes(J,x):
        option1=position_numero(J,0)
        option2=position_finale_zero(J,x)
        J,compteur=translation_de_x(J,x,option1,option2,liste_interdite)
        c+=compteur
    if (x-1)%n==n-2:
        (i0,j0)=position_numero(J,0)
        (i1,j1)=position_numero(J,x)
        if (i0,j0)==(i1,j1-1):
            J[i0][j0],J[i0+1][j0]=J[i0+1][j0],J[i0][j0]
            c+=1
            (i0,j0)=position_numero(J,0)
            J[i0][j0],J[i0][j0+1]=J[i0][j0+1],J[i0][j0]
            c+=1

        if test_est_on_dans_un_cas_complique_dernieres_colonnes(J,x):
            J,compteur=\
    placement_provisoire_dernieres_colonnes_cas_complique(J,x,liste_interdite)
            c+=compteur
    return(J,c)


def position_finale_pivot(J,x):
#J:plateau de jeu (matrice) avec les numéros x et x-1 dans leur position
    #provisoire
#x:numéro que l'on veut déplacer
#renvoie la position finale du pivot (coordonnées)
    if (x-1)%n==n-1:
        (i,j)=position_numero(J,x)
        return((i,j-1))
    else:
        (i,j)=position_numero(J,x)
        return(i+1,j-1)


def placement_du_pivot(J,x,liste_interdite):
#J:plateau de jeu (matrice) avec x et x-1 dans leur position provisoire
#x:numéro que l'on veut déplacer (x est sur la dernière colonne)
#liste_interdite: liste des numéros qui ne doivent pas être déplacés
#fonction qui renvoie la matrice (le plateau de jeu) avec le pivot bien placé et
    #le nombre de coups effectués
    option1=position_numero(J,0)
    option2=position_finale_pivot(J,x)
    C=trouve_chemins(J,option1,option2,liste_interdite)
    X=randint(0,len(C)-1)
    chemin=C[X]
    compteur=0
    for i in range (0,len(chemin)-1):
        (i0,j0)=chemin[i]
        (i1,j1)=chemin[i+1]
        J[i0][j0],J[i1][j1]=J[i1][j1],J[i0][j0]
        compteur+=1
    return(J,compteur)


def rangement_premieres_lignes_strategie_1(J):
#J:matrice représentant le plateau de jeu
#renvoie la matrice (le plateau de jeu) avec les n-2 premières lignes rangées et
    #le nombre de coups effectués pour cela
    liste_interdite=[]
    c=0
    for x in range (1,(n-2)*n+1):
        if (x-1)%n==n-2:
            if position_numero(J,x)!=((x-1)//n,(x-1)%n) or \
            position_numero(J,x+1)!=(x//n,x%n) :
                liste_interdite.append(x)
                J,compteur=\
            placement_provisoire_dernieres_colonnes(J,x,liste_interdite)
                c+=compteur
                liste_interdite.append(x+1)
                J,compteur=\
            placement_provisoire_dernieres_colonnes(J,x+1,liste_interdite)
                c+=compteur
                J,compteur=placement_du_pivot(J,x+1,liste_interdite)
                c+=compteur
                J,compteur=\
            placement_final_premieres_lignes_strategie_1(J,x,liste_interdite)
                c+=compteur
                J,compteur=\
            placement_final_premieres_lignes_strategie_1(J,x+1,liste_interdite)
                c+=compteur
        else:
            liste_interdite.append(x)
            J,compteur=\
            placement_final_premieres_lignes_strategie_1(J,x,liste_interdite)
            c+=compteur
    return(J,c)


def position_provisoire_dernieres_lignes (x):
#x:numéro (faisant partie des deux dernières lignes) que l'on veut déplacer
#renvoie les coordonnées de la position provisoire où placer x
    l=(x-1)//n
    c=(x-1)%n
    if l==n-2:
        (i3,j3)=(l,c+1)
    if l==n-1:
        (i3,j3)=(l-1,c)
    return ((i3,j3))


def test_position_provisoire_dernieres_lignes (J,x):
#J:plateau de jeu (matrice) avec les n-2 premières lignes ordonnées
#x:numéro dont on veut savoir s'il est bien placé
#(booléen) renvoie true si le numéro x est dans sa position provisoire
    (i2,j2)=position_numero(J,x)
    (i3,j3)=position_provisoire_dernieres_lignes(x)
    return ((i3,j3)==(i2,j2))



def position_finale_zero_dernieres_lignes(J,x):
#J:plateau de jeu (matrice) avec les n-2 premières lignes rangées
#x:numéro (faisant partie des 2 dernières lignes) que l'on veut déplacer
#renvoie un couple de coordonnées (la position finale du zéro pour ce numéro)
    (i1,j1)=position_provisoire_dernieres_lignes(x)
    (i2,j2)=position_numero(J,x)
    if i1==i2:
        i3,j3=i2,j2-1
    else :
        if j2<n-1:
            i3,j3=i2,j2+1
        else:
            i3,j3=i2-1,j2
    return(i3,j3)


def placement_provisoire_dernieres_lignes(J,x,liste_interdite):
#J:plateau de jeu (matrice) avec les n-2 premières lignes rangées
#x:numéro que l'on veut déplacer
#liste_interdite: liste des numéros qui ne doivent pas être déplacés
#renvoie la matrice (le plateau de jeu) où les numéros x et x+n sont dans leur
    #position provisoire et le nombre de coups effectués
    c=0
    while not test_position_provisoire_dernieres_lignes (J,x):
        option1=position_numero(J,0)
        option2=position_finale_zero_dernieres_lignes(J,x)
        J,compteur=translation_de_x(J,x,option1,option2,liste_interdite)
        c+=compteur
    l=(x-1)//n
    c=(x-1)%n
    if l==n-1:
        if test_est_on_dans_un_cas_complique_dernieres_lignes(J,x):
            J,\
compteur=placement_provisoire_dernieres_lignes_cas_complique(J,x,liste_interdite)
            c+=compteur
    return(J,c)


def placement_final_dernieres_lignes(J,x,liste_interdite):
#J:plateau de jeu (matrice) avec les numéros des n-2 premières lignes placés et
    #les numéros x et x+n dans leurs positions provisoires
#x:numéro de la ligne n-1 que l'on veut placer
#liste_interdite: liste des numéros qui ne doivent pas être déplacés
#renvoie la matrice (plateau de jeu) où x et x+n sont rangés et le nombre de
    #coups effectués
    c=0
    (i1,j1)=position_numero(J,0)
    (i2,j2)=position_numero(J,x+n)
    J[i1][j1],J[i2][j2]=J[i2][j2],J[i1][j1]
    c+=1
    (i1,j1)=position_numero(J,0)
    (i2,j2)=position_numero(J,x)
    J[i1][j1],J[i2][j2]=J[i2][j2],J[i1][j1]
    c+=1
    return(J,c)


def rangement_dernieres_lignes(J):
#J:plateau de jeu (matrice) avec les n-2 premières lignes rangées
#renvoie la matrice (plateau de jeu) rangée entièrement sauf le dernier carré en
    #bas à droite, et le nombre de coups effectués
    c=0
    liste_interdite=[k for k in range (1,n*(n-2)+1)]
    for x in range ((n-2)*n+1,n*(n-1)-1):
        if position_numero(J,x)!=((x-1)//n,(x-1)%n) or \
        position_numero(J,x+n)!=((x+n-1)//n,(x+n-1)%n):
            liste_interdite.append(x+n)
            J,compteur=\
            placement_provisoire_dernieres_lignes(J,x+n,liste_interdite)
            c+=compteur
            liste_interdite.append(x)
            J,compteur=placement_provisoire_dernieres_lignes(J,x,liste_interdite)
            c+=compteur
            J,c=placement_du_pivot(J,x,liste_interdite)
            c+=compteur
            J,compteur=placement_final_dernieres_lignes(J,x,liste_interdite)
            c+=compteur
    return (J,c)


def rangement_dernier_carre(J):
#J:plateau de jeu (matrice) rangé sauf le dernier carré en bas à droite
#renvoie la matrice (plateau de jeu) entièrement rangée et le nombre de coups
    #effectués
    plateau=creation_plateau()
    i0,j0=position_numero(J,0)
    D=3*direction()
    compteur=0
    k=0
    while J[n-2][n-2]!=plateau[n-2][n-2] or J[n-1][n-1]!=plateau[n-1][n-1]:
        i0,j0=position_numero(J,0)
        i1,j1=i0+D[k][0],j0+D[k][1]
        if 0<=i1<=n-1 and 0<=j1<=n-1:
            J[i0][j0],J[i1][j1]=J[i1][j1],J[i0][j0]
        k+=1
        compteur+=1
    return(J,compteur)


def resolution_taquin_strategie_1(J):
#J:plateau de jeu (matrice) mélangé
#renvoie la matrice (plateau de jeu) rangée et le nombre de coups effectués
    L=creation_plateau()
    M=J.copy()
    compteur=0
    M=J.copy()
    M,c=rangement_premieres_lignes_strategie_1(M)
    compteur+=c
    M,c=rangement_dernieres_lignes(M)
    compteur+=c
    M,c=rangement_dernier_carre(M)
    compteur+=c
    return(M,compteur)


def placement_final_premieres_lignes_strategie_2(J,x,liste_interdite):
#J:matrice représentant le plateau de jeu
#x:numéro des n-2 premières lignes à déplacer
#liste_interdite: liste des numéros qui ne doivent pas être déplacés
#renvoie la matrice (le plateau de jeu) avec le numéro x bien placé et le nombre
#de coups effectués
    option1=position_numero(J,x)
    option2=(x-1)//n,(x-1)%n
    C=trouve_chemins(J,option1,option2,liste_interdite)
    X=randint(0,len(C)-1)
    chemin=C[X]
    liste_interdite.append(x)
    c=0
    for i in range (1,len(chemin)):
        option1=position_numero(J,0)
        option2=chemin[i]
        J,compteur=translation_de_x(J,x,option1,option2,liste_interdite)
        c+=compteur
    return(J,c)


def rangement_premieres_lignes_strategie_2(J):
#J:matrice représentant le plateau de jeu
#renvoie la matrice (plateau de jeu) avec les n-2 premières lignes rangées et le
#nombre de coups effectués
    liste_interdite=[]
    compteur=0
    for x in range (1,n*(n-2)+1):
        if x%n==n-1:
            if position_numero(J,x)!=((x-1)//n,(x-1)%n) or \
            position_numero(J,x+1)!=(x//n,x%n):
                liste_interdite.append(x)
                J,c=placement_provisoire_dernieres_colonnes(J,x,liste_interdite)
                compteur+=c
                liste_interdite.append(x+1)
                J,c=\
                placement_provisoire_dernieres_colonnes(J,x+1,liste_interdite)
                compteur+=c
                J,c=placement_du_pivot(J,x+1,liste_interdite)
                compteur+=c
                J,c=\
            placement_final_premieres_lignes_strategie_1(J,x,liste_interdite)
                compteur+=c
                J,c=\
            placement_final_premieres_lignes_strategie_1(J,x+1,liste_interdite)
                compteur+=c
        else :
            J,c=placement_final_premieres_lignes_strategie_2(J,x,liste_interdite)
            liste_interdite.append(x)
            compteur+=c
    return(J,compteur)


def resolution_taquin_strategie_2(J):
#J:matrice représentant le plateau de jeu
#renvoie la matrice (plateau de jeu) rangée et le nombre de coups effectués
    c=0
    J,compteur=rangement_premieres_lignes_strategie_2(J)
    c+=compteur
    J,compteur=rangement_dernieres_lignes(J)
    c+=compteur
    J,compteur=rangement_dernier_carre(J)
    c+=compteur
    return(J,c)


def comparaison_des_strategies(nb_melange):
#nb_melange: nombre de permutations que l'on effectue pour mélanger le plateau
#renvoie la matrice de départ (mélangée), un 10 uplet correspondant au nombre de
    #coup effectués pour ranger la même matrice par la stratégie 1, un 10 uplet
    #correspondant au nombre de coup effectués pour ranger la même matrice par
    #la stratégie 2
    J=creation_plateau()
    J=melange(J,nb_melange)
    strategie1=[]
    strategie2=[]
    for k in range (10):
        M=J.copy()
        S1=resolution_taquin_strategie_1(M)
        S2=resolution_taquin_strategie_2(M)
        strategie1.append(S1[1])
        strategie2.append(S2[1])
    return(J,strategie1,strategie2)



"""Les fonctions suivantes sont exhaustives. Elles permettent de débloquer le
jeu dans certaines situations compliquées qu'il faut résoudre à la main.
Ceci n'est pas le but de notre projet."""


def test_est_on_dans_un_cas_complique_dernieres_colonnes(J,x):
#J:matrice représentant le plateau de jeu
#x:numéro que l'on veut déplacer
#(booléen) renvoie true si l'on se trouve dans un cas compliqué
    (i1,j1)=position_numero(J,x)
    (i2,j2)=position_numero(J,x+1)
    return((i2,j2)==(i1,j1-1))



def position_finale_du_zero_cas_complique_dernieres_colonnes(J,x):
#J:plateau de jeu (matrice) dans une configuration compliquée
#x:numéro que l'on veut déplacer
#renvoie la position du zéro (coordonnées) pour modifier la position de x et x+1
    (i,j)=position_numero(J,x)
    return(i+1,j)


def placement_provisoire_dernieres_colonnes_cas_complique(J,x,liste_interdite):
#J:plateau de jeu (matrice) dans une configuration compliquée
#x:numéro que l'on veut déplacer
#liste_interdite: liste des numéros qui ne doivent pas être déplacés
#renvoie la matrice (plateau de jeu) avec le numéro x dans sa position provisoire
    compteur=0
    option1=position_numero(J,0)
    option2=position_finale_du_zero_cas_complique_dernieres_colonnes(J,x)
    (i0,j0)=position_numero(J,0)
    (i1,j1)=position_numero(J,x)
    J[i0][j0],J[i1][j1]=J[i1][j1],J[i0][j0]
    compteur+=1
    (i0,j0)=position_numero(J,0)
    (i1,j1)=position_numero(J,x+1)
    J[i0][j0],J[i1][j1]=J[i1][j1],J[i0][j0]
    compteur+=1
    option1=position_numero(J,0)
    option2=position_finale_du_zero_cas_complique_dernieres_colonnes(J,x)
    N=trouve_chemins(J,option1,option2,liste_interdite)
    X=randint(0,len(N)-1)
    chemin=N[X]
    for i in range (len(chemin)-1):
        (i0,j0)=chemin[i]
        (i1,j1)=chemin[i+1]
        J[i0][j0],J[i1][j1]=J[i1][j1],J[i0][j0]
        compteur+=1
    (i1,j1)=position_numero(J,0)
    (i2,j2)=position_numero(J,x)
    J[i1][j1],J[i2][j2]=J[i2][j2],J[i1][j1]
    compteur+=1
    (i1,j1)=position_numero(J,0)
    (i2,j2)=position_numero(J,x+1)
    J[i1][j1],J[i2][j2]=J[i2][j2],J[i1][j1]
    compteur+=1
    (i0,j0)=position_numero(J,0)
    J[i0][j0],J[i0][j0-1]=J[i0][j0-1],J[i0][j0]
    compteur+=1
    (i0,j0)=position_numero(J,0)
    J[i0][j0],J[i0+1][j0]=J[i0+1][j0],J[i0][j0]
    compteur+=1
    (i0,j0)=position_numero(J,0)
    J[i0][j0],J[i0][j0+1]=J[i0][j0+1],J[i0][j0]
    compteur+=1
    while not test_position_provisoire_dernieres_colonnes(J,x):
        option1=position_numero(J,0)
        option2=position_finale_zero(J,x)
        J,c=translation_de_x(J,x,option1,option2,liste_interdite)
        compteur+=c
    return(J,compteur)


def positionnement_initial_du_zero(J,x):
#J:plateau de jeu (matrice) avec les n-2 premières lignes rangées
#x:numéro que l'on veut placer à sa position provisoire
#renvoie la position (couple de coordonnées) où le zéro doit être pour initier
    #la sortie du cas compliqué
    (i,j)=position_numero(J,x)
    return(i,j+1)


def test_est_on_dans_un_cas_complique_dernieres_lignes(J,x):
#J:plateau de jeu (matrice) avec les n-2 premières lignes rangées
#x:numéro que l'on veut déplacer
#(booléen) renvoie true si l'on se trouve dans un cas compliqué
    (i0,j0)=position_numero(J,x)
    (i1,j1)=position_numero(J,x-n)
    return((i1,j1)==(i0+1,j0))


def position_finale_zero_cas_complique_dernieres_lignes (J,x):
#J:plateau de jeu (matrice) avec les n-2 premières lignes rangées
#x:numéro que l'on veut placer à sa position provisoire
#renvoie les coordonnées de la position où le zéro doit être placé pour sortir
    #du cas compliqué
    (i,j)=position_provisoire_dernieres_lignes(x)
    return(i,j+2)

def placement_provisoire_dernieres_lignes_cas_complique(J,x,liste_interdite):
#J:plateau de jeu (matrice) avec les n-2 premieres lignes rangées mais
    #dans un cas compliqué pour x et x+n
#x:numéro (des 2 dernières lignes) à placer dans sa position provisoire
#liste_interdite: liste des numéros qui ne doivent pas être déplacés
#renvoie la matrice (plateau de jeu) sortie du cas compliqué et le nombre de
    #coups effectués
    option1=position_numero(J,0)
    option2=positionnement_initial_du_zero(J,x)
    N=trouve_chemins(J,option1,option2,liste_interdite)
    X=randint(0,len(N)-1)
    chemin=N[X]
    compteur=0
    for i in range (len(chemin)-1):
        (i0,j0)=chemin[i]
        (i1,j1)=chemin[i+1]
        J[i0][j0],J[i1][j1]=J[i1][j1],J[i0][j0]
        compteur+=1
    (i0,j0)=position_numero(J,x)
    (i1,j1)=position_numero(J,0)
    J[i0][j0],J[i1][j1]=J[i1][j1],J[i0][j0]
    compteur+=1
    (i0,j0)=position_numero(J,x-n)
    (i1,j1)=position_numero(J,0)
    J[i0][j0],J[i1][j1]=J[i1][j1],J[i0][j0]
    compteur+=1
    option1=position_numero(J,0)
    option2=position_finale_zero_cas_complique_dernieres_lignes(J,x)
    N=trouve_chemins(J,option1,option2,liste_interdite)
    X=randint(0,len(N)-1)
    chemin=N[X]
    for i in range (len(chemin)-1):
        (i0,j0)=chemin[i]
        (i1,j1)=chemin[i+1]
        J[i0][j0],J[i1][j1]=J[i1][j1],J[i0][j0]
        compteur+=1
    (i1,j1)=position_numero(J,0)
    (i2,j2)=position_numero(J,x)
    J[i1][j1],J[i2][j2]=J[i2][j2],J[i1][j1]
    compteur+=1
    (i1,j1)=position_numero(J,0)
    (i2,j2)=position_numero(J,x-n)
    J[i1][j1],J[i2][j2]=J[i2][j2],J[i1][j1]
    compteur+=1
    (i1,j1)=position_numero(J,0)
    J[i1][j1],J[i1+1][j1]=J[i1+1][j1],J[i1][j1]
    compteur+=1
    (i1,j1)=position_numero(J,0)
    J[i1][j1],J[i1][j1+1]=J[i1][j1+1],J[i1][j1]
    compteur+=1
    (i1,j1)=position_numero(J,0)
    J[i1][j1],J[i1-1][j1]=J[i1-1][j1],J[i1][j1]
    compteur+=1
    (i1,j1)=position_numero(J,0)
    (i2,j2)=position_numero(J,x)
    J[i1][j1],J[i2][j2]=J[i2][j2],J[i1][j1]
    compteur+=1
    while not test_position_provisoire_dernieres_lignes(J,x):
        option1=position_numero(J,0)
        option2=position_finale_zero_dernieres_lignes(J,x)
        J,c=translation_de_x(J,x,option1,option2,liste_interdite)
        compteur+=c
    return(J,compteur)


script()
