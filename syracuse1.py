import sys
import random

class syracuse:

    def __init__(self,lecture_syracuse,ecriture_syracuse) -> None:
        self.lecture_syracuse = lecture_syracuse
        self.ecriture_syracuse = ecriture_syracuse
    
    def lecture(self):
        try:
            fichier = open(self.lecture_syracuse,"r")
        except:
            sys.exit("Impossible d'ouvrir le fichier "+self.lecture_syracuse)

        lignes = fichier.readlines()
        fichier.close()
        nombre_aleatoire = random.randrange(0,len(lignes))
        
        return int(lignes[nombre_aleatoire])


    def ecriture(self,param_1,param_2,param_3,param_4,param_5):

        try:
            fichier = open(self.ecriture_syracuse, "a")
        except:
            sys.exit("Impossible d'ouvrir le fichier "+self.lecture_syracuse)

        fichier.write("Suite de Syracuse du nombre "+ str(param_1) + "\n")
        fichier.write(param_2 + "\n")
        fichier.write("Temps de vol total : " + param_3 + "\n")
        fichier.write("Temps de vol en altitude : " + str(param_4) + "\n")
        fichier.write("Altitude maximale : " + str(param_5) + "\n\n")
        
        fichier.close()

    def syracuse(self,param):
        
        seq = [param]                     
        while seq[-1] != 1:           
            if seq[-1] % 2 == 0:      
                seq.append(seq[-1] // 2)  
            else:                    
                seq.append(seq[-1] * 3 + 1)

        seq_1 = [str(element) for element in seq]
        return (" ".join(seq_1))

    def temps_syracuse(self,param,altitude):
        seq = self.syracuse(param)
        entier = int(param)
        seq_liste = seq.split(" ")
        seq_1 = [int(element) for element in seq_liste]
        compteur = 0
        if not altitude:            
            return str(len(seq_liste) - 1)
        else:                      
            for i in seq_1:
                if i >= entier:
                    compteur+=1
                else:
                    break
            return compteur-1

    def altitude_maximale(self,param):

        seq = self.syracuse(param)
        seq_liste = seq.split(" ")
        seq_1 = [int(element) for element in seq_liste]

        return sorted(seq_1)[-1]
