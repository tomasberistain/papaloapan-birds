# Paisaje y Biodiversidad en la Cuenca del Papaloapan

Análisis del cambio de cobertura forestal y su relación con la distribución
de aves en la cuenca del Papaloapan (Veracruz/Oaxaca, México) entre 1993 y 2018.

## Motivación

Nunca vi la selva. Crecí en la región del Papaloapan pero nunca recuerdo
haber visto selva. Este proyecto nace de esa observación directa: ¿existió 
cobertura forestal significativa en esta cuenca? ¿Cuándo se perdió? ¿Qué 
consecuencias tuvo para la biodiversidad local? ¿Aún vuelan las aves?

## Preguntas de investigación

### Bloque A | Cambio de paisaje
- ¿Existió cobertura forestal significativa en la cuenca entre 1993 y 2018?
- ¿Cuánta superficie de selva existía al inicio del período y cuánta queda?
- ¿Dónde estaba concentrada esa cobertura?
- ¿Cuándo ocurrieron los mayores eventos de pérdida?
- ¿Qué reemplazó a la selva?
- ¿Hay zonas que mantuvieron cobertura forestal a lo largo del período?

### Bloque B | Relación paisaje-aves
- ¿Qué especies han reducido su área de distribución efectiva en la cuenca?
- ¿Existe correlación entre pérdida de cobertura y disminución de registros?
- ¿Hay zonas con mayor resiliencia ecológica?
- ¿Qué variables predicen mejor la presencia de especies sensibles?

### Bloque C | Modelado predictivo
- ¿Qué zonas tienen mayor probabilidad de albergar especies en riesgo?
- ¿Qué variables tienen mayor poder predictivo?

## Fuentes de datos

	| Dataset | Fuente | Período |
	|---------|--------|---------|
	| Uso de Suelo y Vegetación (Series II-VII) | INEGI | 1993–2018 |
	| Polígono cuenca RH-28 | INEGI SIATL | — |
	| Registros de aves | eBird / GBIF | 2000–2024 |

## Stack tecnológico

- **Base de datos:** PostgreSQL + PostGIS (Docker)
- **Análisis:** Python: geopandas, pandas, scikit-learn, statsmodels
- **Notebooks:** Jupyter
- **Dashboard:** PowerBI

## Estructura del proyecto

	papaloapan-birds/
	├── data/
	│   ├── raw/          # Datos crudos (no versionados)
	│   └── processed/    # Datos procesados (no versionados)
	├── db/
	│   ├── schema.sql
	│   └── migrations/
	├── ingestion/        # Scripts de ingesta
	├── analysis/
	│   └── notebooks/
	├── outputs/
	│   └── figures/
	├── CHANGELOG.md
	└── README.md




## Estado del proyecto

	🚧🚧🚧🚧🚧🚧🚧🚧🚧🚧🚧🚧🚧🚧🚧🚧🚧🚧🚧🚧🚧🚧
													🚧
	 En construcción — Fase 1: Setup técnico        🚧
													🚧
	🚧🚧🚧🚧🚧🚧🚧🚧🚧🚧🚧🚧🚧🚧🚧🚧🚧🚧🚧🚧🚧🚧
	
	
	## Decisiones técnicas

### Sistema de coordenadas
Todos los datos se reproyectan a **EPSG:4326** (WGS84) como CRS estándar
del proyecto. Los datos originales de INEGI SIATL vienen en EPSG:4019
(GRS80), casi idéntico numéricamente pero incompatible con la mayoría
del ecosistema de herramientas (PostGIS, eBird, GBIF). La reproyección
garantiza que todas las capas sean compatibles en operaciones espaciales.
Para cálculos de área o distancia que requieran precisión métrica se
usará EPSG:6372 (proyección oficial INEGI México).

### Estructura de la cuenca
La RH-28 se descargó del SIATL de INEGI como 34 subcuencas individuales
(RH28Aa–RH28Ax, RH28Ba–RH28Bj), cada una en su propio shapefile.
En el análisis se cargan todas y se disuelven en un polígono único
para delimitar el área de estudio. Las subcuencas individuales se
conservan para análisis a nivel local.

### Limitación metodológica: escala de mapeo
Las Series de Uso de Suelo y Vegetación de INEGI tienen escala 1:250,000
con unidad mínima de mapeo de ~50 ha para elementos naturales. Esto
significa que pérdidas de cobertura forestal menores a esa superficie
no son detectables. La deforestación real es probablemente mayor
a la que este proyecto puede medir.

El área de estudio corresponde a la Región Hidrológica RH-28, que comprende la cuenca del Río Papaloapan y la cuenca del Río Jamapa y otros afluentes menores.