# dgs -> digits
# rn  -> reversed numbers
# on  -> original number
# n   -> number

def is_palindrome_number(on):
  dgs=[]
  n=on
  if(n<0):return False    
  while (n>0):
    dgs.append(int(n%10))
    n=(n-n%10)/10
  for i in range(len(dgs)):
    n=int(n*10+dgs[i])
  return n==on

print(is_palindrome_number(-232))