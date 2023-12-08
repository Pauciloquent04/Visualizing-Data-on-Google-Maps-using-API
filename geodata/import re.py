import re

hand=open('mbox-short.txt')
# for line in hand:
#     line=line.rstrip()
#     if re.search('^From:',line): # '^' means startswith 
#         print(line)
# for line in hand:
#     line=line.rstrip()
#     # if re.search('^X.*:',line): # '.' means any character '*' means 0 or more occurance of character before it
#     if re.search('^X-\S+:',line): # '\S' means any non-space char '+' means 1 or more occurance
#         print(line)

s='Tkg 8 fytdy 86 huyv 976 h6 jg 6 88'
num=re.findall('[0-9]',s)
num1=re.findall('[0-9]+',s)
num2=re.findall('[0-9]*',s)
print(num)
print(num1)
print(num2)

# x= 'From: Using the : character'
# y=re.findall('^F.+:',x) # '+' is greedy, i.e, it will return the largest maching string
# z=re.findall('^F.+?:',x) # '?' makes 'x' non-greedy, i.e, it will return the smallest maching string
# print(y)
# print(z)

# x= 'Email: rishi.arora763@gmail.com this is my email.'
# y=re.findall('\S+@\S+\.\S+',x)
# z=re.findall('^Email: (\S+@\S+\.\S+)',x) # expression under paranthesis will be stored and expression under '' will be matched
# host=re.findall('@([^ ]*)',x) # '^' under [] means not operator. Here it means @ followed by 0 or more non space char and return char under ()
# print(y)
# print(z)
# print(host)

# x="erk refmn $1de $10.00 $dd 3efe"
# y= re.findall('\$[0-9.]+',x)
# print(y)