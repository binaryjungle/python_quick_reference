#Beginning of the program
print("Beginning Of the Program")
print("")

#class are blueprints
#objects are instance of a class
#objects have properties or methods
#classes and methods are to be defined before objects are created(instantiated)

#sample class definition
class show_message:
    #sample method definition
    def message(self):
        print("This is a test message")

#creation(instantiation) of an object
error_message = show_message()
#using the method of the object
error_message.message()

#another easy example for class
class vehicle1:
    #constructor. This method will be called immediately once the object is created
    def __init__(self, v_type = "car"):
        self._v_type = v_type
        
    def what_vehicle(self):
        return self._v_type

#bus and truck objects created from vehicle1 class
bus = vehicle1()
truck = vehicle1(v_type="truck")

#method of the object called by DOT seperator
print(bus.what_vehicle())
print(truck.what_vehicle())

print(id(bus))
print(type(bus))

class vehicle2:
    def __init__(self, **kwargs ):
        self._v_type = kwargs["v_type"] if "v_type" in kwargs else "Not a Vehicle"
        self._v_fuel = kwargs["v_fuel"] if "v_fuel" in kwargs else "Not Applicable"
        
    def what_vehicle(self):
        return self._v_type
    
    #Setter
    def fuel_method(self, fuel):
        #updates only if value for fule is provided
        if fuel: self._v_fuel=fuel
    
    #Getter or Accessor
    def what_fuel(self, fuel=None):
        #overrides the fuel provided already while creating the object
        self.fuel_method(fuel)
        return self._v_fuel
    
    def __str__(self):
        return f"Vehicle Type: {self.what_vehicle()}; Vehicle Fuel: {self.what_fuel()}"
    
cycle = vehicle2(v_type="bicycle",v_fuel="air")
print(cycle.what_vehicle())
#overrides the fuel provided already while creating the object
print(cycle.what_fuel("Petrol"))
#Will take the fuel provided while creating the object
#or will take the value in else part of __init__ method
print(cycle.what_fuel())

print(cycle) 

#Example using special class method __iter__ and __next__
class multiplication_table1:
    def __init__(self, *args ):
        self._which_table = args[0]
        self._until_what= args[1]
        self._start = 0
        self._next = self._start
    
    #below method will be used to make the object iterable (eg: if for loop is required)
    def __iter__(self):
        return self
    
    def __next__(self):
        if self._next == self._until_what:
            raise StopIteration
        else:
            self._next += 1
            return f"{self._which_table} * {self._next} = {self._which_table * self._next}"

#for 12th table, 15 iterations will be done using iter method
#in each iteration, next will increment by 1 and used for multiplication
#below for loop is possible because of __iter__ method
for looper in multiplication_table1(12, 15):
    print(looper)

print("style 2")

#for 12th table, 20 iterations will be done
#in each ieration, the looper will be incremented in iter method itself
class multiplication_table2:
    def __init__(self, until_when ):
        self._until_when = until_when
        self._looper = 1
    
    #below method will be used to make the object iterable (eg: if for loop is required)
    def __iter__(self):
        while self._looper <= self._until_when:
            yield self._looper
            self._looper += 1

number = 12

#below for loop is possible because of __iter__ method
for looper in multiplication_table2(20):
    print(f"{number} * {looper} = {number * looper}")

#base class is defined
class insurance:
    def __init__(self, **kwargs):
        self._sum_insured = kwargs["sum_insured"]
        self._policy_duration = kwargs["policy_duration"]
        self._start_year = kwargs["start_year"]
        self._premium = kwargs["premium"]
        self._current_year = 2018
        
    def remaining_period(self):
        return self._current_year - self._start_year

#class inheriting the base class define above
#below class will calculate remaining insured amount which the base class can't
class medical_insurance(insurance):
    def __init__(self, **kwargs):
        self._claimed_amount = 0
        #inherits all other values from base class or super class
        super().__init__(**kwargs)
    
    def remaining_insured_amount(self):
        return self._sum_insured - self._claimed_amount

    def claimed_amount(self, amt = 0):
        if amt: self._claimed_amount = amt

#class inheriting the base class define above
#below class will calculate accrued bonus which the base class can't
class money_back_life_insurance(insurance):
    def __init__(self, **kwargs):
        self._interest = 0.08
        #inherits all other values from base class or super class
        super().__init__(**kwargs)
    
    def accrued_bonus(self):
        return ((self._current_year - self._start_year)*\
                self._premium*(self._current_year - self._start_year)\
                *self._interest)+self._premium

#even the input parameters are same for different insurances, outcome of each insurance is different
#by having same base class for one insurance, all other insurance inherits from base class
#the new classes or new insurances will just give back their specific outcomes
sam_medical_insurance = medical_insurance(sum_insured=10000, \
                                        policy_duration=2, start_year=2017, \
                                        premium=250)
john_medical_insurance = medical_insurance(sum_insured=12000, \
                                           policy_duration=4, start_year=2016, \
                                           premium=275)
sam_money_back_insurance = money_back_life_insurance(sum_insured=100000, \
                                        policy_duration=20, start_year=2011, \
                                        premium=1250)
john_money_back_insurance=money_back_life_insurance(sum_insured=100000, \
                                        policy_duration=20, start_year=2015, \
                                        premium=1250)    
    
    
print(sam_medical_insurance.remaining_insured_amount())
sam_medical_insurance.claimed_amount(200)
print(sam_medical_insurance.remaining_insured_amount())
print(sam_money_back_insurance.accrued_bonus())

#using getters and setters    
class furniture:
    def __init__(self, **kwargs):
        self._all_properties = kwargs

    def set_properties(self, ip_property, ip_value):
        self._all_properties[ip_property] = ip_value
        
    def get_properties(self, ip_property):
        return self._all_properties.get(ip_property, "Property Doesn't Exists")
    
    #this definition is required to be used in setter and deleter methods below for just one property MATERIAL
    @property
    def material(self): return self._all_properties.get("material", None)
    
    @material.setter
    def material(self, val): self._all_properties["material"] = val
    
    #need to know how to delete
    @material.deleter
    def material(self): del self._all_properties["material"]

wall_shelf = furniture(rack = 4, material = "wood", price = 350)
chair = furniture(legs = 4, price = 300)
table = furniture(legs = 6, price = 1200, area = 4, material = "teak")

print(wall_shelf.get_properties("material"))
print(chair.get_properties("material"))
#below will use set_properties method
chair.set_properties("material", "plastic")
print(chair.get_properties("material"))

#below approach will use the setter method
print(table.material)
table.material="tree"
print(table.material)

#End of the program
print("")
print("End Of the Program")
