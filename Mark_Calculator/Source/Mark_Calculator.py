import time

#-----------

def CalculateNewMark(mark1,markbase1,markbase2):
  return (mark1*markbase2)/markbase1

def Introduction():
  print("Welcome to Mark Calculator. You will be able to convert an old mark to its equivalent with another base.\nFor example, the program will return you 19.6/20 if you entered that you wanted your old grade equivalent on 20, from 98/100. Decimal numbers are rounded to the first digit.")

#-----------

Introduction()
time.sleep(1)
while True:
  markone = input("\n--------------------------\nEnter your mark below. For example, it represents the 19 in 19/20.\n>>>\t")
  markbaseone = input("\nEnter your mark base below. For example, it represents the 20 in 19/20.\n>>>\t")
  markbasetwo = input("\nEnter the mark base you want below. For example, it represents the 100 in x/100, in the second grade you want.\n>>>\t")
  try:
    markone = round(float(markone),1)
    markbaseone = round(float(markbaseone),1)
    markbasetwo = round(float(markbasetwo),1)
  except ValueError:
    print("Error converting your inputs into numbers. Please enter valid numbers (Examples : 19.3 / 344 / 63).")
  marktwo = round(CalculateNewMark(markone, markbaseone, markbasetwo),1)

  if markone.is_integer() == True:
    markone = int(markone)
  if markbaseone.is_integer() == True:
    markbaseone = int(markbaseone)
  if marktwo.is_integer() == True:
    marktwo = int(marktwo)
  if markbasetwo.is_integer() == True:
    markbasetwo = int(markbasetwo)

  print("\n* The mark "+str(markone)+"/"+str(markbaseone)+" represents "+str(marktwo)+"/"+str(markbasetwo))
  time.sleep(2)
