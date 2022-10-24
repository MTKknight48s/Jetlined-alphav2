#This program was written by Mashrur Kabir
#The purpose of this program is to have information about aircraft stored in dictionaries and to display specific information about specific aircraft based on the user's request.

from audioop import add
from lib2to3.pgen2.token import NAME
import math
from unicodedata import name

#The following code sets up dictionaries of certain planes and adds information about them - Mashrur Kabir

B787 = {
     'brand' : 'boeing',
     'major operators':["american",'united','turkish','ana','lufthansa'],
     'produced from':[2007],
     'production ended':['N/A'],
     'first flight':[2009],
     'variants':['787-8','787-9','787-10'],
     'most popular variant':'787-9',
     'max range variant':['787-9', 14010],
     'max capacity variant':['787-10',336],
     'aircraft class':["Mid-Large Widebody"],
     'engines offered':['Rolls Royce Trent 1000', "General Electric GEnx"],
     'total orders': 1499
}


B777 = {
     'brand' : 'boeing',
     'major operators': ['Emirates', 'United', 'American', 'Qatar', 'Singapore'],
     'produced from':[1993],
     'production ended':['N/A'],
     'first flight':[1994],
     'variants':['777-200','777-200ER','777-200LR', '777-300','777-300ER','777-8','777-9'],
     'most popular variant':'777-300ER',
     'max range variant':['777-8',16170],
     'max capacity variant':['777-9',426],
     'aircraft class': 'Large widebody',
     'engines offered': ['General Electric GE90','Rolls Royce Trent 800', 'Pratt & Whitney PW4000','General Electric GE9X'],
     'total orders':2126
}


A350 = {
     'brand':'airbus',
     'major operators':['Delta','Qatar (grounded)', 'Lufthansa', 'Air France', 'Singapore'],
     'produced from': 2010,
     'production ended' : 'N/A',
     'first flight': 2013,
     'variants':['a350-900','a350-1000','a350-900ULR'],
     'most popular variant':'A350-900',
     'max range variant':['a350-900ULR',18000],
     'max capacity variant':['a350-1000',369],
     'aircraft class':'Mid-Large Widebody',
     'engines offered': 'Rolls Royce Trent XWB',
     'total orders': 919
}


A330 = {
     'brand': 'Airbus',
     'major operators':['Turkish','Delta','China Eastern','Air China'],
     'produced from':1992,
     'production ended':'N/A',
     'first flight':1992,
     'variants':['a330-200','a330-300','a330-800','a330-900'],
     'most popular variant':'A330-300',
     'max range variant':["a330-800",13900],
     'max capacity variant':['a330-900',300],
     'aircraft class': 'Midsize Widebody',
     'engines offered':['General Electric CF6','Pratt & Whitney PW4000','Rolls Royce 700','Rolls Royce Trent 7000'],
     'total orders':1761
}


B747 = {
     'brand':'Boeing',
     'major operators':['PanAm','Lufthansa','United','Atlas Air','Cargolux','UPS'],
     'produced from': 1968,
     'production ended':2022,
     'first flight': 1969,
     'variants':['747-100','747-SP','747-SR','747-100B','747-200','747-300','747-400','747-400ER','747-8','and much more sub-variants'],
     'most popular variant': '747-400',
     'max range variant': ['747-8',15000],
     'max capacity variant':['747-8',467],
     'aircraft class':'Jumbo Widebody',
     'engines offered':['Pratt & Whitney JT9D','Rolls Royce RB211','General Electric CF6','Pratt & Whitney PW4062','General Electric GEnx'],
     'total orders': 1573
}


A380 = {
     'brand':'Airbus',
     'major operators':['Emirates','Air France','Lufthansa','Qantas','British Airways'],
     'produced from': 2003,
     'production ended': 2021,
     'first flight': 2005,
     'variants': 'A380-800',
     'most popular variant': 'A380-800',
     'max range variant': ['A380-800', 15700],
     'max capacity variant': ['A380-800',525],
     'aircraft class': 'Super-Jumbo Widebody',
     'engines offered': ['Rolls Royce Trent 900','Engine Alliance GP7000'],
     'total orders': 251
}


A320 = {
     'brand':'Airbus',
     'major operators': ['American Airlines','Delta','United','Spirit','EasyJet'],
     'produced from': 1986,
     'production ended': 'N/A',
     'first flight': 1987,
     'variants': ['A318','A319','A320-100','A320-200','A321-100','A321-200','A319neo','A320neo','A321neo','A321LR','A321XLR'],
     'most popular variant': 'A320-200',
     'max range variant': ['A321XLR', 8700],
     'max capacity variant': ['A321XLR', 206],
     'aircraft class' : 'Narrowbody',
     'engines offered':['CFM International CFM56','IAE V2500','CFM International LEAP','Pratt & Whitney PW1000G'],
     'total orders': 16631
}

airliners = {
     'Airbus Jets' : ['A320','A380','A330','A350'],
     "Boeing Jets" : ['B777', 'B787', 'B747']
}

mostpopularvariants=[
          A320['most popular variant'], 
          A330['most popular variant'],
          A350['most popular variant'],
          A380['most popular variant'],
          B777['most popular variant'],
          B787['most popular variant'],
          B747['most popular variant']
          
          ]

Utotalorders = A320['total orders']+A330['total orders']+A350['total orders']+A380['total orders']+B777['total orders'] + B787['total orders']+B747['total orders']

listofaircraftfamilies = ['A320','A330','A350','A380','B747','B777','B787']
criteria = ['brand','major operators','produced from','production ended','first flight','variants','most popular variant','max range variant','max capacity variant','aircraft class','engines offered','total orders']


#This sets up the while loop
rerun = 0 

while rerun == 0:

     #This is asks the user what aircraft family the user wants to know about.
     print("Hello! Welcome to Jetlined.")
     print("These are the aircraft families currently in the program:")
     for index in range(len(listofaircraftfamilies)):
          print(listofaircraftfamilies[index])
     print("\n")
     family = input("What aircraft family would you like to know about? Please type one:")
     #This asks the user what they want to know.
     print("\n")
     print("These are the available criteria about the aircraft:")
     for index in range(len(criteria)):
          print(criteria[index])
     print("\n")
     key = input("What would you like to know?")
     #The following code displays the information to the user depending on what they inputed.
     print("\n")

     if family == "A320":
          if key == "brand":
               print(A320['brand'])
          if key == "major operators":
               print(A320['major operators'])
          if key == "produced from":
               print(A320['produced from'])
          if key == "production ended":
               print(A320['production ended'])
          if key == "first flight":
               print(A320['first flight'])
          if key == 'variants':
               print(A320['variants'])
          if key == 'most popular variant':
               print(A320['most popular variant'])
          if key == "max range variant":
               print(A320['max range variant'])
          if key == "max capacity variant":
               print(A320['max capacity variant'])
          if key == 'aircraft class':
               print(A320['aircraft class'])
          if key == 'engines offered':
               print(A320['engines offered'])
          if key == 'total orders':
               print(A320['total orders'])
     if family == "B787":
          if key == "brand":
               print(B787['brand'])
          if key == "major operators":
               print(B787['major operators'])
          if key == "produced from":
               print(B787['produced from'])
          if key == "production ended":
               print(B787['production ended'])
          if key == "first flight":
               print(B787['first flight'])
          if key == 'variants':
               print(B787['variants'])
          if key == 'most popular variant':
               print(B787['most popular variant'])
          if key == "max range variant":
               print(B787['max range variant'])
          if key == "max capacity variant":
               print(B787['max capacity variant'])
          if key == 'aircraft class':
               print(B787['aircraft class'])
          if key == 'engines offered':
               print(B787['engines offered'])
          if key == 'total orders':
               print(B787['total orders'])
     if family == "B777":
          if key == "brand":
               print(B777['brand'])
          if key == "major operators":
               print(B777['major operators'])
          if key == "produced from":
               print(B777['produced from'])
          if key == "production ended":
               print(B777['production ended'])
          if key == "first flight":
               print(B777['first flight'])
          if key == 'variants':
               print(B777['variants'])
          if key == 'most popular variant':
               print(B777['most popular variant'])
          if key == "max range variant":
               print(B777['max range variant'])
          if key == "max capacity variant":
               print(B777['max capacity variant'])
          if key == 'aircraft class':
               print(B777['aircraft class'])
          if key == 'engines offered':
               print(B777['engines offered'])
          if key == 'total orders':
               print(B777['total orders'])
     if family == "B747":
          if key == "brand":
               print(B747['brand'])
          if key == "major operators":
               print(B747['major operators'])
          if key == "produced from":
               print(B747['produced from'])
          if key == "production ended":
               print(B747['production ended'])
          if key == "first flight":
               print(B747['first flight'])
          if key == 'variants':
               print(B747['variants'])
          if key == 'most popular variant':
               print(B747['most popular variant'])
          if key == "max range variant":
               print(B747['max range variant'])
          if key == "max capacity variant":
               print(B747['max capacity variant'])
          if key == 'aircraft class':
               print(B747['aircraft class'])
          if key == 'engines offered':
               print(B747['engines offered'])
          if key == 'total orders':
               print(B747['total orders'])
     if family == "A380":
          if key == "brand":
               print(A380['brand'])
          if key == "major operators":
               print(A380['major operators'])
          if key == "produced from":
               print(A380['produced from'])
          if key == "production ended":
               print(A380['production ended'])
          if key == "first flight":
               print(A380['first flight'])
          if key == 'variants':
               print(A380['variants'])
          if key == 'most popular variant':
               print(A380['most popular variant'])
          if key == "max range variant":
               print(A380['max range variant'])
          if key == "max capacity variant":
               print(A380['max capacity variant'])
          if key == 'aircraft class':
               print(A380['aircraft class'])
          if key == 'engines offered':
               print(A380['engines offered'])
          if key == 'total orders':
               print(A380['total orders'])
     if family == "A330":
          if key == "brand":
               print(A330['brand'])
          if key == "major operators":
               print(A330['major operators'])
          if key == "produced from":
               print(A330['produced from'])
          if key == "production ended":
               print(A330['production ended'])
          if key == "first flight":
               print(A330['first flight'])
          if key == 'variants':
               print(A330['variants'])
          if key == 'most popular variant':
               print(A330['most popular variant'])
          if key == "max range variant":
               print(A330['max range variant'])
          if key == "max capacity variant":
               print(A330['max capacity variant'])
          if key == 'aircraft class':
               print(A330['aircraft class'])
          if key == 'engines offered':
               print(A330['engines offered'])
          if key == 'total orders':
               print(A330['total orders'])
     if family == "A350":
          if key == "brand":
               print(A350['brand'])
          if key == "major operators":
               print(A350['major operators'])
          if key == "produced from":
               print(A350['produced from'])
          if key == "production ended":
               print(A350['production ended'])
          if key == "first flight":
               print(A350['first flight'])
          if key == 'variants':
               print(A350['variants'])
          if key == 'most popular variant':
               print(A350['most popular variant'])
          if key == "max range variant":
               print(A350['max range variant'])
          if key == "max capacity variant":
               print(A350['max capacity variant'])
          if key == 'aircraft class':
               print(A350['aircraft class'])
          if key == 'engines offered':
               print(A350['engines offered'])
          if key == 'total orders':
               print(A350['total orders'])

     print("\n")

     print("Would you like to enter information about another aircraft not displayed?")
     addaircraft = str(input("yes or no: "))

     if addaircraft == "yes" or addaircraft == "Yes" or addaircraft == "Y" or addaircraft == 'y':
          print('\n')
          #ATTENTION: PLEASE REMEMBER TO MODIFY CRITERIA WITH MULTIPLE ENTRIES INTO LISTS AND NOT SINGLE VALUED ITEMS
          nname = input("What is the aircraft family name?")
          nbrand = input("Who is the aircraft made by?")
          nmajoroperators = input("What is one major airline that uses it?")
          nproducedfrom = int(input("When was the aircraft produced from?"))
          nproductionended = input("When did the production end?")
          nfirstflight = int(input("When was the first flight?"))
          nvariants = int(input("How many variants does the aircraft have?"))
          nmostpopularvariant = input("What is the most popular variant?")
          nmaxrangevariant = input("What is the variant with the most range?")
          nmaxrangevariantv = int(input("What is its range in kilometers?"))
          nmaxcapacityvariant = input("What is the variant with the most capacity?")
          nmaxcapacityvariantv = int(input("How many passengers?"))
          naircraftclass = input("What is the class of the aircraft?")
          nenginesoffered = input("What is the most common type of engine on the aircraft?")
          ntotalorders = int(input("How many total orders does the aircraft have?"))
          newaircraft = {
               'aircraft family name' : nname,
               'brand':nbrand,
               'a major operator': nmajoroperators,
               'produced from': nproducedfrom,
               'production ended': nproductionended,
               'first flight': nfirstflight,
               'number of variants' : nvariants,
               'most popular variant' : nmostpopularvariant,
               'max range variant' : [nmaxrangevariant, nmaxrangevariantv],
               'max capacity variant' : [nmaxcapacityvariant, nmaxcapacityvariantv],
               'aircraft class' : naircraftclass,
               'most common engine' : nenginesoffered,
               'total orders' : ntotalorders
          }
          print('\n')
          print("We've created a new dictionary of the aircraft based on the information you entered:")
          print(newaircraft)
          listofaircraftfamilies.append(str(newaircraft['aircraft family name']))
          print("\n")
          print("This is the list of aircraft families in the program now:")
          print(listofaircraftfamilies)
          mostpopularvariants.append(newaircraft['most popular variant'])
          Utotalorders = Utotalorders + newaircraft['total orders']
     #else: 
          #newaircraft = { 'total orders': 0}

     #The following code asks the user what their favorite airliner is and adds it into the airliners list (#8)

     favoritea = input("Which one is your favorite aircraft?")
     airliners['favorite'] = favoritea
#     if favoritea == "A320":
#          airliners['favorite'] = 'A320'
#     if favoritea == "B777":
#          airliners['favorite'] = "B777"
#     if favoritea == "B787":
#          airliners['favorite'] = "B787"
#     if favoritea == "B747":
 #         airliners['favorite'] = "B747"
 #    if favoritea == "A330":
 #         airliners['favorite'] = "A330"
 #    if favoritea == "A350":
 #         airliners['favorite'] = "A350"
  #   if favoritea == "A380":
  #        airliners['favorite'] = "A380"

     print("Stored")
     print("\n")


     #This gets the most popular variants out of dictionaries and places it into one list (#9)
     print("These are the most popular variants of the all the aircraft families in the dictionaries:")

     
     #This prints out the list using a for loop (#10)
     for index in range(len(mostpopularvariants)):
          print(mostpopularvariants[index])


     #This adds an item to the list and removes an item from the list (#11)
     #mostpopularvariants.append('B767-300')
     #mostpopularvariants.remove(A330['most popular variant'])

     print("\n")


     #This uses math to add up the total orders across all aircraft families and displays it (#13)
     print("These are the orders of all the aircraft families in the dictionary summed up together:")
     print(Utotalorders)
     #This uses modulus to determine whether the number of orders is odd or even (#14)
     if Utotalorders % 2 == 0:
          print("The total amount of orders across all aircraft is even.")
     else:
          print("The total amount of orders across all aircraft is odd.")

     print("\n")


     #This displays the modified dictionary (#12)
     print("This is the modified dictionary")
     print(airliners)
     print("\n")

     #This displays the modified list (#12)
     print("This is the modified list")
     print(mostpopularvariants)
     print("\n")


     
  



     #This asks the user if they want the program to run again and runs again if they say yes (#6)
     print("Run again?")
     rerun = str(input("y/n: "))
     if rerun == "y" or rerun == "Y":
          rerun = 0
     else:
          rerun = 1
          print("Goodbye!")
