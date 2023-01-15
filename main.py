#Libreria math para realizar operaciones complejas.
import math
import os
#Creacion de la variables para su posterior uso.
ans = None
pos = []
parent = ")"
pi_num = math.pi
ot = None
count = 1
#FUNCIONES
#____________________________________________________________________________________________________________________________________
#TRIGONOMETRICAS
#Funcion para el seno.
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

#Función para la tangente.
def fun_tg():
    global ot
    global parent 
    global pos 
    global pi_num

    #Detección de la primera parte del coseno.
    pos_pre_tg = ot.find("tg(")
    pos_tg = pos_pre_tg + 3 

    #detección de todos los paréntesis de cierre.
    i_tg = ot.find(parent)
    while i_tg != -1:
        pos.append(i_tg)
        i_tg = ot.find(parent, i_tg + 1)
    
    #selección del paréntesis de cierre.
    if len([x for x in pos if x > pos_tg]) > 0:
        cierre_tg = min([x for x in pos if x > pos_tg])

        #Extracción el ángulo.
        angulo_tg = ot[pos_tg : cierre_tg]

        #Transformación del ángulo a radianes.
        angulo_tg_rad = (float(angulo_tg) * float(pi_num))/float(180)
        
        #Cálculo del coseno.
        resul_tg = math.tan(angulo_tg_rad)
        resul_tg = round(resul_tg,10)

        #Reemplazo del coseno en la string original por el resultado
        delete_tg = str(angulo_tg) + ")"
        ot = ot.replace("tg(", str(resul_tg))
        ot = ot.replace(delete_tg, "")

#Función para el arcocoseno.
def fun_acos():
    global ot
    global parent 
    global pos 
    global pi_num

    #Detección de la primera parte del arcocoseno.
    pos_pre_acos = ot.find("acos(")
    pos_acos = pos_pre_acos + 5 

    #detección de todos los paréntesis de cierre.
    i_acos = ot.find(parent)
    while i_acos != -1:
        pos.append(i_acos)
        i_acos = ot.find(parent, i_acos + 1)
    
    #selección del paréntesis de cierre.
    if len([x for x in pos if x > pos_acos]) > 0:
        cierre_acos = min([x for x in pos if x > pos_acos])

        #Extracción el ángulo.
        valor_acos = ot[pos_acos : cierre_acos]
        
        #Cálculo del arcocoseno.
        resul_acos = math.acos(float(valor_acos))

        #Transformación de radianes a grados.
        resul_acos_grad = ((float(resul_acos)*180)/float(pi_num))

        #Reemplazo del arcocoseno en la string original por el resultado
        delete_acos = str(valor_acos) + ")"
        ot = ot.replace("acos(", str(resul_acos_grad))
        ot = ot.replace(delete_acos, "")

#Función para el arcoseno.
def fun_asen():
    global ot
    global parent 
    global pos 
    global pi_num

    #Detección de la primera parte del arcocoseno.
    pos_pre_asen = ot.find("asen(")
    pos_asen = pos_pre_asen + 5 

    #detección de todos los paréntesis de cierre.
    i_asen = ot.find(parent)
    while i_asen != -1:
        pos.append(i_asen)
        i_asen = ot.find(parent, i_asen + 1)
    
    #selección del paréntesis de cierre.
    if len([x for x in pos if x > pos_asen]) > 0:
        cierre_asen = min([x for x in pos if x > pos_asen])

        #Extracción el ángulo.
        valor_asen = ot[pos_asen : cierre_asen]
        
        #Cálculo del arcocoseno.
        resul_asen = math.asin(float(valor_asen))

        #Transformación de radianes a grados.
        resul_asen_grad = ((float(resul_asen)*180)/float(pi_num))

        #Reemplazo del arcocoseno en la string original por el resultado
        delete_asen = str(valor_asen) + ")"
        ot = ot.replace("asen(", str(resul_asen_grad))
        ot = ot.replace(delete_asen, "")

#Función para la arcotangente.
def fun_atg():
    global ot
    global parent 
    global pos 
    global pi_num

    #Detección de la primera parte del arcocoseno.
    pos_pre_atg = ot.find("atg(")
    pos_atg = pos_pre_atg + 4 

    #detección de todos los paréntesis de cierre.
    i_atg = ot.find(parent)
    while i_atg != -1:
        pos.append(i_atg)
        i_atg = ot.find(parent, i_atg + 1)
    
    #selección del paréntesis de cierre.
    if len([x for x in pos if x > pos_atg]) > 0:
        cierre_atg = min([x for x in pos if x > pos_atg])

        #Extracción el ángulo.
        valor_atg = ot[pos_atg : cierre_atg]
        
        #Cálculo del arcocoseno.
        resul_atg = math.atan(float(valor_atg))

        #Transformación de radianes a grados.
        resul_atg_grad = ((float(resul_atg)*180)/float(pi_num))

        #Reemplazo del arcocoseno en la string original por el resultado
        delete_atg = str(valor_atg) + ")"
        ot = ot.replace("atg(", str(resul_atg_grad))
        ot = ot.replace(delete_atg, "")


#   BUCLE
#______________________________________________________________________________________________________________________________________
while True:
    
    print("Operation num", str(count) + ".")
    o = input("Calculator: ")

    #arreglo del string para que sea posible usar la función eval().
    ot = o.replace("x", "*")
    ot = ot.replace("^","**")  

    try:

        #Detección de arcocosenos.
        if ot.find("acos(") != -1:
            fun_acos()

        #Detección de arcosenos.
        if ot.find("asen(") != -1:
            fun_asen()    

        #Detección de arcotangentes.
        if ot.find("atg(") != -1:
            fun_atg() 

        #Detección de cosenos.
        if ot.find("cos(") != -1:
            fun_cos()
        
        #Detección de cosenos.
        if ot.find("sen(") != -1:
            fun_sen()

        #Detección de tangentes.
        if ot.find("tg(") != -1:
            fun_tg()

        #Cálculo de la operación, registro de la variable y print del resultado.
        result = eval(ot)
        ans=result
        print(o,"=", result)
        count += 1

    #except en caso de que la operación sea mal escrita y de error.
    except NameError:
        print("Sintax error.")
    except ValueError:
        print("Sintax error.")
    except:
        print("Error.")
    
    print("____________________________________________")