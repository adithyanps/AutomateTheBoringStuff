birthdays={'alice':'apr 1','bob':'jan 12','carol':'feb 6' }
while True:
  print 'enter the name :(blank to quit)'
  name = input()
  if name == '':
   break
  if name in birthdays:
   print birthdays[name] + 'is the birthday of ' + name
  else:
   print 'i dont have birthday information for' + name
   print 'what is their birthday'
   bday=input()
   birthdays[name]=bday
   print 'birthday database is updated'

