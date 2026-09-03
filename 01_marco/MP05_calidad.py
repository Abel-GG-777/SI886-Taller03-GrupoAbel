import pandas as pd

def calcular_calidad():
    try:
        # Carga la matriz de articulación que ya tienes creada
        a = pd.read_csv("MP04_articulacion.csv")
        n = len(a)
        
        print("=== REPORTE METODOLÓGICO DE CALIDAD DE PLANES - GRUPO UPT ===")
        print(f"Objetivos del PGD analizados            : {n}")
        print(f"Declaran articulación con el PEI        : {(a.iloc[:,1]=='Sí').sum()} ({(a.iloc[:,1]=='Sí').mean():.0%})")
        print(f"Articulación VERIFICABLE en el texto    : {(a.iloc[:,3]=='Sí').sum()} ({(a.iloc[:,3]=='Sí').mean():.0%})")
        print(f"Con indicador                           : {(a.iloc[:,4]=='Sí').sum()}")
        print(f"Con línea base                          : {(a.iloc[:,5]=='Sí').sum()}")
        print(f"Con meta anual                          : {(a.iloc[:,6]=='Sí').sum()}")
        print(f"Con proyectos asociados                 : {a.iloc[:,7].notna().sum()}")

        # Filtra los objetivos que cumplen con todos los criterios de la guía
        completos = a[(a.iloc[:,3]=='Sí') & (a.iloc[:,4]=='Sí') & (a.iloc[:,5]=='Sí') & (a.iloc[:,6]=='Sí')]
        print(f"\nObjetivos COMPLETOS (articulados, con indicador, línea base y meta): "
              f"{len(completos)} de {n} ({len(completos)/n:.0%})")
        print("\nInterpretación: El porcentaje de objetivos completos es el mejor predictor")
        print("de que el plan pueda evaluarse cuantitativamente al final del periodo.")
        
    except FileNotFoundError:
        print("Error: No se encontró el archivo MP04_articulacion.csv en la ruta actual.")

if __name__ == "__main__":
    calcular_calidad()
