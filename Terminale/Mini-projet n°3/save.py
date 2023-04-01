import csv
import os

class Save: 
    def __init__(self, name) -> None:
        """fonction qui prend en paramètre un string name, vérifie si le fichier name existe, sinon on le créé"""
        self.name = name
        open(name,"a").close()
        if os.path.getsize(name) == 0:
            with open(name,"a", newline="") as csvfile:
                writer = csv.writer(csvfile)
                for i in range(2):
                    writer.writerow("0")
                
                

    def read(self):
        """lie le fichier et récupérer ses données dans une liste"""
        with open(self.name,"r") as csvfile:
            reader = csv.reader(csvfile)
            data = []
            for i in reader :
                data += i
        return data
    
    def write(self, data):
        """fonction qui prend en paramètre une liste data, écrit data dans le fichier """
        with open(self.name, "w", newline = "") as csvfile :
            writer = csv.writer(csvfile)
            for i in data:
                writer.writerow([i])