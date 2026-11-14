# %% [markdown]
# # La ventaja de ser local en el fútbol
# Integrantes: Natalia Guzmán , Juan José Cruz

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
print(df.head())

# %% [markdown]
# Tomamos los primeros 5 registros para dar un primer vistazo a la base de datos y sus variables.

# %%
print("Dimensiones:")
print(df.shape)

# %% [markdown]
# Encontramos las dimensiones para que cumplan con lo requerido.

# %%
print("Información general:")
df.info()

# %% [markdown]
# Nos permitió conocer las variables detalladamente y los valores nulos en las mismas.

# %%
print("Estadísticas descriptivas:")
print(df.describe().round(2))

# %% [markdown]
# ## 2. Manejo de datos faltantes  (Integrante B)
# Nuestra base de datos no tiene ningún dato faltante. En el caso de que existieran se imputarían usando la mediana, 
# ya que además de que esta medida no se deja influenciar por outliers, columnas como "home_points", "goals_away" y 
# "fouls_away" tienen variables discretas y por lo tanto la media no es adecuada para reemplazarlos.

# %%
print('Cantidad de valores faltantes:')
df.isna().sum()

# %% [markdown]
# Si existieran datos faltantes se reemplazarían de esta manera (variables numéricas):

# %%
df['travel_distance_km'] = df['travel_distance_km'].fillna(df['travel_distance_km'].median())

# %% [markdown]
# ## 3. Identificación de outliers  (Integrante A)
# Las variables que tomamos para hacer los boxplot nos permitieron hacer una primera comparación entre el local y el visitante, además de identificar outliers y los cuartiles en cada una de ellas.

# %%
plt.figure(figsize=(7, 4))

sns.boxplot(x="attendance_pct", data=df, color="skyblue", width=0.5)

plt.xlabel("Porcentaje de asistencia", fontsize=10)

plt.show()

# %% [markdown]
# Observamos como la asistencia está en un 50% de los datos entre el 0.5 y 0.85 de la capacidad de los estadios.

# %%
plt.figure(figsize=(6, 4))

sns.boxplot(x="fouls_away", data=df, color="skyblue", width=0.5) 

plt.xlabel("Faltas del equipo visitante", fontsize=10)

plt.show()

# %% [markdown]
# Observamos en el caso de las faltas del equipo visitante se concentran entre 10 y 15, sin embargo existen varios outliers especialmente sobre las 22 faltas.

# %%
plt.figure(figsize=(6, 4))

sns.boxplot(x="goals_away", data=df, color="skyblue", width=0.5) 

plt.xlabel("Goles del Equipo Visitante", fontsize=10)

plt.show()

# %% [markdown]
# En el caso de los goles del equipo visitante, observamos que se concentran entre 0 y 2, sin embargo el q3 es bastante amplio, está entre 2 y 5 goles.

# %%
plt.figure(figsize=(6, 4))

sns.boxplot(x="goals_home", data=df, color="skyblue", width=0.5) 

plt.xlabel("Goles del Equipo Local", fontsize=10)

plt.show()

# %% [markdown]
# Sin embargo comparándolo con los del equipo local, se evidencia que están mucho más compactos y por encima de 3 goles se considera outlier.

# %%
plt.figure(figsize=(6, 4))

sns.boxplot(x="yellow_home", data=df, color="skyblue", width=0.5) 

plt.xlabel("Tarjetas amarillas del Equipo Local", fontsize=10)

plt.show()

# %% [markdown]
# Las tarjetas amarillas para el equipo local están entre 0 y 4 y sus cuartiles son totalmente uniformes entre ellos, sin embargo existen bastantes outliers que llegan hasta las 9 tarjetas.

# %%
plt.figure(figsize=(6, 4))

sns.boxplot(x="yellow_away", data=df, color="skyblue", width=0.5) 

plt.xlabel("Tarjetas amarillas del Equipo Visitante", fontsize=10)

plt.show()

# %% [markdown]
# A diferencia del local, los visitantes suelen recibir bastantes más tarjetas, a pesar de que su mediana sea la misma, el q3 es bastante más extenso cubriendo desde 3 a 6 tarjetas del equipo visitante.

# %% [markdown]
# ## 4. Valores inconsistentes y duplicados  (Integrante B)
# Usando ```.duplicated()``` verificamos que esta base de datos no tiene valores duplicados. Adicionalmente revisamos las variables categóricas con   ```.unique()``` y comprobamos que no hay valores inconsistentes de texto. Si existieran, los eliminaríamos o cambiaríamos usando ```.drop_duplicates()```, ```.replace()``` o ```fillna()``` según el caso.

# %%
duplicados = df[df.duplicated()]
print(f' Cantidad de duplicados: {duplicados.shape[0]}')

# %% [markdown]
# En el caso de que hubieran duplicados se eliminarían así:

# %%
df = df.drop_duplicates()

# %%
ligas = list(df['league'].unique())
print(f'Lista de valores únicos en la columna "league": {ligas}')

# %%
resultados = list(df['home_result'].unique())
print(f'Lista de valores únicos en la columna "home_result": {resultados}')

# %% [markdown]
# Si existieran valores inconsistentes en texto se reemplazarían así:

# %%
df['league'] = df['league'].replace({'LaLiga': 'La_Liga'})

# %% [markdown]
# ## 5. Creación de variables  (Integrante A)

# %%
mapa_paises = {
    'Serie_A': 'Italy',
    'Primeira': 'Portugal',
    'Eredivisie': 'Netherlands',
    'EPL': 'England',
    'La_Liga': 'Spain',
    'Championship': 'England',
    'Ligue_1': 'France',
    'Bundesliga': 'Germany'
}
print(df.columns)
print(df.head(10))
print(df['league'].unique())
df['country'] = df['league'].map(mapa_paises)
df["country"].unique()

# %% [markdown]
# Creamos la variable país, que después la usaremos en un mapa de calor.

# %%
df["fouls_diff"] = df["fouls_home"] - df["fouls_away"]

# %% [markdown]
# Esta variable nos permite evidenciar de manera directa la diferencia de faltas cobradas del local respecto al visitante.

# %%
df["total_cards"] = (
    df["yellow_home"] + df["yellow_away"] +
    df["red_home"] + df["red_away"]
)

# %% [markdown]
# Esta variable nos permite medir la intensidad de los partidos, nos puede servir para comparar si en los derbis hay más intensidad.
# %% [markdown]
# ## 6. Filtrado y condiciones en pandas  (Integrante B)
#%%
filtro = df['home_result'].value_counts(normalize=True)
filtro
# %% [markdown]
# En el 46.9% del total de partidos gana el equipo local, en el 29,4% gana el visitante y en el 23,8% restante el resultado es un empate.
#%%
largos = df[df['travel_distance_km'] > 800]
print(len(largos))
print(largos['home_result'].value_counts(normalize=True))
# %% [markdown]
# En los 2885 partidos donde la distancia de viaje es de más de 800 km 60,7% del total de partidos gana el equipo local, en el 20,7% gana el visitante y en el 28,5% restante el resultado es un empate.

#%%
lleno = df[df['attendance_pct'] > 0.8]
print(len(lleno))
print(lleno['home_result'].value_counts(normalize=True))
# %% [markdown]
# En los 16919 partidos donde el porcentaje de asistencia es mayor al 80%, 48.51% del total de partidos gana el equipo local, en el 28.1% gana el visitante y en el 23.3% restante el resultado es un empate.

#%%
alta_asistencia = df[df['crowd_size'] > 50000]
print(len(alta_asistencia))
print(alta_asistencia['home_result'].value_counts(normalize=True))
# %% [markdown]
# De los 3122 partidos donde asisten más de 50000 personas el 49.0% gana el equipo local, el 28.3% gana el visitante y en el 22.6% restante el resultado es un empate.

#%%
goles_visitante = df[df['goals_away'] >= 1]
print(len(goles_visitante))
print(goles_visitante['home_result'].value_counts(normalize=True))
# %% [markdown]
# En los 33878 partidos donde el equipo visitante mete uno o más goles 43.3% los gana el equipo visitante, 31.3% son empates y en el 25.3% restante gana el local.


# %% [markdown]
# ## 7. Agrupación con groupby  (Integrante A)
#%%
derbis = df.groupby("is_derby").agg(
    partidos=("match_id", "count"),
    goles_locales=("goals_home", "mean"),
    goles_visitantes=("goals_away", "mean"),
    puntos_locales=("home_points", "mean"),
    tarjetas_totales=("total_cards","mean"),
    diferencia_faltas=("fouls_diff","mean"),
    
)

derbis.round(2)
#%% [markdown]
# Contrario a la creencia popular, los datos muestran que en los derbis se diluye ligeramente la ventaja de jugar en casa: el equipo local promedia menos goles (1.45 vs 1.60) y menos puntos (1.54 vs 1.65). Por otro lado, el aspecto disciplinario se mantiene prácticamente intactotanto el promedio de tarjetas totales (~3.76) como la diferencia de faltas a favor del local (~2.85 faltas menos cometidas) no sufren variaciones relevantes respecto a un partido regular
#%%
Asistencia = df.groupby("crowd_present").agg(
    goles_locales=("goals_home", "mean"),
    goles_visitantes=("goals_away", "mean"),
    puntos_locales=("home_points", "mean"),
    tarjetas_totales=("total_cards","mean"),
    diferencia_faltas=("fouls_diff","mean"),
    sesgo_arbitro=("referee_bias_susceptibility","mean")
)
Asistencia.round(2)
#%% [markdown]
# La presencia de público incrementa los goles y puntos del equipo local mientras reduce los del visitante. Asimismo, genera un fuerte desbalance en las faltas a favor del local, confirmando la influencia psicológica de la hinchada.
#%%
country = df.groupby("country").agg(
    partidos=("match_id", "count"),
    goles_locales=("goals_home", "mean"),
    goles_visitantes=("goals_away", "mean"),
    puntos_locales=("home_points", "mean"),
    tarjetas_totales=("total_cards","mean"),
    diferencia_faltas=("fouls_diff","mean"),
    
)

country.round(2)
#%% [markdown]
# La ventaja de local es sumamente homogénea en todos los países evaluados, mostrando promedios casi idénticos en goles (~1.6 a favor y ~1.1 visitante), puntos (~1.65) y tarjetas (~3.7). Esto demuestra que el factor local es un fenómeno global y constante, independiente de la liga o país.
#%%
attendance_pct = df.groupby("attendance_pct").agg(
    partidos=("match_id", "count"),
    goles_locales=("goals_home", "mean"),
    goles_visitantes=("goals_away", "mean"),
    puntos_locales=("home_points", "mean"),
    tarjetas_totales=("total_cards","mean"),
    diferencia_faltas=("fouls_diff","mean"),
    
)

attendance_pct.round(2)
#%% [markdown]
# A mayor porcentaje de asistencia, efectivamente mejora el rendimiento del equipo local en goles, puntos y faltas a favor. En los 9,925 partidos con asistencia 0.0 (que corresponden en su mayoría a la pandemia), el juego fue mucho más parejo en goles (1.44 vs 1.20) y prácticamente neutral en las faltas (0.01). En contraste, cuando el estadio roza el 100% de ocupación (0.995 - 0.999), el local dispara su promedio hasta los 2.00 goles y más de 2.1 puntos por partido, mientras el desbalance en faltas supera las -5.00 a su favor.
# %% [markdown]
# ## 8. Visualizaciones  (Integrante B)

# %% [markdown]
# **1. Comparación porcentaje de victorias del equipo local entre países** 
#%%
import plotly.express as px

df['local_gana'] = (df['home_result'] == 'home_win').astype(int)
df_mapa = (df.groupby('country', as_index=False)['local_gana'].mean())
df_mapa['local_gana'] = df_mapa['local_gana'] * 100
df_mapa['country_plot'] = df_mapa['country'].replace({'England': 'United Kingdom'})

fig = px.choropleth(
    df_mapa,
    locations='country_plot',
    locationmode='country names',
    color='local_gana',
    hover_name='country',
    scope='europe',
    color_continuous_scale='plasma',  
    template='plotly_dark',           
    title='Porcentaje de victorias en casa por país',
    labels={'puntos_casa': 'Promedio de puntos'}
)
fig.update_geos(
    resolution=50,               
    showcountries=True,
    countrycolor="#8A8A8A",      
    countrywidth=0.8,
    showland=True,
    landcolor="#E4E4E4D6",         
    showocean=True,
    oceancolor="#000000",        
    bgcolor="#000000FF"            
)


fig.update_layout(
    title={
        'text': '<b>Porcentaje de victorias en casa por país</b>',
        'x': 0.5,
        'xanchor': 'center',
        'font': {'size': 20, 'color': 'white'}
    },
    paper_bgcolor="#000000FF",    
    margin={"r": 10, "t": 60, "l": 10, "b": 10}
)

fig.show()

# %% [markdown]
# A través del gráfico podemos observar que mientras Paises Bajos tiene el mayor porcentaje de victoria de los equipos locales (47.18%), España presenta el menor (46,04%). A pesar de esto la diferencia entre ligas es pequeña (1.14%), lo cual indica que no existe un cambio significativo de la ventaja de la localía entre ligas.
# %% [markdown]
# **2. Porcentaje de victorias en casa según la distacia de viaje**

#%%
df['tramo'] = pd.cut(df['travel_distance_km'], [0, 200, 500, 800, 1500, 10000])
tabla = (df.groupby('tramo', observed=True)['home_result']
           .value_counts(normalize=True).unstack() * 100)
colores = plt.get_cmap('YlGnBu')(np.linspace(0.25, 0.95, tabla.shape[1]))
tabla.plot(kind='bar', stacked=True, color=colores)
plt.ylabel('% victorias locales')
plt.xlabel('Distancia de viaje (km)')
plt.show()
# %% [markdown]
# Se evidencia una disminución progresiva en el porcentaje de victorias de visitante a medida que aumenta la distancia, de ~33% en viajes de hasta 200 km a ~13 % en viajes de más de 1500 km. Así mismo, los empates disminuyen y aumentan las victorias, de ~40% a ~65%. Esto indica que la distancia es uno de los factores que puede aumentar la ventaja del local.
# %% [markdown]
# **3. Proporción de victorias del equipo local en los derbis**

#%%
sns.barplot(data=df, x='is_derby', y='local_gana', palette='Set2')
plt.xticks([0, 1], ['No', 'Sí'])
plt.xlabel('¿Es un derbi?')
plt.ylabel('Proporción de victorias locales')
plt.show()

# %% [markdown]
# En los derbis disminuye ~4% las victorias del local, indicando que en este tipo de partidos se reduce la ventaja de jugar en casa.

# %% [markdown]
# **4. Diferencia entre faltas y amarillas según la asistencia** 

#%%
df['dif_amarillas'] = df['yellow_home'] - df['yellow_away']
df['tramo_crowd'] = pd.qcut(df.loc[df['crowd_size'] > 0, 'crowd_size'], q=5)

df[df['crowd_size'] > 0].groupby('tramo_crowd', observed=True)[['fouls_diff', 'dif_amarillas']].mean().plot(marker='o', cmap = 'coolwarm')
plt.legend(['Diferencia de faltas', 'Diferencia de amarillas'])
plt.xlabel('Cantidad de público')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
# %% [markdown]
# A medida que aumenta la cantidad de público, el equipo local comete en promedio menos faltas que el visitante (de ~-3,2 a ~-4,0 faltas).En cambio, las diferencia de amarillas se mantiene constante. 
# Adicionalmente, en promedio, el equipo visitante acumula más faltas y recibe más tarjetas amarillas que el local.
# %% [markdown]
# **5. Porcentaje de victorias del local según la ocupación del estadio**

#%%
df['tramo_ocup'] = pd.cut(df['attendance_pct'],
                          bins=[0, 0.5, 0.7, 0.9, 1.01],
                          labels=['0-50 %', '50-70 %', '70-90 %', '90-100 %'])
(df.groupby('tramo_ocup', observed=True)['local_gana'].mean() * 100).plot(kind='bar', color = 'teal')
plt.xticks(rotation=0, ha='center')
plt.tight_layout()
plt.xlabel('Porcentaje de ocupación')
plt.ylabel('% de victorias locales')
# %% [markdown]
#Conforme crece el porcentaje de ocupación, las victorias del local tienden a aumentar, pasan de ~43% con un estadio entre el 0 y 50% a ~50% con una ocupación de 90%-100%. Esto sugiere una relación entre estadios más llenos y mayor ventaja local, aunque pueden influir otros factores como la fortaleza del rival.

# %% [markdown]
# **6. Proporción de victorias en casa a partir de la presencia de público**

#%%
sns.barplot(data=df, x='crowd_present', y='local_gana', palette= 'Set3')
plt.xticks([0, 1], ['Sin público', 'Con público'])
plt.xlabel('Presencia de público')
plt.ylabel('Proporción de victorias locales')

# %% [markdown]
#En los partidos jugados sin público las victorias en casa disminuyeron aproximadamente un 5%. Esto confirma que el público es otro factor que puede aumentar la ventaja del local.

# %% [markdown]
# ## 9. Conclusiones finales  (Integrante A)