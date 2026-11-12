# %% [markdown]
# # La ventaja de ser local en el fútbol
# Integrantes: Natalía Guzmán , Juan José Cruz

# %%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("datos/home_advantage_matches.csv")

# %% [markdown]
# ## 1. Carga e inspección inicial de los datos  (Integrante A)
# %%
print("Muestra de los registros:")
display(df.head())
# ## Tomamos los primeros 5 registros para dar un primer vistazo a la base de datos y sus variables.
# %%
print("Dimensiones:")
print(df.shape)
# ## Encontramos las dimensiones para que cumplan con lo requerido.
# %%
print("Información general:")
df.info()
# ## Nos permitio conocer las variables detalladamente y los valores nulos en las mismas.
# %%
print("Estadísticas descriptivas:")
display(df.describe().round(2))

# %% [Markdown]
# ## 2. Manejo de datos faltantes  (Integrante B)
# Nuestra base de datos no tiene ningún dato faltante. En el caso de que existieran se imputarían usando la mediana 
# ya que además de que esta medida no se deja influenciar por outliers, columnas como "home_points", "goals_away" y 
# "fouls_away" tienen variables discretas y por lo tanto la media no es adecuada para reemplazarlos.

# %%
print('Cantidad de valores faltantes:')
df.isna().sum()

# %%
#Si existieran datos faltantes se reemplazarían de esta manera (variables numéricas):
df['travel_distance_km'] = df['travel_distance_km'].fillna(df['travel_distance_km'].median())

# %% [markdown]
# ## 3. Identificación de outliers  (Integrante A)

# %%
plt.figure(figsize=(7, 4))

sns.boxplot(x="attendance_pct", data=df, color="skyblue", width=0.5)

plt.xlabel("Porcentaje de asistencia", fontsize=10)

plt.show()

# %%
plt.figure(figsize=(6, 4))

sns.boxplot(x="fouls_away", data=df, color="skyblue", width=0.5) 

plt.xlabel("Faltas del equipo visitante", fontsize=10)

plt.show()
# %%
plt.figure(figsize=(6, 4))

sns.boxplot(x="goals_away", data=df, color="skyblue", width=0.5) 

plt.xlabel("Goles del Equipo Visitante", fontsize=10)

plt.show()
# %%
plt.figure(figsize=(6, 4))

sns.boxplot(x="goals_home", data=df, color="skyblue", width=0.5) 

plt.xlabel("Goles del Equipo Local", fontsize=10)

plt.show()

# %%
plt.figure(figsize=(6, 4))

sns.boxplot(x="yellow_home", data=df, color="skyblue", width=0.5) 

plt.xlabel("Tarjetas amarillas del Equipo Local", fontsize=10)

plt.show()

# %%
plt.figure(figsize=(6, 4))

sns.boxplot(x="yellow_away", data=df, color="skyblue", width=0.5) 

plt.xlabel("Tarjetas amarillas del Equipo Visitante", fontsize=10)

plt.show()
# %% [markdown]
# ## 4. Valores inconsistentes y duplicados  (Integrante B)
# Usando .duplicated() verificamos que esta base de datos no tiene valores duplicados.
# Adicionalmente revisamos las variables categóricas con .unique() y comprobamos que no hay valores inconsistentes de texto.
# Si existieran, los eliminaríamos o cambiaríamos usando .drop_duplicates(), .replace() o fillna() según el caso.

#%%
duplicados = df[df.duplicated()]
print(f' Cantidad de duplicados: {duplicados.shape[0]}')

#%%
# En el caso de que hubieran duplicados se eleminarían así: 
df = df.drop_duplicates()

#%%
ligas = list(df['league'].unique())
print(f'Lista de valores únicos en la columna "league": {ligas}')

#%%
resultados = list(df['home_result'].unique())
print(f'Lista de valores únicos en la columna "home_result": {resultados}')

#%%
# Si existieran valores inconsistentes en texto se reemplazarían así:
df = df['league'].replace({'LaLiga': 'La_Liga'})

# %% [markdown]
# ## 5. Creación de variables  (Integrante A)

# %% [markdown]
# ## 6. Filtrado y condiciones en pandas  (Integrante B)

# %% [markdown]
# ## 7. Agrupación con groupby  (Integrante A)

# %% [markdown]
# ## 8. Visualizaciones  (Integrante B)

# %% [markdown]
# ## 9. Conclusiones finales  (Integrante A)