import data
import time
Data = data.data.Dictionnary
book = data.data.book
BF = data.data.BfBook
class translate:
  
    def __init__(self):
        pass

    def translate(self):
       
        string = ""
        total = ""
        while 1:
            char = book.read(1)
            
            
            


            for a in Data:
                if str(char) == a:
                    string = string + Data[a]
                    BF.write(string + "\n")
                   

        BF.close()

    def translateBis(self,text):
        string = ""
        for a in Data:
            string = string + Data[a]
        print(string)
            
    
    

