dictionary={"one":"1","two":"2","three":"3"}

print(dictionary.get(input("enter key")))

while True:
 
 newkey=str(input("enter key"))
 if newkey=="q"  :
  break
 
 newvalue=str(input("enter value"))
 
 dictionary.update({newkey:newvalue})

 

print(dictionary.items())