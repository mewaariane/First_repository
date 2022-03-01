from Syracuse import *

if __name__ == "__main__":

    objet = syracuse("lecture.txt","ecriture.txt")
    nombre = objet.lecture()
    suite_syracuse = objet.syracuse(nombre)
    objet.ecriture(nombre,objet.syracuse(nombre),objet.temps_syracuse(nombre,False),objet.temps_syracuse(nombre,True),objet.altitude_maximale(nombre))
    

    print("<<< execution terminée >>>\nConsultez le fichier ecriture.txt")
    