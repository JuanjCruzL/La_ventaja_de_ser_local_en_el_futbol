# La ventaja de ser local en el fútbol

## Integrantes
- Juan José Cruz Lesmes
- Natalia Sofía Guzmán Cortés

## Fuente de los datos
[Enlace al dataset en kaggle](https://www.kaggle.com/datasets/sergionefedov/home-advantage-in-football-bias-or-real)

Este dataset sintético Home Advantage in Football — Bias or Real? contiene 50000 partidos construidos con el objetivo de verificar si la ventaja de jugar de local en los partidos de fútbol es real. Separa sus posibles causas en variables distintas: el público (asistencia y ocupación del estadio, y si asistió público o no), la distancia de viaje del visitante, la familiaridad del local con la cancha y la fortaleza de los equipos medida con Elo. 
## Estructura de los datos
El conjunto contiene 50000 registros y 25 variables. Cada fila representa un partido de fútbol, con sus características previas (liga, Elo, distancia de viaje, asistencia) y sus resultados (goles, faltas, tarjetas, resultado y puntos).

| Tipo | Cantidad | Variables |
|---|---|---|
| **Categóricas** | 5 | `match_id`, `league`, `home_result`, `crowd_present`, `is_derby` |
| **Numéricas continuas** | 7 | `elo_home`, `elo_away`, `elo_diff`, `attendance_pct`, `travel_distance_km`, `venue_familiarity`, `referee_bias_susceptibility` |

## Diccionario de datos
| Variable | Tipo | Descripción | Valores / unidades |
|---|---|---|---|
| `match_id` | Categórica | Identificador único de cada partido registrado. | Texto alfanumérico único (`MCH000000` – `MCH049999`) |
| `league` | Categórica | Liga o competición de fútbol en la que se disputó el encuentro. | `EPL`, `Serie_A`, `La_Liga`, `Bundesliga`, `Ligue_1`, `Primeira`, `Eredivisie`, `Championship` |
| `elo_home` | Numérica discreta | Calificación Elo (nivel de fuerza) del equipo local antes del partido. | Rango: `1200` a `1900` puntos Elo |
| `elo_away` | Numérica discreta | Calificación Elo (nivel de fuerza) del equipo visitante antes del partido. | Rango: `1200` a `1900` puntos Elo |
| `elo_diff` | Numérica discreta | Diferencia de calificación Elo entre el equipo local y el visitante (`elo_home - elo_away`). | Rango: `-667` a `675` puntos Elo |
| `crowd_present` | Categórica | Indicador binario de si hubo asistencia de público en el estadio o se jugó a puerta cerrada. | `0` (sin público), `1` (con público) |
| `stadium_capacity` | Numérica discreta | Capacidad máxima de espectadores del estadio anfitrión. | Rango: `8,000` a `90,000` espectadores |
| `attendance_pct` | Numérica continua | Proporción de ocupación del estadio respecto a su capacidad total. | Rango: `0.000` a `0.999` (proporción de 0 a 1) |
| `crowd_size` | Numérica discreta | Número total de espectadores que asistieron al partido. | Rango: `0` a `86,300` espectadores |
| `travel_distance_km` | Numérica continua | Distancia recorrida por el equipo visitante hasta la sede del encuentro. | Rango: `0.0` a `2,390.0` kilómetros (`km`) |
| `timezones_crossed` | Numérica discreta | Cantidad de husos horarios atravesados por el equipo visitante en su desplazamiento. | Valores enteros: `0`, `1`, `2` husos horarios |
| `is_derby` | Categórica | Indicador binario de si el encuentro corresponde a un derbi o clásico regional. | `0` (no es derbi), `1` (es derbi) |
| `venue_familiarity` | Numérica continua | Índice o puntuación del grado de familiaridad del equipo con el estadio/terreno de juego. | Rango: `0.00` a `10.00` puntos |
| `referee_bias_susceptibility` | Numérica continua | Índice de susceptibilidad del árbitro a verse influenciado por la presión ambiental o localía. | Rango: `0.00` a `10.00` puntos |
| `fouls_home` | Numérica discreta | Número total de faltas cometidas por el equipo local. | Rango: `1` a `23` faltas |
| `fouls_away` | Numérica discreta | Número total de faltas cometidas por el equipo visitante. | Rango: `1` a `28` faltas |
| `yellow_home` | Numérica discreta | Cantidad de tarjetas amarillas recibidas por el equipo local. | Rango: `0` a `9` tarjetas |
| `yellow_away` | Numérica discreta | Cantidad de tarjetas amarillas recibidas por el equipo visitante. | Rango: `0` a `10` tarjetas |
| `red_home` | Numérica discreta | Cantidad de tarjetas rojas recibidas por el equipo local. | Valores: `0`, `1` tarjeta |
| `red_away` | Numérica discreta | Cantidad de tarjetas rojas recibidas por el equipo visitante. | Valores: `0`, `1` tarjeta |
| `goals_home` | Numérica discreta | Goles anotados por el equipo local al finalizar el partido. | Rango: `0` a `11` goles |
| `goals_away` | Numérica discreta | Goles anotados por el equipo visitante al finalizar el partido. | Rango: `0` a `8` goles |
| `home_goal_diff` | Numérica discreta | Diferencia de goles desde la perspectiva del equipo local (`goals_home - goals_away`). | Rango: `-8` a `11` goles |
| `home_result` | Categórica | Resultado final del partido para el equipo local. | `home_win` (victoria local), `draw` (empate), `away_win` (derrota local) |
| `home_points` | Numérica discreta | Puntos obtenidos por el equipo local según el resultado del partido. | `0` (derrota), `1` (empate), `3` (victoria) puntos |

## Organización del repositorio
- `analisis.py`: script principal con el procesamiento de datos, análisis estadístico y resultados finales del proyecto.
- `cuadernos/`: Jupyter Notebooks (`.ipynb`) con el análisis exploratorio y pruebas realizadas por cada integrante.
- `datos/`: carpeta que contiene el dataset original (`home_advantage_matches.csv`) obtenido de Kaggle.

## Conclusiones
1. **La localía es una realidad global y muy constante:**
Los datos demuestran que jugar en casa pesa: los locales ganan el 46.9% de los partidos frente al 29.4% de los visitantes. Al comparar las ligas europeas, vemos que este comportamiento es sumamente estable —con Países Bajos liderando con 47.18% y España con 46.04%—, lo que comprueba que la ventaja local no es un caso aislado, sino una constante del fútbol profesional.

2. **La calidad de los equipos sigue mandando, pero la localía inclina la balanza:** 
Si bien el nivel relativo entre ambos clubes es el predictor individual más fuerte del resultado , el promedio de Elo entre locales (1500.6) y visitantes (1499.6) en el dataset está prácticamente equilibrado. Esto confirma que, en igualdad de condiciones futbolísticas, los factores ambientales y logísticos del estadio son los que terminan inclinando la balanza a favor del anfitrión.

3. **El público es el verdadero motor (El efecto pandemia):** 
El factor ambiental lo cambia todo. En los 9,925 partidos jugados sin público (a puerta cerrada), el rendimiento fue mucho más parejo: los goles locales bajaron a un promedio de 1.44 (vs. 1.20 del visitante) y la tasa de triunfo local cayó del 47.84% al 42.87%. Sin hinchada, gran parte de la ventaja local se desvanece, aunque persiste un remanente explicado por el desplazamiento del rival y la familiaridad con el campo.

4. **La presión ambiental actúa a través del arbitraje:** 
#Los datos revelan uno de los mecanismos clave detrás del efecto del público: sin espectadores, las sanciones disciplinarias son prácticamente idénticas para ambos equipos (11.03 faltas del local vs. 11.02 del visitante). En cambio, cuando hay público en las gradas, a los visitantes se les pitan en promedio +3.55 faltas más (12.92 vs. 9.36), reciben +0.72 tarjetas amarillas más y más del doble de expulsiones (0.094 vs. 0.038), una brecha que se amplía cuanto mayor es la susceptibilidad del árbitro.

5. **A mayor afición, mayor rendimiento:** 
#El impacto de la grada también es gradual según la ocupación de los estadios: incluso filtrando únicamente los partidos con público, las victorias locales suben progresivamente desde un 43.25% cuando el estadio está medio vacío (0–50% de aforo) hasta tocar el 49.57% cuando la asistencia está a reventar (90–100%). El aliento de la gente impulsa directamente al equipo de casa.

6. **El desgaste de viajar pesa:** 
#La geografía también juega su partido. El éxito del equipo visitante cae en picada conforme aumenta la distancia a recorrer: pasan de ganar un 32.88% en trayectos cortos (menos de 200 km) a un 16.75% en viajes superiores a 1,000 km (y apenas un 12.61% por encima de 1,500 km). Además, cruzar una zona horaria eleva las victorias locales del 45.81% al 59.31%, reflejando el fuerte impacto del cansancio físico y logístico.

7. **Los derbis rompen la regla:** 
#Curiosamente, en los partidos de máxima rivalidad (derbis) la ventaja del local se reduce en 4.1 puntos porcentuales (bajando del 47.11% al 43.00% de victorias locales). Más allá de la tensión emocional propia de un clásico, los datos muestran que en estos encuentros desaparece el desgaste por desplazamiento (distancia promedio de 10.9 km frente a 359.6 km en partidos normales), neutralizando uno de los principales castigos que sufre el equipo visitante.

35299    245
48553    118
8719    -237
44063    -64
21557     52
42308    -16
14482   -125
16398    285
48094   -233
43306     87
Name: elo_diff, dtype: int64