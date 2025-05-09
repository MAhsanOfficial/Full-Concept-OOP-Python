##                                      ******************  OOPS  in PYthon  ***************

 

#                                 ......     Object Oriented Programing  (Code likhne ka tarika)   ......




#  Self is the Object ONe by One Property Insert


#                         ****************** Static OOPS  ==> By Defult Values  *****************



class BankAccount():
    def __init__(self):                  # Initializer / Constructor Function / Magic Function    "Self" *Seld Is the constract of Object* 
        self.owner_name= 'Ahsan'           ## Constructor Fucntion Object Ko Bana Tha Hai
        self.balance =  1000               #  By Default Vallue is a Static
        
        
## Object of the Class

account1 = BankAccount()   # Calling the Class (Call this class of Constructor)  1) Object 

account2 = BankAccount()   # Calling the Class (Call this class of Constructor)  2) Object

## Jitni Bar Constructo call karein ge uthni bar Object bane Gein

print(account1.owner_name)           # Calling the Attribute (Property)  Acess The Value   1) Value
print(account2.balance)           # Calling the Attribute (Property)  Acess The Value      2) Value








# .......................................................XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX.....................................................







#                     ****************** Dynamic OOPS  ==> (Dynamic Value Enter the User is own ) ********************


class BankAccount():
    def __init__(self,owner_name,balance):       # Initializer / Constructor Function / Magic Function    "Self" *Seld Is the constract of Object* 
        self.owner_name = owner_name          ## Constructor Fucntion Object Ko Bana Tha Hai
        self.balance = balance                 # Its not defualt valye its a Dynamic value 
        
        
## Object of the Class

account1 = BankAccount("Ali",3000)   # Calling the Class (Call this class of Constructor)  1) Object      *Dynamic Value *

account2 = BankAccount("Arham",5000)   # Calling the Class (Call this class of Constructor)  2) Object     "Dynamic Value"

## Jitni Bar Constructo call karein ge uthni bar Object bane Gein

print(account1.owner_name)           # Calling the Attribute (Property)  Acess The Value   1) Value
print(account2.balance)              # Calling the Attribute (Property)  Acess The Value      2) Value  


#                                 **** INStANCE == OBJECT  ****  IS Equal






# ....................................................XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX............................................................







#                     ****************** Methods / Function  ==> (Insde the Inslializaer) ********************


class BankAccount():
    def __init__(self,owner_name,balance):       # Initializer / Constructor Function / Magic Function    "Self" *Seld Is the constract of Object* 
        self.owner_name = owner_name          ## Constructor Fucntion Object Ko Bana Tha Hai
        self.balance = balance                 # Its not defualt valye its a Dynamic value 
        
        
        
    def deposit(self,amount):                 # The Function and Method of Inisializer (The Part of Object )
        self.balance += amount
        
        
        
        
## Object of the Class

account1 = BankAccount("Ali",1000)   # Calling the Class (Call this class of Constructor)  1) Object      *Dynamic Value *


account1.deposit(8000)             # THe function Of OOPS this function are worked in Construtor these are logic Fucntion


account2 = BankAccount("Arham",3000)   # Calling the Class (Call this class of Constructor)  2) Object     "Dynamic Value"

##                           Jitni Bar Constructo call karein ge uthni bar Object bane Gein

print(account1.owner_name)           # Calling the Attribute (Property)  Acess The Value   1) Value
print(account1.balance)           # Calling the Attribute (Property)  Acess The Value   1) Value
   
                               #         (Update the value and amount by MEthods in OOPS)      




 
 
 # .........................................................XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX............................................................
 
 
 
 
 
 
 
 
 #                      GEt Detail Function all Details Account in one Methond and Function
 
    #   * Jab Sari Value Print Krwani ho Publically *  So is Function ki Madad se kr sakhte hain ....   (Get_Details)
 
 
class BankAccount():
    def __init__(self,owner_name,balance):       # Initializer / Constructor Function / Magic Function    "Self" *Seld Is the constract of Object* 
        self.owner_name = owner_name          ## Constructor Fucntion Object Ko Bana Tha Hai
        self.balance = balance                 # Its not defualt valye its a Dynamic value 
        
        
        
    def deposit(self,amount):                 # The Function and Method of Inisializer (The Part of Object )
        self.balance += amount
        
    def get_details(self):
        print(f"Owner Name :{self.owner_name}")              # All the value Acess In Vankacout with Publically
        print(f"Balanced :{self.balance}")
        
        
        
        
## Object of the Class

account1 = BankAccount("Ali",1000)   # Calling the Class (Call this class of Constructor)  1) Object      *Dynamic Value *


account1.deposit(8000)             # THe function Of OOPS this function are worked in Construtor these are logic Fucntion


account2 = BankAccount("Arham",3000)   # Calling the Class (Call this class of Constructor)  2) Object     "Dynamic Value"

##                           Jitni Bar Constructo call karein ge uthni bar Object bane Gein





print(account1.owner_name)           # Calling the Attribute (Property)  Acess The Value   1) Value
print(account1.balance)           # Calling the Attribute (Property)  Acess The Value   1) Value
   
                               #         (Update the value and amount by MEthods in OOPS)      

account1.get_details()    #  All the value acess Bank Acount ... 









# .........................................................XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX>......................................................


#                                   ****************(PIllars in OOPS)**************


#                    (There are 4 Pillar in OOPS)

#        1) Encapsulation (Hiding-Private (Protect) Acess Only INside the classs)      1) Double UNderscore 

#        2)InheritanceGrandFather and Are Properties in CHilds)   Inherits the properties In Class 
#           1) Single Underscore     
#           2) super.__init__()     == Call the Parent Constructor 

#        2) Abstraction : Ek Tarika hai jo k Complexity ko Hide Krta hai. (complex implementation ko chhupa kar sirf relevant details dikhana.) 
#        3) Polymorphism: Yaani ek hi method ka alag-alag classes me alag behavior ho sakta hai. or Phele Wwale k same name ko overright kr k jo humne banai ha bad me chalaiaga 











# ................................................XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX................................................................










#                                       1)   Pillar Of OOPS (Encapsulation) 

# **************************** Encapsulation (Hiding-Private (Protect) Acess Only INside the classs) ***********************
#                             Ye Double underscore se represent hota ha jp k sirf isi class me acess ho sakhti ha
                  
       
#         Hide and Private the Property and Value 

#    Class k Bahir us Property ko Acess nhi Kr sakhte hain Private or Hide kr ne se

# Double under score lagane se property 


 
class BankAccount():
    def __init__(self,owner_name,balance):      
        self.owner_name = owner_name          
        self.__balance = balance                    # Idr is me mene Private kr dia Hai Balance ko ab isko Class k Bahir K Acess nhi kr sakhte      
        
        
        
    def deposit(self,amount):                
        self.balance += amount
        
    def get_details(self):
        print(f"Owner Name :{self.owner_name}")            
        print(f"Balanced :{self.balance}")
        
        
        
        
## Object of the Class

account1 = BankAccount("Ali",1000)  

account1.deposit(8000)             

account2 = BankAccount("Arham",3000)  



print(account1.owner_name)          

# print(account1.__balance)                    Double Under score (Error Not Ecess ble )   
   

account1.get_details()              # Acess and use Only inside the Class 










# ................................................XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX................................................................









#  Duoble Under is Like a Provate Function __ buyt a sigle score _ is protected function in dono me ye farq ha k Private function jo k
# class me hi srif acess ho sakhte hai us k bagir nho ho sakhti 
# Single Score Ka mAtlab ha k wo apni dosri child class me acess ho sakhta ha jis se hum INteritance bhi kehte hain







#             xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx 2) Inheritance xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
# === Inherit wo ha jo agr ek father ki property us k child me ajai to usko inheritance kehte hain Singlescore wo class me to hosa khte
#  ha acess likin wo ek dosri child class me b acess ho sakhti hai



class BankAccount():
    def __init__(self,owner_name,balance):      
        self.owner_name = owner_name          
        self._balance = balance                   
        
        
        
    def deposit(self,amount):                
        self.balance += amount
        
    def get_details(self):
        print(f"Owner Name :{self.owner_name}")            
        print(f"Balanced :{self.balance}")
        
        


account1 = BankAccount("Ali",1000)  

account1.deposit(8000)             

account2 = BankAccount("Arham",3000)  



print(account1.owner_name)          


#  "nd Class with Insert the Parent



class BussinessAcount(BankAccount):
    def __init__(self,campany_name,owner_name):
        super().__init__(owner_name)                       # ISka parent ka Contructor Call kr aha hai
        self.campany_name = campany_name
        
        
b1  =  BussinessAcount('Upword','Ali')
print(b1.owner_name)                                         # Inherit the class Perent  call the Paerent Constructor Function 





# xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx







# xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx  3) Abstraction :xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
 # Ek Tarika hai jo k Complexity ko Hide Krta hai. (complex implementation ko chhupa kar sirf relevant details dikhana.) 
class BankAccount():
    def __init__(self, owner_name, balance):
        self.owner_name = owner_name
        self.__balance = balance   # 🔒 Abstraction: balance ko private banaya gaya hai

    def deposit(self, amount):
        self.__balance += amount   # ✅ Abstraction: private balance ko class ke andar access kiya

    def get_details(self):
        print(f"Owner Name : {self.owner_name}")
        print(f"Balance    : {self.__balance}")  # ✅ Abstraction: private data ko method ke through access kiya

# Object creation
account1 = BankAccount("Ali", 1000)
account1.deposit(8000)

# account1.__balance     ❌ Abstraction: direct access allowed nahi hai (error aayega)

account1.get_details()     # ✅ Safe access via method (abstraction)






# xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx





#   xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx  4 ) Polymorphism : xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
# Yaani ek hi method ka alag-alag classes me alag behavior ho sakta hai.


class BankAccount():
    def __init__(self, owner_name, balance):
        self.owner_name = owner_name
        self.__balance = balance

    def get_details(self):
        print(f"[BankAccount] Owner: {self.owner_name}, Balance: {self.__balance}")


# Subclass 1
class SavingsAccount(BankAccount):
    def get_details(self):
        # 🔁 Polymorphism: Same method name, different behavior
        print(f"[SavingsAccount] Owner: {self.owner_name} (Savings)")


# Subclass 2
class CurrentAccount(BankAccount):
    def get_details(self):
        # 🔁 Polymorphism: Different output for current account
        print(f"[CurrentAccount] Owner: {self.owner_name} (Current)")


# Polymorphism in action
accounts = [
    BankAccount("Ali", 1000),
    SavingsAccount("Arham", 5000),
    CurrentAccount("Hina", 7000)
]

for acc in accounts:
    acc.get_details()    # ✅ Same method call — different output (polymorphism)








