a = "My naMe is Sudish kaRki !"
print(len(a))      #string ko lenght
print(a.upper())     #sabai capital banauxa
print(a.lower())       # sabai small banauxa
print(a.rstrip("!"))      #diyeko last ko string hatauxa
print(a.strip())         #aagadi ko space hatauxa
print(a.replace("Sudish", "Suraj"))      #diyeko string lai naya string ma change garxa
print(a.split(" "))      #sabai string lai cotation ma lauxa
print(a.capitalize())     #word lai proper banauxa
print(a.center(50))     #string lai aagadi space dera center ma lauxa
print(a.count("a"))          #tyo word kati ota x dekhauxa
print(a.endswith(" !"))        #last ma deko string xa ki nai herna milxa if xa true if xaina false
print(a.endswith("is", 9, 10))  #yo index ma deko word xa ki naii dekhauxa
print(a.find("s"))      #yo wor kun index ma x dekhauxa aani naa vako halo vani -1 dekhauxa
print(a.index("s"))      #yo wor kun index ma x dekhauxa aani naa vako halo vani error dekhauxa
print(a.isalnum())      #A dekhin Z samma ra 1 dekhin 9 samma matra hunu paro string ma na vaye false dekhauxa 
print(a.isalpha())      #A dekhin Z samma ra a dekhin z samma matra hunu paro string ma na vaye false dekhauxa 
print(a.islower())      #check garxa sbaai letter small ma xa ki nai if xa true if 1ta ni capital xa false
print(a.isupper())      #check garxa sbaai letter capital ma xa ki nai if xa true if 1ta ni small xa false
print(a.isprintable())      #deko  string printable xa ki nai ifn xa true if xaina false
print(a.isspace())      #white space xa vani true navaye false
print(a.istitle())      #Sabai string ko 1st letter capital hunu paro xaina vani false xa vani true
print(a.startswith("My"))      #1st letter ma yo string xa ki nai if xa true if xaina false
print(a.swapcase())      #Capital word lai small  ani small lai capital ma change garxa
print(a.title())      #Sabai string ko 1st letter lai capital ma change garxa if bich ma capital xa vani teslai small ma ni change garxa

