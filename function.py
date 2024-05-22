#simple function
def greet():
 print('Hello world!')

greet()


#function with parameter
def greet_with_name(name):
  print(f"Hello {name}")

greet_with_name("Kaeng")

# 변수명 name = "Hyojoo"
#name : parameter "Hyojoo" : Argumente
#parameter는 함수에 전달된 데이터의 이름이고 Argumente는 그 데이터의 실제 값 


def greet_with(name, location):
  print(f"Hello {name}")
  print(f"what ist it like in {location}")

# 변수명을 써주는게 변수값을 헷갈리지 않고 출력할 수 있게 해줌 
greet_with(name = "Kaeng Kaeng", location="Berlin")

#########
import math

w = int(input())
h = int(input())

coverage = 5  # Cans of paint needed per unit area

def paint(w, h, cover):
  area = w * h  # Calculate the total area to be painted
  cans_needed = math.ceil(area / cover)  # Round up the number of cans
  print(f"You will need {cans_needed} cans of paint.")

paint(w, h, coverage)  # Call the paint function

########
def prime_checker(num):

 is_Prime = True

 for i in range(2,num):
  if num % i == 0 : 
    is_Prime = False 
 if is_Prime :
    print("Yes, It's correct")
 else :
    print("Sorry, It's not correct")

n = int(input())
prime_checker(n)
  
               
