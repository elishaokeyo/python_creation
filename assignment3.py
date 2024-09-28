grossincome=float(input("gross income"))

if grossincome <=5999:
    print("monthly contribution:150")
elif grossincome >=6000 and grossincome<7999:
     print("monthly contribution:300") 
elif grossincome >=8000 and grossincome<11999:
     print("monthly contribution:400")    
elif grossincome >=12000 and grossincome<14999:
     print("monthly contribution:500")  
elif grossincome >=15000 and grossincome<19999:
     print("monthly contribution:600")    
elif grossincome >=20000 and grossincome<24999:
     print("monthly contribution:750") 
elif grossincome >=25000 and grossincome<29999:
     print("monthly contribution:850")      
elif grossincome >=30000 and grossincome<49999:
     print("monthly contribution:1000")    
elif grossincome >=50000 and grossincome<99999:
     print("monthly contribution:1500")   
else:
     print("monthly contribution:2000")





