class City:
    def __init__(self,name,country,population,landmarks):
        self.name = name
        self.country = country
        self.population = population
        self.landmarks = landmarks

Kandy = City("Kandy","Sri Lanka",1500000,"Temple of Tooth")

print(vars(Kandy))

Jaffna = City("Jaffna","Sri Lanka",1100000,"Jaffna National Library")

print(vars(Jaffna))