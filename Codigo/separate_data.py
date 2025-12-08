import pandas as pd
import re

"""
Leer xlsx
y guardar df
"""
path = "C:\\Users\\javba\\Documents\\Codigo\\Python\\dwh-pipeline-python-project1\\Tareas programadas (Chores) (1).xlsx"
df_data_qs = pd.read_excel(io=path, sheet_name=None)

"""
Definicion de variables
"""
REGEX_sheet_names = "Q(1|2)-(Ene|Feb|Mar|Abr|May|Jun|Jul|Ago|Sep|Oct|Nov|Dic)"
REGEX_tipo_concepto = "gasto|pago"
valid_sheets = {}
#Quitar espacios en blanco de los nombres

for original_name, df in df_data_qs.items():
    clean_name = original_name.replace(" ", "")
    if re.search(REGEX_sheet_names, clean_name):
        df = df.iloc[:, :2]
        df["Quincena"] = clean_name[:2]
        df["Mes"] = clean_name[3:]
        df.columns = ["Concepto", "Monto", "Quincena", "Mes"]
        mask = df["Concepto"].str.contains(REGEX_tipo_concepto, case=False, na=False)
        split_index = mask.idxmax()
        df["Tipo concepto"] = None
        df.loc[df.index < split_index, "Tipo concepto"] = "Ingreso"
        df.loc[df.index > split_index, "Tipo concepto"] = "Gasto"
        df = df.drop(index=split_index).reset_index(drop=True)
        df = df.dropna(how="any").reset_index(drop=True)
        valid_sheets[clean_name] = df

df_export = pd.concat(valid_sheets.values(), ignore_index=True)

df_export.to_csv(path_or_buf="C:\\Users\\javba\\Documents\\Codigo\\Python\\dwh-pipeline-python-project1\\gastos_unificados.csv", index=False)