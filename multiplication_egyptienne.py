
import re

 

if __name__ == "__main__":

 

    liste_index = [] #liste des indexes des multiples de 2

    liste_petit_nombre = [] #liste des reste de la soustraction lors de la decomposition initialisé par le plus petit nombre entré par l'utilisateur

    liste_multiple_2 = [1]  #liste des multiples de 2

    liste_decomposition = [] #liste de multiple de 2 de la decomposition

 

   

    # generation du tableau de multiple de 2

    a = 10

    while a > 0:

       liste_multiple_2.append(2*liste_multiple_2[-1])

       a-=1

   

    # recuperation des nombres à multiplier

    n_1 = input("entrer le premier nombre de la multiplication : ")

 

    while (not re.search("\d{1,}",n_1)):

 

         n_1 = input("entrer le premier nombre de la multiplication : ")

    n_1 = int(n_1)

 

    n_2 = input("entrer le deuxième nombre de la multiplication : ")

 

    while (not re.search("\d{1,}",n_2)):

 

         n_2 = input("entrer le deuxième nombre de la multiplication : ")

    n_2 = int(n_2)

 

    if(n_1>n_2):

        liste_petit_nombre.append(n_2)

    else:

        liste_petit_nombre.append(n_1)

 

    #decomposition du plus petit nombre

    while (liste_petit_nombre[-1] != 0):

        index = 0

        for element in liste_multiple_2:

            if element > liste_petit_nombre[-1]:

                liste_index.append(index-1)

                liste_decomposition.append(liste_multiple_2[index-1])

                print(str(liste_petit_nombre[-1])+"-"+str(liste_multiple_2[index-1])+"="+str(liste_petit_nombre[-1]-liste_multiple_2[index-1]))

                liste_petit_nombre.append(liste_petit_nombre[-1]-liste_multiple_2[index-1])

               

                break

            index += 1

 

    # affichage element de la decomposition

    if(n_1>n_2):

        print("element de la decomposition de "+str(n_2)+"  :",liste_decomposition)

    else:

        print("element de la decomposition de "+str(n_1)+"  :",liste_decomposition)

   

   

 

    #calcul à partir des elements de la decomposition

    result = 0

    if(n_1>n_2):

        for i in liste_index:

            result += n_1*liste_multiple_2[i]

    else:

        for i in liste_index:

            result += n_2*liste_multiple_2[i]

           

    print("la multiplication de "+str(n_1)+" x "+str(n_2)+" = "+str(result))

 

