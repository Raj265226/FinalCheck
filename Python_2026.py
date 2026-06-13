# One solution
msg = 'the sun rises in the east'
# output = 'eht snu sesir ni eht stea'
# condition 1 - words in odd position -> reverse it
# condition 2 - words in even position -> consonants appear vowels
y=[]
x=msg.split()
cons = ''
vows = ''
for i in range(len(x)):
    if i%2 == 0:
        y.append(x[i][::-1])
    else:
        for j in range(len(x[i])):
            if x[i][j] not in 'aeiou':
                cons += x[i][j]
            else:
                vows += x[i][j]
        y.append(cons+vows)
        cons = ''
        vows = ''
print(' '.join(y))

# Second Solution
sentence = 'I love python and it so easy to learn'
# output = {1:1,2:3,3:1,4:2,5:1,6:1}
output = {}
x=[]
for i,w in enumerate(sentence.split()):
    x.append(len(w))
x.sort()
count = 1
for i in range(len(x)-1):
    if x[i] == x[i+1]:
        count += 1
    else:
        output[x[i]] = count
        count = 1
output[x[-1]] = count
print(output)

# -------------------- Python Dev -----------------------------
# Condition 1 - Vehicle 2 types - Two Wheelers , Four Wheelers
# Condition 2 - Display vehicle details - Id,type,cost, premium and also handle error
# Condition 3 - Premium - For 2 wheelers 2% , 4 wheelers 6%

class Vehicle:
    def __init__(self,vehicle_id, type, cost):
        self.vehicle_id = vehicle_id
        self.type = type
        self.cost = cost
        self.premium_amount = 0

    def calculate_premium(self):
        if self.type == 'Two Wheelers':
            self.premium_amount = self.cost*0.02
        elif self.type == 'Four Wheelers':
            self.premium_amount = self.cost * 0.06
        else:
            print('Invalid Vehicle type')
            return
    def display_details(self):
        self.calculate_premium()
        print('Vehicle Id: ',self.vehicle_id,' Vehicle type: ',self.type,' Vehicle cost: ',self.cost,' Vehicle premium: ',self.premium_amount)
w1=Vehicle(26,'Two Wheelers', 26000)
w1.display_details()
w2=Vehicle(52,'Four Wheelers', 52000)
w2.display_details()
w3=Vehicle(104,'Three Wheelers', 104000)
w3.display_details()

# Condition 1 - Class - Student, Private Attributes - student_id , marks , age , initialize all variables to None
# Condition 2 - Age > 20, Marks between 0 and 100.
# Condition 3 - validate_marks() and validate_age() - If valid return True else False
# Condition 4 - valid validate_marks() , validate_age() and If marks > 65 return True else False

class Student:
    def __init__(self):
        self.__student_id = None
        self.__marks = None
        self.__age = None

    def set_student_id(self, student_id):
        self.__student_id = student_id
    def set_marks(self, marks):
        self.__marks = marks
    def set_age(self, age):
        self.__age = age

    def get_student_id(self):
        return self.__student_id
    def get_marks(self):
        return self.__marks
    def get_age(self):
        return self.__age

    def validate_marks(self):
        if 0 <= self.__marks <= 100:
            return True
        return False
    def validate_age(self):
        if self.__age > 20:
            return True
        return False

    def check_qualification(self):
        if self.validate_marks() and self.validate_age():
            if self.__marks > 65:
                return True
        return False

s1 = Student()
s1.set_student_id(101)
s1.set_marks(63)                # Condition 1 -- Not qualified
s1.set_marks(66)                # Condition 2 -- Qualified
s1.set_age(36)
if s1.check_qualification():
    print('Qualified')
else:
    print('Not qualified')

# Condition 1 - Class - Student, Private Attributes - course_id , fees , initialize all variables to None
# Condition 2 - course_id - 1001,1002 and fees - 26000, 17000
# Condition 3 - choose_course(course_id) - If valid course then marks > 85 then discount 25% and return True else False
# Condition 4 - Include getter

class Student:
    def __init__(self, marks):
        self.__course_id = None
        self.__fees = None
        self.__marks = marks

    def get_course_id(self):
        return self.__course_id
    def get_fees(self):
        return self.__fees

    def choose_course(self, course_id):
        course_details = {
            '1001': 25575,
            '1002': 15500
        }
        if course_id in course_details:
            self.__course_id = course_id
            self.__fees = course_details[course_id]
            if self.__marks > 85:
                self.__fees *= 0.75
            return True
        return False

s1 = Student(80)                    # Condition 1
# s1 = Student(86)                                  # Condition 2       # Condition 3
if s1.choose_course('1001'):        # Condition 1   # Condition 2
# if s1.choose_course('1003'):                                          # Condition 3
    print('fees', s1.get_fees(), 'for ', s1.get_course_id())
else:
    print('No course')


# Condition 1 - classroom_list -> class attribute
# Condition 2 - search_classroom(class_room) -> classmethod
# Condition 3 - if classroom is in list then return 'Found' or else -1
class Classroom:
    classroom_list = ['c1','c2']
    def __init__(self,classroom):
        self.classroom=classroom

    @classmethod    
    def search_classroom(cls,classroom):
        if classroom in cls.classroom_list:
            return 'Found'
        return -1
print(Classroom.search_classroom('c1'))
print(Classroom.search_classroom('c3'))

# Condition 1 - class Ticket , class variable counter = 0 , __init__(passenger_name,source,destination)
# Condition 2 - validate_source_destination() when source - Delhi and destination - Mumbai,Kolkata
# Condition 3 - generate_ticket() where  ticket_id auto-generated - 1st letter of source destination and then number [SD01]

class Ticket:
    counter = 0
    def __init__(self,passenger_name,source,destination):
        self.passenger_name=passenger_name
        self.source=source
        self.destination=destination
        self.ticket_id=None

    def get_source(self):
        return self.source == 'Delhi'
    def get_destination(self):
        return self.destination in ['Mumbai','Kolkata']
    def validate_source_destination(self):
        return self.get_source() and self.get_destination()
    def get_passenger_name(self):
        return self.passenger_name
    def get_ticket_id(self):
        return self.ticket_id

    def generate_ticket(self):
        if self.validate_source_destination():
            Ticket.counter += 1
            self.ticket_id = (self.source[0]+self.destination[0]+str(Ticket.counter).zfill(2))
        else:
            self.ticket_id = None

t1=Ticket('Raj','Delhi','Kolkata')
t1.generate_ticket()
print(t1.ticket_id)
t2=Ticket('Ram','Delhi','Kolkata')
t2.generate_ticket()
print(t2.ticket_id)
t3=Ticket('Rahul','Delhi','Noida')
t3.generate_ticket()
print(t3.ticket_id)

# Condition 1 - class FruitInfo , static - fruit_name_list and fruit_price_list, static - get_fruit_price(fruit_name) 
# Condition 2 - fruit_name_list -'Apple','Guava','Orange','Grape','Sweet Lime' and fruit_price_list - 200,80,70,110,60
# Condition 3 - class Customer , __init__(customer_name,cust_type)
# Condition 4 - class Purchase , __init__(customer,fruit_name,quantity), calculate_price() , static counter 101
# Condition 4 - calculate_price() - price = kg*quantity , if price max then 2% discount on > 1, if min then 5% on >=5 ,
#    cust_type 'wholesale' additional 10% discount, purchase_id will be P101,P102 (prefix 'P'+ counter). no fruit return -1

class FruitInfo:
    fruit_name_list = ['Apple','Guava','Orange','Grape','Sweet Lime']
    fruit_price_list = [200,80,70,110,60]

    @staticmethod
    def get_fruit_price(fruit_name):
        if fruit_name in FruitInfo.fruit_name_list:
            index = FruitInfo.fruit_name_list.index(fruit_name)
            return FruitInfo.fruit_price_list[index]
        return -1
    @staticmethod
    def get_fruit_name_list():
        return FruitInfo.fruit_price_list
    @staticmethod
    def get_fruit_price_list():
        return FruitInfo.fruit_price_list

class Customer:
    def __init__(self,customer_name,cust_type):
        self.customer_name = customer_name
        self.cust_type = cust_type
    def get_customer_name(self):
        return self.customer_name
    def get_cust_type(self):
        return self.cust_type

class Purchase:
    counter = 101
    def __init__(self,customer,fruit_name,quantity):
        self.customer = customer
        self.fruit_name = fruit_name
        self.quantity = quantity
        self.purchase_id = None
    def get_purchase_id(self):
        return self.purchase_id
    def get_customer(self):
        return self.customer
    def get_quantity(self):
        return self.quantity
    def calculate_price(self):
        price_per_kg = FruitInfo.get_fruit_price(self.fruit_name)
        total_price = price_per_kg * self.quantity      
        if price_per_kg == -1:                                          #Condition0
            return -1                        
        max_price = max(FruitInfo.get_fruit_price_list())
        min_price = min(FruitInfo.get_fruit_price_list())
        if price_per_kg == max_price and self.quantity > 1:             #Condition1,Condition2
            total_price *= 0.98
        if price_per_kg == min_price and self.quantity >= 5:            #Condition3,Condition4
            total_price *= 0.95
        if self.customer.get_cust_type() == 'Wholesale':                #Condition5,Condition6
            total_price *= 0.90
        self.purchase_id = 'P'+str(Purchase.counter)
        Purchase.counter += 1
        return total_price
c0 = Customer('Raj','Wholesale')                                                #Condition0
p0 = Purchase(c0,'Papaya',5)    
print('Total price: ',p0.calculate_price(),' and id: ',p0.get_purchase_id())  
c1 = Customer('Raj','Regular')                                                  #Condition1
p1 = Purchase(c1,'Apple',0.5)          
print('Total price: ',p1.calculate_price(),' and id: ',p1.get_purchase_id())                                 
c2 = Customer('Raj','Regular')                                                  #Condition2
p2 = Purchase(c2,'Apple',2)          
print('Total price: ',p2.calculate_price(),' and id: ',p2.get_purchase_id())   
c3 = Customer('Raj','Regular')                                                  #Condition3
p3 = Purchase(c3,'Sweet Lime',4)          
print('Total price: ',p3.calculate_price(),' and id: ',p3.get_purchase_id())   
c4 = Customer('Raj','Regular')                                                  #Condition4
p4 = Purchase(c4,'Sweet Lime',5)          
print('Total price: ',p4.calculate_price(),' and id: ',p4.get_purchase_id())   
c5 = Customer('Raj','Wholesale')                                                #Condition5
p5 = Purchase(c5,'Sweet Lime',6)          
print('Total price: ',p5.calculate_price(),' and id: ',p5.get_purchase_id())   
c6 = Customer('Raj','Wholesale')                                                #Condition6
p6 = Purchase(c6,'Orange',5)          
print('Total price: ',p6.calculate_price(),' and id: ',p6.get_purchase_id())   

# Condition 1 - class Appreal , __init__(price,item_type) , get_price(), set_price(price), get_item_type()
#               calculate_price()-Add 5%, static counter 100 , get_item_id() - item_id - C/S+counter 
# Condition 2 - class Cutton , __init__(price,discount), invoke Cotton as item_type, price - Apply discount -> Add 5%
# Condition 3 - class Silk , __init__(price), calculate_price() , invoke Silk as item_type , price - Add 10% 
#                points 10 if price > 10000 else 3
class Apprel:
    counter = 100
    def __init__(self,price,item_type):
        Apprel.counter += 1
        self.price = price 
        self.item_type = item_type
        if self.item_type == 'Cotton':
            self.item_id = 'C'+ str(Apprel.counter)
        elif item_type == 'Silk':
            self.item_id = 'S'+ str(Apprel.counter)
        else:
            self.item_id = str(Apprel.counter)
    def get_item_id(self):
        return self.item_id
    def get_price(self):
        return self.price
    def set_price(self,price):
        self.price = price
    def calculate_price(self):
        self.price = self.price * 1.05

class Cotton(Apprel):
    def __init__(self,price,discount):
        super().__init__(price,'Cotton')
        self.discount = discount    
    def calculate_price(self):
        super().calculate_price()
        self.price = self.price - (self.price*self.discount/100)
        self.price = self.price * 1.05
    def get_discount(self):
        return self.discount

class Silk(Apprel):
    def __init__(self,price):
        super().__init__(price,'Silk')
        self.points = 0
    def calculate_price(self):
        super().calculate_price()
        if self.price > 10000:
            self.points = 10
        else:
            self.points = 3
        self.price = self.price * 1.10 
    def get_points(self):
        return self.points

c1=Cotton(1000,5)
c1.calculate_price()
print('Item price',c1.get_price(),'and Item id:',c1.get_item_id())
s1=Silk(1000)
s1.calculate_price()
print('Item price',s1.get_price(),'and Item id:',s1.get_item_id(),'and item point:',s1.get_points())
s2=Silk(11000)
s2.calculate_price()
print('Item price',s2.get_price(),'and Item id:',s2.get_item_id(),'and item point:',s2.get_points())
a1=Apprel(1500,'Synthetic')
a1.calculate_price()
print('Item price',a1.get_price(),'and Item id:',a1.get_item_id())

# Condition 1 - class Customer,__init__(customer_name),bill_amount,bill_id,calculate_bill_amount()[abstract],get_customer_name()           
# Condition 2 - class RegularCustomer , __init__(customer_name,no_of_tiffin),counter-100, validate_no_of_tiffin() - 1-7
#    calculate_bill_amount()-tiffin_cost=50,if no_of_tiffin-1-2, if 3-5-10% discount,if 6-7-30% discount,bill_amount=tiffin_cost*no_of_tiffin
# Condition 3 - class OccasionalCustomer , __init__(customer_name,distance_in_kms), counter - 100, validate_distance_in_kms() - 1-5 kms ,
#    calculate_bill_amount()-tiffin_cost=50,delivery_charge-if 1-2 kms then 5 else 7.5,bill_amount = tiffin_cost+distance*delivery_charge

from abc import ABC, abstractmethod
class Customer(ABC):
    def __init__(self,customer_name):
        self.customer_name = customer_name
        self.bill_amount = 0
        self.bill_id = None
    def get_customer_name(self):
        return self.customer_name
    @abstractmethod
    def calculate_bill_amount(self):
        pass

class RegularCustomer(Customer):
    counter = 100
    def __init__(self,customer_name,no_of_tiffin):
        super().__init__(customer_name)
        RegularCustomer.counter += 1
        self.bill_id = 'R' + str(RegularCustomer.counter)
        self.no_of_tiffin = no_of_tiffin
    def get_no_of_tiffin(self):
        return self.no_of_tiffin
    def validate_no_of_tiffin(self):
        if 1<= self.no_of_tiffin <=7:
            return True
        return False
    def calculate_bill_amount(self):
        if self.validate_no_of_tiffin():
            tiffin_cost = 50
            if 1<= self.no_of_tiffin <= 2:
                self.bill_amount = tiffin_cost * self.no_of_tiffin
            elif 3<= self.no_of_tiffin <= 5:
                self.bill_amount = tiffin_cost * self.no_of_tiffin * 0.90
            else: self.bill_amount = tiffin_cost * self.no_of_tiffin * 0.70
            return self.bill_amount
        else:
            self.bill_amount = -1
            return self.bill_amount

class OccasionalCustomer(Customer):
    counter = 100
    def __init__(self,customer_name,distance_in_kms):
        super().__init__(customer_name)
        OccasionalCustomer.counter += 1
        self.bill_id = 'O' + str(OccasionalCustomer.counter)
        self.distance_in_kms = distance_in_kms
    def get_distance_in_kms(self):
        return self.distance_in_kms
    def validate_distance_in_kms(self):
        if 1<= self.distance_in_kms <= 5:
            return True
        return False
        
    def calculate_bill_amount(self):
        if self.validate_distance_in_kms():
            tiffin_cost = 50
            if 1<= self.distance_in_kms <= 2:
                self.bill_amount = tiffin_cost + self.distance_in_kms * 5
            else:
                self.bill_amount = tiffin_cost + self.distance_in_kms * 7.5
            return self.bill_amount
        else:
            self.bill_amount = -1
            return self.bill_amount
        
r1 = RegularCustomer('Raj1',1)
r2 = RegularCustomer('Raj2',2)
r3 = RegularCustomer('Raj3',4)
r4 = RegularCustomer('Raj4',6)
r5 = RegularCustomer('Raj5',8)

r_list = [r1,r2,r3,r4,r5]

for Customer in r_list:
    print('c_name:',Customer.get_customer_name(),'b_id:',Customer.bill_id,'Tiffins:',Customer.get_no_of_tiffin(),'b_amount:',Customer.calculate_bill_amount())

o1 = OccasionalCustomer('Raj1',1)
o2 = OccasionalCustomer('Raj2',2)
o3 = OccasionalCustomer('Raj3',3)
o4 = OccasionalCustomer('Raj4',5)
o5 = OccasionalCustomer('Raj5',6)

o_list = [o1,o2,o3,o4,o5]

for Customer in o_list:
    print('c_name:',Customer.get_customer_name(),'b_id:',Customer.bill_id,'Distances:',Customer.get_distance_in_kms(),'b_amount:',Customer.calculate_bill_amount())

# condition 1 - class Mechanic, __init__(mechanic_id, specialization, vehicle_count) , use set get
# condition 2 - class VehicleService , __init__(mechanic_list) , assign_vehicle_for_service(mechanic_id, vehicle_type)
# condition 3 - Mechanic ID	 Specialization	 Vehicle Count , 101 TW	1 , 102	FW	0 , 103	TW	4 , 104	FW	2
# condition 4 - check given mechanic exists , if no - raise InvalidMechanicIdException
#    if vehicle_type not exists - raise InvalidMechanicSpecializationException, if success vehicle count =+ 1 else proper msg

class InvalidMechanicIdException(Exception):
    pass

class InvalidMechanicSpecializationException(Exception):
    pass

class Mechanic:
    def __init__(self,mechanic_id, specialization, vehicle_count):
        self.mechanic_id = mechanic_id
        self.specialization = specialization
        self.vehicle_count = vehicle_count
    def get_mechanic_id(self):
        return self.mechanic_id
    def get_specialization(self):
        return self.specialization
    def get_vehicle_count(self):
        return self.vehicle_count
    def set_mechanic_id(self,mechanic_id):
        self.mechanic_id = mechanic_id
    def set_specialization(self,specialization):
        self.specialization = specialization
    def set_vehicle_count(self,vehicle_count):
        self.vehicle_count = vehicle_count

class VehicleService:
    def __init__(self,mechanic_list):
        self.mechanic_list = mechanic_list

    def assign_vehicle_for_service(self,mechanic_id, vehicle_type):
        mechanic_found = None
        for mechanic in self.mechanic_list:
            if mechanic.get_mechanic_id() == mechanic_id:
                mechanic_found = mechanic
                break    
        if mechanic_found is None:
            raise InvalidMechanicIdException('InvalidMechanicIdException..')
        if mechanic_found.get_specialization() != vehicle_type:
            raise InvalidMechanicSpecializationException('InvalidMechanicSpecializationException..')
        mechanic_found.set_vehicle_count(mechanic_found.get_vehicle_count() + 1)
        return mechanic_found.get_vehicle_count()

mechanic_list = [
    Mechanic(101,'TW',1),
    Mechanic(102,'FW',0),
    Mechanic(103,'TW',4),
    Mechanic(104,'FW',2)
]
Vehicle_service = VehicleService(mechanic_list)
try:
    updated_vehicle_count = Vehicle_service.assign_vehicle_for_service(int(input('Enter Mechanic_id: ')), input('Enter Mechanic type: '))
    print('updated count: -',updated_vehicle_count)
except Exception as e:
    print(e)