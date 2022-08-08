list_of_numbers = [3, 66, 20, 5, 200, 81, 95, 150, 160]

for number in list_of_numbers :
  if number > 150:
     break
  else:
     if number % 5 == 0 :
        print(number)
     else:
      print(f"{number} is not divisable by 5")