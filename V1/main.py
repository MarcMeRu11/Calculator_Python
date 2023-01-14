ans=None
while True:
  o = input("Calculator: ")
  ot = o.replace("x", "*")
  ot = ot.replace("^","**")
  try:
    result = eval(ot)
    ans=result
    print(o,"=", result)
  except:
    print("Error.")