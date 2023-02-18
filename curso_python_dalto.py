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

# 1a)
porcentaje_curso_dalto_vs_curso_minimo = (curso_minimo / curso_dalto - 1)*100
print(f'El curso mínimo es {round(porcentaje_curso_dalto_vs_curso_minimo,2)}% más lento que el de dalto')
# 1b)
porcentaje_curso_dalto_vs_curso_maximo = (curso_maximo / curso_dalto - 1)*100
print(f'El curso máximo es {round(porcentaje_curso_dalto_vs_curso_maximo,2)}% más lento que el de dalto')
# 1b)
porcentaje_curso_dalto_vs_curso_promedio = (curso_promedio / curso_dalto - 1)*100
print(f'El curso promedio es {round(porcentaje_curso_dalto_vs_curso_promedio,2)}% más lento que el de dalto')

# 2a)
porcentaje_reduccion_cursos_general = round((1 - (curso_promedio / curso_resto_crudo))*100,2)
print(f'El curso promedio se reduce {round(porcentaje_reduccion_cursos_general,2)}% luego de ser editado')
# 2b)
porcentaje_reduccion_curso_dalto = round((1 - (curso_dalto / curso_dalto_crudo))*100,2)
print(f'El curso de dalto se reduce {round(porcentaje_reduccion_curso_dalto,2)}% luego de ser editado')

# 3a)
horas_de_otro_curso_equivalentes_curso_dalto = 10 * curso_promedio / curso_dalto
print(f'Ver 10 horas del curso de dalto equivale a ver {round(horas_de_otro_curso_equivalentes_curso_dalto,2)} hs de otros cursos')
# 3b)
horas_curso_dalto_equivalentes_horas_de_otro_curso = 10 * curso_dalto / curso_promedio
print(f'Ver 10 horas de otros cursos equivale a ver {round(horas_curso_dalto_equivalentes_horas_de_otro_curso,2)} hs del curso de dalto')

