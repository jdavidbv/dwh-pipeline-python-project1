"""
Docstring for Codigo.reglas

Esto es lo que se ha detectado en el archivo
PESTAÑAS*******************************************************
1. Las pestañas validas son aquellas que tiene la estructura:
    Q[1|2]-[Ene|Feb|Mar|Abr|May|Jun|Jul|Ago|Sep|Oct|Nov|Dic]
2. Hacer trim, podria haber espacios antes o despues del guion medio
3. Si una pestaña no cumple, verificar que si tenga al menos Q[1|2], despues con la pestaña anterior y posterior, se puede validar a que mes corresponde

DATOS**********************************************************
4. Solo se deben evaluar las primeras dos columnas
5. Los datos tienen tanto ingresos como egresos, siempre la primera parte son ingresos
6. Los gastos empiezan si se detecta: (n) Espacios en blanc0o|Plan de gastos|Pagos|Gastos
7. Ignorar Totales|Resta|Concepto  en blanco

Paso 2, armar el diagrama de flujo
Paso 3, Hacer el codigo y pruebas minimas
Paso 4, definir tests
"""
