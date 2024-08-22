class House:
    def __init__(self,name,number_of_floors):
        self.name=name
        self.number_of_floors=number_of_floors
        
    def go_to(self,new_floor):
        i=0
        if new_floor>self.number_of_floors or new_floor<1:
            print('Такого этажа не существует')
            
        else:
            for i in range(new_floor):
                i+=1
                print(i)
            
                
    def __len__(self):
        print(self.number_of_floors)
        
    def __str__(self):
        print(f'Название: {self.name}, кол-во этажей:{self.number_of_floors}')
        
        
    def __lt__(self,other):
        return self.number_of_floors<other.number_of_floors
    
    def __le__(self,other):
        return self.number_of_floors<=other.number_of_floors
        
    def __gt__(self,other):
        return self.number_of_floors>other.number_of_floors
    
    def __ge__(self,other):
        return self.number_of_floors>=other.number_of_floors
    
    def __ne__(self,other):
        return self.number_of_floors!=other.number_of_floors
    
    def __add__(self,value):
        if isinstance(value,House):
            print(f'{self.number_of_floors+value.number_of_floors}')
        elif isinstance(value,int):
            self.number_of_floors+=value
            print(f'{self.number_of_floors}')
    def __radd__(self,value):
        if isinstance(value,House):
            print(f'{self.number_of_floors+value.number_of_floors}')
        elif isinstance(value,int):
            self.number_of_floors+=value
            print(f'{self.number_of_floors}')
            
    def __iadd__(self,value):
        if isinstance(value,House):
            print(f'{self.number_of_floors+value.number_of_floors}')
        elif isinstance(value,int):
            self.number_of_floors+=value
            print(f'{self.number_of_floors}')


    
dev=House('GK Les', 12)
print(dev.name, dev.number_of_floors)
dev2=House('Domik v derevne', 2)
print(dev2.name, dev2.number_of_floors)
print(dev2>dev)
dev2.__radd__(8)