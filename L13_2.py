
class Country:
    def __init__(self, name: str, population: str):
            self.name = name
            self.population = population
            
    def __add__(self, second_country):
        combinated_name = f'{self.name} {second_country.name}'
        combinated_population = self.population + second_country.population
        return Country(combinated_name, combinated_population)

bosnia = Country('Bosnia', 10_000_000) 
herzegovina = Country('Herzegovina', 5_000_000)  
             
bosnia_herzegovina = bosnia + herzegovina

print(bosnia_herzegovina.population) #-> 15_000_000 
print(bosnia_herzegovina.name) #-> 'Bosnia Herzegovina'
