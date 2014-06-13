import re
import code

def locator(m,secondnum):
  for row in m:
    secondnum +=1
    firstnum = -1
    columnrange = len(row)
    for letter in range( ord('a'), columnrange + ord('a') ):
      letter = chr(letter) + str(m.index(row))
    for items in row:
      firstnum += 1
      letter = m[secondnum][firstnum]
      beautify(m,letter,secondnum, firstnum)

def beautify(m, letter, secondnum, firstnum):
  if isinstance(letter, basestring):
    m[secondnum][firstnum] =  re.sub("=", '', letter)
    m[secondnum][firstnum] = m[secondnum][firstnum].lower()
    letter = m[secondnum][firstnum]
    number_connector_and_cell_split(letter,m, secondnum, firstnum)

def number_connector_and_cell_split(letter, m, secondnum, firstnum):
  if any(char.isalpha() for string in letter for char in string) == False :
    m[secondnum][firstnum] = str(eval("".join(m[secondnum][firstnum])))
  if any(char.isalpha() for string in letter for char in string) :
    while any(characters.isalpha() for characters in letter) :
      letter = re.split("([+-/*])", letter.replace(" ", ""))
      seperate_nums_letters(m,letter, secondnum, firstnum)
  else:
    number_value_setter(letter, m, secondnum, firstnum)

def seperate_nums_letters(m,letter, secondnum, firstnum):
  for item in letter:
    if isinstance(item, basestring):
      match = re.match(r"([a-z]+)([0-9]+)", item, re.I)
      if match:
        items = match.groups()
        item_letter = ord(items[0])-97
        item_number = int(items[1])-1
        letter_value_setter(m,letter,item, item_number, item_letter, secondnum, firstnum)

def letter_value_setter(m,letter,item,item_number,item_letter, secondnum, firstnum):
  for index, value in enumerate(letter):
    if value == item:
      try:
        letter[index] =  str(m[item_number][item_letter])
      except (RuntimeError, TypeError, NameError, IndexError):
        print("Oops! One (or more) of your cells contains an invalid reference.")
        raise ReferenceError
  number_value_setter(letter, m, secondnum, firstnum)

def number_value_setter(letter,m, secondnum, firstnum):
  if any(char.isalpha() for string in letter for char in string) == False :
    if len(letter) > 1:
      try:
        m[secondnum][firstnum] = int(eval("".join(letter)))
      except SyntaxError:
        print("Oops! One (or more) of your cells contains an invalid reference.")
        raise ValueError
    else:
      m[secondnum][firstnum] = int(eval("".join(letter)))
  else:
    number_connector_and_cell_split(letter, m, secondnum, firstnum)

def stringify(m, letter):
  for lists in m:
    for index, value in enumerate(lists):
      lists[index] = int(value)

def evaluate(m):
    secondnum = -1
    locator(m,secondnum)
    try:
      for lists in m:
        for index, value in enumerate(lists):
          lists[index] = int(value)
      return m
    except ValueError:
      print("Oops! One (or more) of your cells contains an invalid reference...maybe an infinite loop?")
      raise ValueError


mini_spreadsheet = [
  [1,     "=A1+1", "=A1 + B1"],
  ["=B1", "3",     "=C1 + B2"],
  ["A1", "=B1+A1", "C2 + B3", "= A3 + B3 + C3"]
]

mini_spreadsheet2 = [
  [1,     "=A1+1", "=A1 + B1"],
  ["=B1", "3",     "=C1 * B2"],
  ["A1", "=B1+A1", "C2 + B3", "= A3 + B3 + C3"]
]

mini_spreadsheet3 = [
  [1,     "=A1+1", "=A1 + B1"],
  ["=B1", "3",     "=C1 * B2"],
  ["A1", "=B1*A1", "C2 + B3", "= A3 * B3 * C3"]
]
print evaluate(mini_spreadsheet)
print evaluate(mini_spreadsheet2)
print evaluate(mini_spreadsheet3)