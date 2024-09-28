# using for loop in list 
languages=["english", "kiswahili", " french", "spanish", "germany"]
for english in languages:
    print(english)


countries=["kenya", "uganda", "tanzania","somalia", "ethiopia"]    
for country in countries:
    print(country)


# loop through countries and print those starting with same alphabet 
countries=["kenya", "kuwait", "turkey", "uganda", "tanzania","somalia", "ethiopia"]   

startingwithk= "e"
for country in countries:
    if country.startswith(startingwithk):
      print(country)
    