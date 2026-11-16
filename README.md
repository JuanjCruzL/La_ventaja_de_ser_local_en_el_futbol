# La ventaja de ser local en el fútbol

## Integrantes
- Nombre Apellido (Integrante A)
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
| ... | Categórica | ... | ... |
| ... | Numérica continua | ... | ... |
| ... | Numérica discreta | ... | ... |

## Organización del repositorio
- `analisis.py`: solución final del proyecto.
- `cuadernos/`: cuadernos de exploración de cada integrante.
- `datos/`: base de datos descargada de Kaggle.

## Conclusiones
1. **La localía es una realidad global y muy constante:**
Los datos demuestran que jugar en casa pesa: los locales ganan el 46.9% de los partidos frente al 29.4% de los visitantes. Al comparar las ligas europeas, vemos que este comportamiento es sumamente estable —con Países Bajos liderando con 47.18% y España con 46.04%—, lo que comprueba que la ventaja local no es un caso aislado, sino una constante del fútbol profesional.

2. **La calidad de los equipos sigue mandando, pero la localía inclina la balanza:** 
Si bien el nivel relativo entre ambos clubes es el predictor individual más fuerte del resultado , el promedio de Elo entre locales (1500.6) y visitantes (1499.6) en el dataset está prácticamente equilibrado. Esto confirma que, en igualdad de condiciones futbolísticas, los factores ambientales y logísticos del estadio son los que terminan inclinando la balanza a favor del anfitrión.

3. **El público es el verdadero motor (El efecto pandemia):** 
El factor ambiental lo cambia todo. En los 9,925 partidos jugados sin público (a puerta cerrada), el rendimiento fue mucho más parejo: los goles locales bajaron a un promedio de 1.44 (vs. 1.20 del visitante) y la tasa de triunfo local cayó del 47.84% al 42.87%. Sin hinchada, gran parte de la ventaja local se desvanece, aunque persiste un remanente explicado por el desplazamiento del rival y la familiaridad con el campo.

4. (Integrante B)
5. (Integrante A)