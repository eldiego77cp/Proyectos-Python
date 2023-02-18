# -*- coding: Windows-1252 -*-
# Ejercicio 1

# Enunciado 
 
# El timming para ver un curso de python es 2.5 hs como mínimo
# El timming para ver un curso de python es 7 hs como máximo
# El timming para ver un curso de python es 4 hs en promedio
# El curso de dalto dura 1.5 hs

# 1)
# a) Que diferencia en % hay entre el curso actual y el más rápido del resto?
# b) Que diferencia en % hay entre el curso actual y el más lento del resto?
# c) Que diferencia en % hay entre el curso actual y el promedio del resto?

# El promedio en crudo para el resto de los cursos es de 5 hs y con edición lo convierten en 4 hs
# El crudo del curso de dalto fue de 3.5 hs y con edición se convirtió en 1.5 hs

# 2)
# a) Que diferencia en % de reducción hay entre el crudo y la conversión para los cursos en general? 
# b) Que diferencia en % de reducción hay entre el crudo y la conversión para el curso de dalto?

# 3) 
# a) Ver 10 hs del curso de dalto a cuantas horas de otro curso equivalen? 
# b) Ver 10 hs de otros cursos a cuantas horas del curso de dalto equivalen?

curso_minimo = 2.5
curso_promedio = 4
curso_maximo = 7
curso_dalto = 1.5
curso_dalto_crudo = 3.5
curso_resto_crudo = 5

# 1 a-b-c
porcentaje_curso_dalto_vs_curso_minimo = (1 - curso_dalto / curso_minimo) * 100
porcentaje_curso_dalto_vs_curso_maximo = (1 - curso_dalto / curso_maximo) * 100
porcentaje_curso_dalto_vs_curso_promedio = (1 - curso_dalto / curso_promedio) * 100

print('----------')
print(f'El curso de dalto es {round(porcentaje_curso_dalto_vs_curso_minimo,2)}% más rápido que el curso de dictado minimo')
print(f'El curso de dalto es {round(porcentaje_curso_dalto_vs_curso_maximo,2)}% más rápido que el curso de dictado máximo')
print(f'El curso de dalto es {round(porcentaje_curso_dalto_vs_curso_promedio,2)}% más rápido que el curso de dictado promedio')
print('----------' + '\n')

# 2 a-b
porcentaje_reduccion_cursos_general = round((1 - (curso_promedio / curso_resto_crudo))*100,2)
porcentaje_reduccion_curso_dalto = round((1 - (curso_dalto / curso_dalto_crudo))*100,2)


print(f'El curso promedio se reduce {round(porcentaje_reduccion_cursos_general,2)}% luego de ser editado')
print(f'El curso de dalto se reduce {round(porcentaje_reduccion_curso_dalto,2)}% luego de ser editado')
print('----------' + '\n')

# 3 a-b
horas_de_otro_curso_equivalentes_curso_dalto = 10 * curso_promedio / curso_dalto
horas_curso_dalto_equivalentes_horas_de_otro_curso = 10 * curso_dalto / curso_promedio

print('----------')
print(f'Ver 10 horas del curso de dalto equivale a ver {round(horas_de_otro_curso_equivalentes_curso_dalto,2)} hs de otros cursos')
print(f'Ver 10 horas de otros cursos equivale a ver {round(horas_curso_dalto_equivalentes_horas_de_otro_curso,2)} hs del curso de dalto')
print('----------' + '\n')

# Ejercicio 2

# Enunciado 
# Suponiendo que cada persona en promedio habla 2 palabras por segundo, pedirle al usuario:
# a) Escriba un texto real, calcular cuanto tardaría en decir esa frase y contar las palabras que dijo
# b) Si se tarda más de un minuto decirle "para flaco, tampoco te pedí un testamento"
# c) Cuanto tardaría dalto si consideramos que es habla un 30% más rápido

frase = input("Ingrese una frase: ")