import math 
parent = ")"
ot = "cos(cos())"
pos = []
pi_num = math.pi

pos_pre_cos = ot.find("cos(")
pos_cos = pos_pre_cos + 4 

    #detección de todos los paréntesis de cierre.
i_cos=ot.find(parent)
while i_cos != -1:
        pos.append(i_cos)
        i_cos = ot.find(parent, i_cos + 1)
    
    #selección del paréntesis de cierre.
if len([x for x in pos if x>pos_cos]) > 0:
        cierre_cos = min([x for x in pos if x>pos_cos])

        #Extracción el ángulo.
        angulo_cos = ot[pos_cos:cierre_cos]

        #Transformación del ángulo a radianes
        angulo_cos_rad = (float(angulo_cos)*float(pi_num))/float(180)
        
        #Cálculo del coseno.
        resul_cos = math.cos(angulo_cos_rad)
        resul_cos = round(resul_cos,10)

        #Reemplazo del coseno en la string original por el resultado
        delete_cos = str(angulo_cos) + ")"
        ot = ot.replace("cos(",str(resul_cos))
        ot = ot.replace(delete_cos,"")


print(ot)