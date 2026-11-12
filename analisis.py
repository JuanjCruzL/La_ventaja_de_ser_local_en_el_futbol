# %% [markdown]
# # La ventaja de ser local en el fútbol
# Integrantes: Natalía Guzmán , Juan José Criz

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
# ## 
# %% [markdown]
# ## 2. Manejo de datos faltantes  (Integrante B)

# %%
df.isna().sum()

# %%
# Si existieran datos faltantes se reemplazarían de esta manera (variables numéricas):
df['travel_distance_km'] = df['travel_distance_km'].fillna(df['travel_distance_km'].median())
# %% [markdown]
# ## 3. Identificación de outliers  (Integrante A)
# ## Las variables que tomamos para hacer los boxplot nos permitieron hacer una primera comparación entre el local y el visitante, además de identifcar outliers y los cuartiles en cada una de ellas.
# %%
plt.figure(figsize=(7, 4))

sns.boxplot(x="attendance_pct", data=df, color="skyblue", width=0.5)

plt.xlabel("Porcentaje de asistencia", fontsize=10)

plt.show()
# ## Observamos como la asistencia esta en un 50% de los datos entre el 0.5 y 0.85 de la capacidad de los estadios.
# %%
plt.figure(figsize=(6, 4))

sns.boxplot(x="fouls_away", data=df, color="skyblue", width=0.5) 

plt.xlabel("Faltas del equipo visitante", fontsize=10)

plt.show()
# ## Observamos en el caso de las faltas del equipo visitante se concentran entre 10 y 15, sin embargo existen varios outliers especialmente sobre las 22 faltas.
# %%
plt.figure(figsize=(6, 4))

sns.boxplot(x="goals_away", data=df, color="skyblue", width=0.5) 

plt.xlabel("Goles del Equipo Visitante", fontsize=10)

plt.show()
# ## En el caso de los goles del equipo visitante, observamos que se concentran entre 0 y 2, sin embargo el q3 es bastante amplio, está entre 2 y 5 goles.
# %%
plt.figure(figsize=(6, 4))

sns.boxplot(x="goals_home", data=df, color="skyblue", width=0.5) 

plt.xlabel("Goles del Equipo Local", fontsize=10)

plt.show()
# ## Sin embargo comparandolo con los del equipo local, se evidencia que estan mucho mas compactos y por encima de 3 goles se considera outlier.
# %%
plt.figure(figsize=(6, 4))

sns.boxplot(x="yellow_home", data=df, color="skyblue", width=0.5) 

plt.xlabel("Tarjetas amarillas del Equipo Local", fontsize=10)

plt.show()
# ## Las tarjetas amarillas para el quipo local están entre 0 y 4 y sus cuartiles son totalmente uniformes entre ellos, sin embargo existen bastante outliers que llegan hasta las 9 tarjetas.
# %%
plt.figure(figsize=(6, 4))

sns.boxplot(x="yellow_away", data=df, color="skyblue", width=0.5) 

plt.xlabel("Tarjetas amarillas del Equipo Visitante", fontsize=10)

plt.show()
# ## A diferencia del local, los visitantes suelen recibir bastantes más tarjetas, a pesar de que su mediana sea la misma, el q3 es bastante mas extenso cubriendo desde 3 a 6 tarjetas del equpio visitante, 
# %% [markdown]
# ## 4. Valores inconsistentes y duplicados  (Integrante B)

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