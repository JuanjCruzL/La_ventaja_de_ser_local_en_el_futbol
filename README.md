# La ventaja de ser local en el fútbol

## Integrantes
- Juan José Cruz Lesmes
- Natalia Sofía Guzmán Cortés

## Fuente de los datos
Enlace al dataset en Kaggle y breve descripción de su contenido.

## Estructura de los datos
Número de registros y de variables, qué representa cada fila, y cuántas variables
categóricas, numéricas continuas y numéricas discretas tiene el conjunto.

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
1. (Integrante A)
2. (Integrante B)
3. (Integrante A)
4. (Integrante B)
5. (Integrante A)