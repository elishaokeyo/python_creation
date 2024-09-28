# students performance scenario 
# comparison and logical operators 

# marks=78 
marks= float(input("enter student marks:"))

if marks< 30:
    print("below average")
elif marks>=30 and marks<40:
    print("average")    
elif marks>=40 and marks<70:
    print("above average")    
else:
    print("excellent") 
    if marks==100:
        print("you will get an award")
