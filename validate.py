def checkLength(str, start, end):
  if len(str) <= end and len(str) >= start:
    return True
  else:
    return False

def checkStartsWithLetter(str):
  for alphabet in "abcdefghijklmnopqrstuvwxyz":
    if str[0].lower() == alphabet:
      return True
  return False
  
def containsLNU(str):
  #Contains Letter, Number, Dash or Underscore (only)
  counter = 0
  for letter in str:
      for alphabet in "abcdefghijklmnopqrstuvwxyz":
        if letter.lower() == alphabet:
          counter+=1
      for number in range(0,10):
        if letter == number:
          counter+=1
      if letter == '_' or letter == '-':
        counter+=1
      if counter == 0:
        return False
      counter = 0
  return True

def endsWithUnderScore(str):
  if str[len(str)-1] == "_":
    return True
  else:
    return False

def validateUsername(str):
  if checkLength(str, 4, 25) and checkStartsWithLetter(str) and containsLNU(str) and not endsWithUnderScore(str):
    return 'true'
  else:
    return 'false'

while True:
	print("Write the username you wish to validate")
	print(validateUsername(input()))
