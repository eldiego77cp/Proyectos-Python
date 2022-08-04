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

