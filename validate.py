def checkLength(text, start, end):
  if len(text) <= end and len(text) >= start:
    return True
  else:
    return False

def checkStartsWithLetter(text):
  for alphabet in "abcdefghijklmnopqrstuvwxyz":
    if text[0].lower() == alphabet:
      return True
  return False
  
def containsLNU(text):
  #Contains Letter, Number, Dash or Underscore (only)
  counter = 0
  for letter in text:
      for alphabet in "abcdefghijklmnopqrstuvwxyz":
        if letter.lower() == alphabet:
          counter+=1
      for number in range(0,10):
        if str(letter) == str(number):
          counter+=1
      if letter == '_' or letter == '-':
        counter+=1
      if counter == 0:
        return False
      counter = 0
  return True

def endsWithUnderScore(text):
  if text[len(text)-1] == "_":
    return True
  else:
    return False

def validateUsername(text):
  if checkLength(text, 4, 25) and checkStartsWithLetter(text) and containsLNU(text) and not endsWithUnderScore(text):
    return True
  else:
    return False

while True:
	print("Write the username you wish to validate")
	print(validateUsername(input()))
