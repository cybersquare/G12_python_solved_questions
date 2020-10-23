class Country: 
    def __init__(self, name, capital):
        self.c_name = name 
        self.c_capital = capital
        
        
class State (Country):
    def __init__(self, name,  capital, c_name, c_capital): 
        super().__init__(c_name, c_capital)
        self.name = name
        self.capital = capital

   

c = Country('India', 'Delhi')
s = State('Kerala', 'Tvm', 'India', 'Delhi' )

print('Country:')
print(c.c_name, c.c_capital)


print('State:')
print(s.name, s.capital)
print(s.c_name)



