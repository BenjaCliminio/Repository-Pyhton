#a) Diferencia en porcentaje entre el curso actual y: -El mas rapido de otros cursos, -El mas lento de otros cursos, -El promedio de los cursos
curso_actual = 1.5

curso_mas_rapido = 2.5

curso_mas_lento = 7

curso_promedio = 4

Diferencia_con_mas_rapido = 100 - (curso_actual / curso_mas_rapido) *100
Diferencia_con_mas_lento = 100 - (curso_actual / curso_mas_lento) *100
Diferencia_con_promedio = 100 - (curso_actual / curso_promedio) *100

print(f"La diferencia de porcentaje entre el curso actual y el mas rapido es de: {Diferencia_con_mas_rapido}")
print(f"La diferencia de porcentaje entre el curso actual y el mas lento es de: {Diferencia_con_mas_lento}")
print(f"La diferencia de porcentaje entre el curso actual y el mas promedio es de: {Diferencia_con_promedio}")
#b) Porcentaje de marterial inservible que se reduce en: -El promedio de los cursos, El curso actual

#c) Ver 10 horas de este curso a cuantas equivale de otros cursos, y al reves?