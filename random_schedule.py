import random
predmety = ["TEV","TEV","MAT","MAT","MAT","MAT","INF","INF","VAP","VAP","CJL","CJL","CJL","MIT","MIT","POS","POS","POS",
            "ASW","ASW","PRG","PRG","PRG","MSW","MSW"]
OBN = 0
if random.randint(0,1) == 1:
    predmety.append("OBN","OBN")
    OBN = 2
    
CELKOVE_HODIN = 28 + OBN
rozvrh = [0] * 50

def generate_schedule(seed) :
    random.seed(seed)
    

                
        


