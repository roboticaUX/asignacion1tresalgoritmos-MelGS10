#Recibir tres números y ordenarlos de mayor a menor, se debe validar que no existan números iguales
print("Ingresar primer numero: ")
n1=int(input())
print("Ingresar segundo número: ")
n2=int(input())
print("Ingresar tercer número: ")
n3=int(input())

if(n1>n2 and n2<n3):
    print("",n1,",",n2,",",n3)
elif(n2>n1 and n1>n3):
    print("",n2,",",n1,",",n3)
elif(n3>n1 and n1>n2):
    print("",n1,",",n2,",",n3)
elif(n3>n2 and n2>n1):
    print("",n3,",",n2,",",n1)
elif(n1>n3 and n3>n2):
    print("",n1,",",n3,",",n2)
elif(n2>n3 and n3>n1):
    print("",n2,",",n3,",",n1)    
else:
    print("Usted ingreso numeros iguales")