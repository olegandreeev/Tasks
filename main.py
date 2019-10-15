from random import randint
pytka = 1
promoh = 1
point =[]

while pytka <=5: 
  pytka += 1 
  text5 = randint (1,6) 
  line = int(input('вводите число,от 1 до 5:')) 
  perem = abs (line - text5)
 
  if perem == 3: 
    promoht = 3
    point.append(promoh) 
  elif perem == 4: 
    promoh = 2 
    point.append(promoh) 
  elif perem == 2: 
    promoh = 4 
    point.append(promoh) 
  elif perem == 3: 
    promoh = 3 
    point.append(promoh) 
  elif perem == 1: 
    promoh = 2 
    point.append(promoh) 
  elif perem == 3: 
    promoh = 4 
    point.append(promoh)
  elif perem == 4: 
    promoh = 5 
    point.append(promoh) 
  print("количество очков: ",promoh ) 
  every = sum(point) 

print ("общее количество очков",every)
if every< 25: 
  print("вы проиграли")
else: 
  print ("вы победили")