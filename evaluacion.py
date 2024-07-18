import os   
import random 
Trabajadores = ["Juan perez", "Maria Garcia", "Carlos Lopez", "Ana Martinez", "Pedro Rodriguez", "Laura Hernandez" , "Miguel Sanchez" , "Isabel Gomez", "Francisco Diaz", "Elena Fernandez"]
sueldos={}
def asignar_sueldos_aleatorios(Trabajadores):
    sueldos={trabajador:random.randint(300000,2500000) for trabajador in Trabajadores}
    print("sueldos aleatorios")
    for trabajador, sueldo in sueldos.items():
     print(f"trabajadores:sueldos")
     return sueldos   
def clasificar_sueldo(sueldos):
     clasificar_sueldos={"menores a $800000":[], "entre $8000000 y $2000000":[], "superiores a $2000000":[]}
for trabajador, sueldo in sueldos.items():
     if sueldo < 800000:
    clasificacion["menores a 800000"].append((trabajador,sueldo))
sueldo > 2000000

def sueldo_liquido(sueldo):
    return sueldo-sueldo*0.07-sueldo*0.12
def menu():
   print("Menu principal")
print("1.Asignar sueldos aleatorios")
print("2.Clasificar Sueldos")
print("3.ver estadisticas")
print("4.Reporte de sueldos")
print("5.Salir del programa")
while True:
    opc=menu{["Menu Principal":, "1.Asignar Sueldos aleatorios","2.Clasificar sueldos","3.Ver Estadisticas","4.Reporte de sueldos","5.Salir del programa"]}:
    if opc==1:
            asignar_sueldos_aleatorios()
    elif opc==5:
     print("Finalizando programa.....")
     print("Desarrollado por Carlos Vergara")
     print("12.345.678-9")
     exit 
      
    

             

