'''name=input('Enter your name: ')
password=input('Enter your password: ')
while name!='Tej':
    print('You entered either wrong name or password or both.')
    name=input('Enter your name: ')
while password!='swordfish':
    password=input('Enter your password: ')
print('Hi,',name)
'''
'''name=''
while True:
    name=input('Enter your name: ')
    if name=='Tej':
        break
print('Hi, user',name)'''


'''name=input('Enter your name: ')
#password=input('Enter is the password: ')
if name=='Tej':
    pwd=input('Enter the password: ')
    while pwd!='Swordfish':
        print('password you entered is wrong.')
        pwd=input('Enter your password: ')
        if pwd=='Swordfish':
            break
print('Done.')'''

'''import random
for i in range(0,5):
    print(random.randint(1,10))'''

'''import sys
while True:
    print('Type exit to exit.')
    response=input()
    if response=='exit':
        sys.exit()
    print('You typed ' + response +  '.')'''

'''import random
def randomNum():
    print(random.randint(1,10))
    print(random.randint(11,20))
    print(random.randint(21,30))
def sayHello(name):
    print('Hello '+name)
#randomNum()
#randomNum()
#randomNum()
sayHello('Jaya')
print('Hello', end=' ')
print('World')'''

'''for i in range(1,11):
    print(i)'''

'''i=1
while i<11:
    print(i)
    i=i+1'''

#print(round(12.6589,3))
#print(abs(-56))

'''import random
def getAnswer(answerNumber):
    if answerNumber==1:
        return 'No'
    elif answerNumber==2:
        return 'Yes'
    else:
        return 'It sucks'
r=random.randint(1,5)
print(getAnswer(random.randint(1,5)))
print(getAnswer(r))
print(getAnswer(r))
print(getAnswer(r))
print(getAnswer(r))
print(getAnswer(r))'''


'''def gloChange():
    global a
    a='local'
a='global'
gloChange()
print(a)'''


'''def exceptionError(dividedby):
    return 12/dividedby
try:
    print(exceptionError(3))
    print(exceptionError(2))
    print(exceptionError(0))
except:
    print('Error : Invalid Argument.')'''

'''def collatz(number):
    if number%2==0:
        return number//2
    elif number%2==1:
        return 3*number+1
print('Enter a number:')
while True:
    #print('Enter a number:')
    num=int(input())
    res=collatz(num)
    if res!=1:
        continue
    elif res==1:
        print(res)
        break
print('Done!')'''

'''a=['cat','rat','parrot']
print('Enter your choice: ')
ch=int(input())
try:
    print(a[ch])
except:
    print('Error : index is out of limit.')

print(len(a))'''

'''catNames=[]
while True:
    print('Enter the name of '+str(len(catNames)+1)+' (Just hit Enter if you want to exit)')
    name=input()
    if name=='':
        break
    else:
        catNames=catNames+[name]'''

#names=['Sophie', 'Jayven', 'Venus']
'''print('Enter pet name:')
chk=input()
if chk not in names:
    print('I don\'t have a pet named '+chk)
else:
    print('I\'ve the pet named '+chk)'''
'''male,female,poi=names
print(male)
print(female)
print(poi)'''
'''import random
names=['Sophie', 'Jayven', 'Venus']
for index,item in enumerate(names):
    print('Index '+str(index)+' has ',item)
print(random.choice(names))
random.shuffle(names)
print(names)
random.shuffle(names)
print(names)'''

#import random
#spam = ['Zophie', 'Pooka', 'Fat-tail', 'Pooka']
'''print(spam.index('Pooka'))
print(spam.index('Fat-tail'))
print(spam.index('Zophie'))
print(random.choice(spam))
random.shuffle(spam)
print(spam)'''
'''spam.append('Toka')
print(spam)
spam.insert(1,'Joka')
print(spam)'''
'''spam.remove('Pooka')
#print(spam)
spam.sort()
print(spam)
print(spam)'''
#spam.sort(reverse=True)
#print(spam)
'''name='Zophie a cat'
newName=name[:7]+ 'the ' +name[9:12]
print(name)
print(newName)'''

'''def listMod(argList):
    res=''
    #a=''
    if argList!=[]:
        for i in range(0,len(argList)):
            if i!=(len(argList)-1):
                res=res+str(argList[i])+', '
            elif i==(len(argList)-1):
                res=res+'and '+argList[len(argList)-1]
    else:
        print('List should be big.')
    return res
        
a=['cat','dog','rat','pig','hen','ant','bat']
print(listMod(a))'''

'''birthdays={'Alice': 'Apr 1', 'Bob': 'Dec 12', 'Carol': 'Mar 4'}
while True:
    print('Enter the name or Press Enter to quit')
    name=input()
    if name=='':
        break
    if name in birthdays:
        print(name,'\'s birthday is on ',birthdays[name])
    else:
        print('No such name exists in the list.')
        break
print('We are sorry.')'''

'''message = 'It was a bright cold day in April, and the clocks were striking thirteen.'
count={}
for i in message:
    count.setdefault(i,0)
    count[i]=count[i]+1
print(count)'''

'''allGuests = {'Alice': {'apples': 5, 'pretzels': 12},
             'Bob': {'ham sandwiches': 3, 'apples': 2},
             'Carol': {'cups': 3, 'apple pies': 1}}
def totalBrought(guests,item):
    numOfItems=0
    for k,v in guests.items():
        numOfItems=numOfItems+v.get(item,0)
    return numOfItems'''

'''items={'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
def inventCount(inventory):
    itemCount=0
    print('Inventory')
    for k,v in inventory.items():
        print(str(v)+ ' '+ k)
        itemCount=itemCount+v
    print('Total number of items: ',itemCount)
inventCount(items)'''

'''def addToInventory(inventory,addedItems):
    for i in addedItems:
        if i in inventory:
            inventory[i]=inventory[i]+1
        elif i not in inventory:
            inventory[i]=inventory.setdefault(i,1)
    return inventory
inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
print(addToInventory(inv,dragonLoot))'''

'''#Palindrome
s=''
while True:
    print('Enter text you want to check :')
    text=input()
    if text!='':
        for i in text[::-1]:
            s=s+i
        if text==s:
            print(text,'is palindrome.')
        elif text!=s:
            print(text,'is not palindrome.')
            continue
    elif text=='':
        break'''

'''def printPicnic(picnicItems,leftWidth,rightWidth):
    print('PicnicItems'.center(leftWidth+rightWidth,'-'))
    for k,v in picnicItems.items():
        print(k.ljust(leftWidth,'.')+str(v).rjust(rightWidth))
picnicItems = {'sandwiches': 4, 'apples': 12, 'cups': 4, 'cookies': 8000}
printPicnic(picnicItems, 12, 5)        '''

'''import re
#phNumRegex=re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
#mo=phNumRegex.search('My number is 785-800-1574.')
#pint(mo.group())
batRegex=re.compile(r'Bat(wo)+man')
mob=batRegex.search('Batman in the future.')
print(mob.group())'''


#counting no of vowels and consonents in a string
'''print('Enter the text below: ')
a=input()
vowelCnt=0
consonentCnt=0
for i in a:
    if i in ('a','e','i','o','u'):
        vowelCnt=vowelCnt+1
    else:
        consonentCnt=consonentCnt+1
print('No of vowels are: ',vowelCnt)
print('No of consonents are: ',consonentCnt)'''


#Finding the no of occurence of the chars in a string
'''print('Enter the text: ')
s=input()
print('Enter the char you want to count.')
chk=input()
cnt=0
for i in s:
    if i==chk:
        cnt=cnt+1
print('The count of character '+ chk + 'is ',cnt)'''

'''a=10
b=20
c=0
c=a
a=b
b=c
print(a)
print(b)
print(c)'''

'''class Dog():
    def __init__(self,name,breed):
        self.name=name
        self.breed=breed
    def tailWag(self):
        print('The tail is there for '+self.name.title())
    def play(self):
        print('The dog is playful '+self.breed.title())
dog1=Dog('Bruno','German Shepard')
dog2=Dog('Plassey','Pug')
dog1.tailWag()
dog2.tailWag()
dog1.play()
dog2.play()
dog.__dict()__'''



'''class Restaurant():
    #hospitality=''
    def __init__(self,name,ctype):
        self.name=name
        self.ctype=ctype
        self.hospitality=''
        self.ambience=''
    def describeRestaurant(self):
        print('Restaurant name'.upper()+'-------'+'Cuisine type'.upper()+'-------'+'Hospitality'.upper())
        print(self.name.title()+'-------'+self.ctype.title()+'------'+self.hospitality.title())
    def openRestaurant(self):
        print(self.resName+ 'is open.')
    def ambience(self,amb):
        self.ambience=amb
class Country(Restaurant):
    def __init__(self,nameOfCountry):
        self.countryName=nameOfCountry
        #super(Restaurant,self).__init__(name,ctype)
    pass
c1=Country('Taste of India','Indian')

print(c1.name)
#c1


res1=Restaurant('Desi Bites', 'Indian')
res2=Restaurant('Olive Garden', 'Italian')
res3=Restaurant('Green Papaya', 'Thai')
res1.hospitality='good'
res1.ambience('good')
print(res1.ambience)
print(res1.__dict__)

#res2.hospitality='average'
#print(res2.__dict__)'''


'''class Car:
    def __init__(self,year,make,model):
        self.year=year
        self.make=make
        self.model=model
        self.odo=0
    def getDescriptionName(self):
        print(str(self.year).title()+' '+self.make.title()+' ' +self.model.title())
    def getOdometerReading(self)    :
        print('This car has '+str(self.odo)+' miles on it.')
    def odoUpdate(self,rdng):
        self.odo=rdng
        print('The mileage is updated to '+str(self.odo)+' for '+str(self.year).title()+' '+self.make.title()+' ' +self.model.title())
    def fill_gas_tank():
        print('How many gallons is required?')

class ElectricCar(Car):
    def __init__(self,year,make,model):
        super().__init__(year,make,model)
        self.batterySize=70
    def getBatteryDetails(self):
        print('The size of the battery is '+str(self.batterySize)+' kwh battery.')
    @classmethod
    def fill_gas_tank(cls):
        print('Ecars don\'t have gas tanks mate.')
myECar=ElectricCar(2016,'Tesla','Plaid')
myECar.getDescriptionName()
myECar.batterySize=100
myECar.getBatteryDetails()
ElectricCar.fill_gas_tank()'''


''''class Restaurant:
    def __init__(self,name,cuisine):
        self.name=name
        self.cuisine=cuisine
    def resDescription(self):
        print('The name of the restaurant is '+self.name.title()+' and the cuisine type is '+self.cuisine.title())
        
class icecreamStand(Restaurant):
    flavors=['Vanilla','Chocolate','Butterscotch','Strawberry']
    def __init__(self,name,cuisine):
        super().__init__(name,cuisine)
    def listOfFlavors(self):
        for i,j in enumerate(self.flavors):
            print(str(i+1)+ '. '+j)
    
cus1=icecreamStand('Desi Bites', 'Indian')
cus1.resDescription()
cus1.listOfFlavors()'''

a=input("Enter the string: ")
count=0
for i in a:
    
        
        
    
