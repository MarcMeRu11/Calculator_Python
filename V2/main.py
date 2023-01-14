#Librería math para realizar operaciones complejas.
import math
import os
#Creación de la variables para su posterior uso
ans=None
pos = []
parent = ")"
pi_num = math.pi
ot= None
#FUNCIONES
#____________________________________________________________________________________________________________________________________
def fun_cos():
    global ot
    global parent 
    global pos 
    global pi_num

    #Detección de la primera parte del coseno.
    pos_pre_cos = ot.find("cos(")
    pos_cos = pos_pre_cos + 4 

    #detección de todos los paréntesis de cierre.
    i_cos = ot.find(parent)
    while i_cos != -1:
        pos.append(i_cos)
        i_cos = ot.find(parent, i_cos + 1)
    
    #selección del paréntesis de cierre.
    if len([x for x in pos if x > pos_cos]) > 0:
        cierre_cos = min([x for x in pos if x > pos_cos])

        #Extracción el ángulo.
        angulo_cos = ot[pos_cos : cierre_cos]

        #Transformación del ángulo a radianes.
        angulo_cos_rad = (float(angulo_cos) * float(pi_num))/float(180)
        
        #Cálculo del coseno.
        resul_cos = math.cos(angulo_cos_rad)
        resul_cos = round(resul_cos,10)

        #Reemplazo del coseno en la string original por el resultado
        delete_cos = str(angulo_cos) + ")"
        ot = ot.replace("cos(", str(resul_cos))
        ot = ot.replace(delete_cos, "")

#Funcion para el seno.
def fun_sen():
    global ot
    global parent 
    global pos 
    global pi_num

    #Detección de la primera parte del seno.
    pos_pre_sen = ot.find("sen(")
    pos_sen = pos_pre_sen + 4 

    #detección de todos los paréntesis de cierre.
    i_sen=ot.find(parent)
    while i_sen != -1:
        pos.append(i_sen)
        i_sen = ot.find(parent, i_sen + 1)
    
    #selección del paréntesis de cierre.
    if len([x for x in pos if x>pos_sen]) > 0:
        cierre_sen = min([x for x in pos if x>pos_sen])

        #Extracción el ángulo.
        angulo_sen = ot[pos_sen:cierre_sen]

        #Transformación del ángulo a radianes.
        angulo_sen_rad = (float(angulo_sen)*float(pi_num))/float(180)
        
        #Cálculo del coseno.
        resul_sen = math.sin(angulo_sen_rad)
        resul_sen = round(resul_sen,10)

        #Reemplazo del coseno en la string original por el resultado.
        delete_sen = str(angulo_sen) + ")"
        ot = ot.replace("sen(",str(resul_sen))
        ot = ot.replace(delete_sen,"")

#Funcion para la tangente.


#   BUCLE
#______________________________________________________________________________________________________________________________________
while True:
    o = input("Calculator: ")

    #arreglo del string para que sea posible usar la función eval().
    ot = o.replace("x", "*")
    ot = ot.replace("^","**")  

    try:
        #Detección de cosenos.
        if ot.find("cos(") != -1:
            fun_cos()
        
        #Detección de cosenos.
        if ot.find("sen(") != -1:
            fun_sen()

        #Cálculo de la operación, registro de la variable y print del resultado.
        result = eval(ot)
        ans=result
        print(o,"=", result)

    #except en caso de que la operación sea mal escrita y de error.
    except NameError:
        print("Sintax error.")
    except ValueError:
        print("Sintax error.")
    except:
        print("Error.")
    
    zzz= input("continue...")