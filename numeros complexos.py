import cmath 

print ("3 números complexos:") 
print ("Z1: ",end="") 
print (complex(1,2)) 
print ("Z2: ",end="") 
print (complex(3,4)) 
print ("Z3: ",end="") 
print (complex(5,6)) 

print ("") 
print ("") 
print ("Soma:") 
z = complex(1,2) + complex(3,4) + complex(5,6); 
print ("real: ",end="") 
print (z.real) 
  
print ("img: ",end="") 
print (z.imag) 


print ("") 
print ("") 
print ("Subtração:") 
z = complex(1,2) - complex(3,4) - complex(5,6); 
print ("real: ",end="") 
print (z.real) 
  
print ("img: ",end="") 
print (z.imag) 


print ("") 
print ("") 
print ("Multiplicação:") 
z = complex(1,2) * complex(3,4) * complex(5,6); 
print ("real: ",end="") 
print (z.real) 
  
print ("img: ",end="") 
print (z.imag) 

print ("") 
print ("") 
print ("Divisão:") 
z = complex(1,2) / complex(3,4) / complex(5,6); 
print ("real: ",end="") 
print (z.real) 
  
print ("img: ",end="") 
print (z.imag) 
 