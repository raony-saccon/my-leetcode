from constants import integers

def int_to_roman(input):
  num = input
  roman = ""
  for n in integers:
    while num >= int(n):
      roman += integers[n]
      num -= int(n)
  return roman