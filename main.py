#function for run the program again
def use_again():
  #str with English and Portuguese possible answers
  yes = "yessim"
  no = "nonãonao"
  ans = input("-> Use again? ")
  ans = ans.lower()
  if ans in yes:
    return True
  elif ans in no:
    return False


use = True
while use == True:
  signs = "+-*/"

  #data entry
  print("===CALCULATOR===")
  phrase = str(input("-> "))

  #finding the operation sign and its index
  op_exists = False
  for character in phrase:
    if character in signs:
      op_exists = True 
      idx_op = phrase.index(character)
      op = phrase[idx_op] 
  
  #testing the operador existence
  if op_exists == True:
    #defining the operation numbers
    n1 = float(phrase[0:idx_op])
    n2 = float(phrase[idx_op+1:len(phrase)])

    #operations tests and final results
    if op == "+":
      ans = n1 + n2
      print("=", ans)
    elif op == "-":
      ans = n1 - n2
      print("=", ans)
    elif op == "*":
      ans = n1 * n2
      print("=", ans)
    elif op == "/":
      ans = n1 / n2
      print("=", ans)
  else:
    print("Syntax ERROR")

  #use again function
  print("================")
  print("")
  use = use_again()
  print("")