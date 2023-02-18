'''
Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score. You are given 
scores. Store them in a list and find the score of the runner-up.

Input Format: The first line contains n. The second line contains an array A[] of n integers each separated by a space.

Constraints: 

2 <= n <= 10
-100 <= A[i] <= 100

Output Format: Print the runner-up score.

Sample Input 0: 2 3 6 6 5
Sample Output 0: 5
Explanation 0: Given list is [2,3,6,6,5]. The maximum score is 6, second maximum is 5. Hence, we print 5 as the runner-up score.
'''

participants=''
while participants.isnumeric() == False or (participants.isnumeric() == True and (int(participants) < 2 or int(participants) > 10)):
        participants=input("Ingrese el número de participantes: ")

scores=[]
data= ''
champion=[]
runnerUp=[]

while len(scores) != int(participants) or data.isnumeric() == False:
    data = input('Ingresa las calificaciones de los participantes: \n')
    if data.isnumeric() == False: 
        continue
    elif int(data) < -100 or int(data) > 100:
        data = input('La calificacion tiene que estar entre -100 y 100, ingresela nuevamente: \n')
    else: 
        scores.append(int(data))

scores.sort(reverse=True)

for i in range(len(scores)):
    if len(champion) == 1 and len(runnerUp) == 1:
        if scores[i] >= champion[0]:
            champion.pop(0)
            champion.append(scores[i])
        elif scores[i] >= runnerUp[0]:
            runnerUp.pop(0)
            runnerUp.append(scores[i])
    elif len(champion) == 1 and len(runnerUp) == 0:
        if scores[i] >= champion[0]:
            champion.pop(0)
            champion.append(scores[i])
        else:
            runnerUp.append(scores[i])
    else:
        champion.append(scores[i])

print(runnerUp[0])

IF(AND(INCLUDES({!Obtiene_CV.ERPvs__A_cuenta_y_orden_de__r.Dias_de_Exclusion_de_Facturacion_SE__c}, "01"), LPAD(TEXT(DAY({!Obtiene_MF.ERPvs__Fecha__c})), 2, "0") = "01"), true,
IF(AND(INCLUDES({!Obtiene_CV.ERPvs__A_cuenta_y_orden_de__r.Dias_de_Exclusion_de_Facturacion_SE__c}, "02"), LPAD(TEXT(DAY({!Obtiene_MF.ERPvs__Fecha__c})), 2, "0") = "02"), true,
IF(AND(INCLUDES({!Obtiene_CV.ERPvs__A_cuenta_y_orden_de__r.Dias_de_Exclusion_de_Facturacion_SE__c}, "03"), LPAD(TEXT(DAY({!Obtiene_MF.ERPvs__Fecha__c})), 2, "0") = "03"), true,
IF(AND(INCLUDES({!Obtiene_CV.ERPvs__A_cuenta_y_orden_de__r.Dias_de_Exclusion_de_Facturacion_SE__c}, "04"), LPAD(TEXT(DAY({!Obtiene_MF.ERPvs__Fecha__c})), 2, "0") = "04"), true,
IF(AND(INCLUDES({!Obtiene_CV.ERPvs__A_cuenta_y_orden_de__r.Dias_de_Exclusion_de_Facturacion_SE__c}, "05"), LPAD(TEXT(DAY({!Obtiene_MF.ERPvs__Fecha__c})), 2, "0") = "05"), true,
IF(AND(INCLUDES({!Obtiene_CV.ERPvs__A_cuenta_y_orden_de__r.Dias_de_Exclusion_de_Facturacion_SE__c}, "06"), LPAD(TEXT(DAY({!Obtiene_MF.ERPvs__Fecha__c})), 2, "0") = "06"), true,
IF(AND(INCLUDES({!Obtiene_CV.ERPvs__A_cuenta_y_orden_de__r.Dias_de_Exclusion_de_Facturacion_SE__c}, "07"), LPAD(TEXT(DAY({!Obtiene_MF.ERPvs__Fecha__c})), 2, "0") = "07"), true,
IF(AND(INCLUDES({!Obtiene_CV.ERPvs__A_cuenta_y_orden_de__r.Dias_de_Exclusion_de_Facturacion_SE__c}, "08"), LPAD(TEXT(DAY({!Obtiene_MF.ERPvs__Fecha__c})), 2, "0") = "08"), true,
IF(AND(INCLUDES({!Obtiene_CV.ERPvs__A_cuenta_y_orden_de__r.Dias_de_Exclusion_de_Facturacion_SE__c}, "09"), LPAD(TEXT(DAY({!Obtiene_MF.ERPvs__Fecha__c})), 2, "0") = "09"), true,
IF(AND(INCLUDES({!Obtiene_CV.ERPvs__A_cuenta_y_orden_de__r.Dias_de_Exclusion_de_Facturacion_SE__c}, "10"), LPAD(TEXT(DAY({!Obtiene_MF.ERPvs__Fecha__c})), 2, "0") = "10"), true,
IF(AND(INCLUDES({!Obtiene_CV.ERPvs__A_cuenta_y_orden_de__r.Dias_de_Exclusion_de_Facturacion_SE__c}, "11"), LPAD(TEXT(DAY({!Obtiene_MF.ERPvs__Fecha__c})), 2, "0") = "11"), true,
IF(AND(INCLUDES({!Obtiene_CV.ERPvs__A_cuenta_y_orden_de__r.Dias_de_Exclusion_de_Facturacion_SE__c}, "12"), LPAD(TEXT(DAY({!Obtiene_MF.ERPvs__Fecha__c})), 2, "0") = "12"), true,
IF(AND(INCLUDES({!Obtiene_CV.ERPvs__A_cuenta_y_orden_de__r.Dias_de_Exclusion_de_Facturacion_SE__c}, "13"), LPAD(TEXT(DAY({!Obtiene_MF.ERPvs__Fecha__c})), 2, "0") = "13"), true,
IF(AND(INCLUDES({!Obtiene_CV.ERPvs__A_cuenta_y_orden_de__r.Dias_de_Exclusion_de_Facturacion_SE__c}, "14"), LPAD(TEXT(DAY({!Obtiene_MF.ERPvs__Fecha__c})), 2, "0") = "14"), true,
IF(AND(INCLUDES({!Obtiene_CV.ERPvs__A_cuenta_y_orden_de__r.Dias_de_Exclusion_de_Facturacion_SE__c}, "15"), LPAD(TEXT(DAY({!Obtiene_MF.ERPvs__Fecha__c})), 2, "0") = "15"), true,
IF(AND(INCLUDES({!Obtiene_CV.ERPvs__A_cuenta_y_orden_de__r.Dias_de_Exclusion_de_Facturacion_SE__c}, "16"), LPAD(TEXT(DAY({!Obtiene_MF.ERPvs__Fecha__c})), 2, "0") = "16"), true,
IF(AND(INCLUDES({!Obtiene_CV.ERPvs__A_cuenta_y_orden_de__r.Dias_de_Exclusion_de_Facturacion_SE__c}, "17"), LPAD(TEXT(DAY({!Obtiene_MF.ERPvs__Fecha__c})), 2, "0") = "17"), true,
IF(AND(INCLUDES({!Obtiene_CV.ERPvs__A_cuenta_y_orden_de__r.Dias_de_Exclusion_de_Facturacion_SE__c}, "18"), LPAD(TEXT(DAY({!Obtiene_MF.ERPvs__Fecha__c})), 2, "0") = "18"), true,
IF(AND(INCLUDES({!Obtiene_CV.ERPvs__A_cuenta_y_orden_de__r.Dias_de_Exclusion_de_Facturacion_SE__c}, "19"), LPAD(TEXT(DAY({!Obtiene_MF.ERPvs__Fecha__c})), 2, "0") = "19"), true,
IF(AND(INCLUDES({!Obtiene_CV.ERPvs__A_cuenta_y_orden_de__r.Dias_de_Exclusion_de_Facturacion_SE__c}, "20"), LPAD(TEXT(DAY({!Obtiene_MF.ERPvs__Fecha__c})), 2, "0") = "20"), true,
IF(AND(INCLUDES({!Obtiene_CV.ERPvs__A_cuenta_y_orden_de__r.Dias_de_Exclusion_de_Facturacion_SE__c}, "21"), LPAD(TEXT(DAY({!Obtiene_MF.ERPvs__Fecha__c})), 2, "0") = "21"), true,
IF(AND(INCLUDES({!Obtiene_CV.ERPvs__A_cuenta_y_orden_de__r.Dias_de_Exclusion_de_Facturacion_SE__c}, "22"), LPAD(TEXT(DAY({!Obtiene_MF.ERPvs__Fecha__c})), 2, "0") = "22"), true,
IF(AND(INCLUDES({!Obtiene_CV.ERPvs__A_cuenta_y_orden_de__r.Dias_de_Exclusion_de_Facturacion_SE__c}, "23"), LPAD(TEXT(DAY({!Obtiene_MF.ERPvs__Fecha__c})), 2, "0") = "23"), true,
IF(AND(INCLUDES({!Obtiene_CV.ERPvs__A_cuenta_y_orden_de__r.Dias_de_Exclusion_de_Facturacion_SE__c}, "24"), LPAD(TEXT(DAY({!Obtiene_MF.ERPvs__Fecha__c})), 2, "0") = "24"), true,
IF(AND(INCLUDES({!Obtiene_CV.ERPvs__A_cuenta_y_orden_de__r.Dias_de_Exclusion_de_Facturacion_SE__c}, "25"), LPAD(TEXT(DAY({!Obtiene_MF.ERPvs__Fecha__c})), 2, "0") = "25"), true,
IF(AND(INCLUDES({!Obtiene_CV.ERPvs__A_cuenta_y_orden_de__r.Dias_de_Exclusion_de_Facturacion_SE__c}, "26"), LPAD(TEXT(DAY({!Obtiene_MF.ERPvs__Fecha__c})), 2, "0") = "26"), true,
IF(AND(INCLUDES({!Obtiene_CV.ERPvs__A_cuenta_y_orden_de__r.Dias_de_Exclusion_de_Facturacion_SE__c}, "27"), LPAD(TEXT(DAY({!Obtiene_MF.ERPvs__Fecha__c})), 2, "0") = "27"), true,
IF(AND(INCLUDES({!Obtiene_CV.ERPvs__A_cuenta_y_orden_de__r.Dias_de_Exclusion_de_Facturacion_SE__c}, "28"), LPAD(TEXT(DAY({!Obtiene_MF.ERPvs__Fecha__c})), 2, "0") = "28"), true,
IF(AND(INCLUDES({!Obtiene_CV.ERPvs__A_cuenta_y_orden_de__r.Dias_de_Exclusion_de_Facturacion_SE__c}, "29"), LPAD(TEXT(DAY({!Obtiene_MF.ERPvs__Fecha__c})), 2, "0") = "29"), true,
IF(AND(INCLUDES({!Obtiene_CV.ERPvs__A_cuenta_y_orden_de__r.Dias_de_Exclusion_de_Facturacion_SE__c}, "30"), LPAD(TEXT(DAY({!Obtiene_MF.ERPvs__Fecha__c})), 2, "0") = "30"), true,
IF(AND(INCLUDES({!Obtiene_CV.ERPvs__A_cuenta_y_orden_de__r.Dias_de_Exclusion_de_Facturacion_SE__c}, "31"), LPAD(TEXT(DAY({!Obtiene_MF.ERPvs__Fecha__c})), 2, "0") = "31"), true, false)))))))))))))))))))))))))))))))






