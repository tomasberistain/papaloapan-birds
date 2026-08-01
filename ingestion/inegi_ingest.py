"""
inegi_ingest.py
Procesamiento de las Series de Uso de Suelo y Vegetación (INEGI)
para la cuenca RH-28 (Papaloapan + Jamapa).

Salida: data/processed/cobertura_rh28.gpkg
        (GeoPackage con todas las series, recortadas y clasificadas)
"""

from pathlib import Path
import geopandas as gpd
import pandas as pd
from mapeo_cobertura import aplicar_mapeo



# =================================================================
# CONFIGURACIÓN
# =================================================================


BASE_PROYECTO = Path(__file__).resolve().parents[1]
BASE_DATOS    = BASE_PROYECTO / "data/raw/inegi_usv"
BASE_SIATL    = BASE_PROYECTO / "data/raw/siatl"
SALIDA        = BASE_PROYECTO / "data/processed/cobertura_rh28.gpkg"


CRS_DESTINO  = "EPSG:4326"

# Umbral máximo tolerado de polígonos sin clasificar (proporción del total)
UMBRAL_SIN_CLASIFICAR = 0.005  # 0.5%


SERIES = {
    "I":  {
        "anio_imagen":      1985,
        "anio_publicacion": 1991,
        "col_descripcion":  "TIPO",
        "combinar_otros":   True,
    },
    "II":  {
        "anio_imagen":      1993,
        "anio_publicacion": 2001,
        "col_descripcion":  "TIPO",
        "combinar_otros":   True,
    },
    "III": {
        "anio_imagen":      2002,
        "anio_publicacion": 2005,
        "col_descripcion":  "TIP_VEG",
        "combinar_otros":   True,
    },
    "IV":  {
        "anio_imagen":      2007,
        "anio_publicacion": 2009,
        "col_descripcion":  "TIP_VEG",
        "combinar_otros":   True,
    },
    "V":   {
        "anio_imagen":      2011,
        "anio_publicacion": 2013,
        "col_descripcion":  "TIP_VEG",
        "combinar_otros":   True,
    },
    "VI":  {
        "anio_imagen":      2014,
        "anio_publicacion": 2016,
        "col_descripcion":  "TIP_VEG",
        "combinar_otros":   True,
    },
    "VII": {
        "anio_imagen":      2018,
        "anio_publicacion": 2021,
        "col_descripcion":  "DESCRIPCIO",
        "combinar_otros":   True,
        "patron_glob":      "*cnal.shp",
    },
}

# =================================================================
# CARGAR POLÍGONO DE LA CUENCA
# =================================================================

def cargar_cuenca():
    print("Cargando polígono de la cuenca RH-28...")
    partes = []
    for shp in BASE_SIATL.rglob("*_subc.shp"):
        partes.append(gpd.read_file(shp))
    cuenca = pd.concat(partes, ignore_index=True)
    cuenca = cuenca.to_crs(CRS_DESTINO)
    cuenca = cuenca.dissolve()
    print(f"  Cuenca cargada. CRS: {cuenca.crs}")
    return cuenca

# =================================================================
# PROCESAR UNA SERIE
# =================================================================

def procesar_serie(nombre_serie, config, cuenca):
    print(f"\nProcesando Serie {nombre_serie}...")
    patron = config.get("patron_glob", "*v.shp")
    archivos = list((BASE_DATOS / f"SERIE {nombre_serie}").glob(patron))
    col_desc  = config["col_descripcion"]


    # 1. Leer y concatenar archivos
    partes = []
    for archivo in archivos:
        try:
            gdf = gpd.read_file(archivo)
            # Eliminar columnas duplicadas
            gdf = gdf.loc[:, ~gdf.columns.duplicated()]
            partes.append(gdf)
        except Exception as e:
            print(f"  Error leyendo {archivo.name}: {e}")

    if not partes:
        print(f"  Sin archivos para Serie {nombre_serie}, saltando.")
        return None

    gdf = pd.concat(partes, ignore_index=True)
    print(f"  {len(gdf):,} polígonos leídos")

    # 2. Verificar columna de descripción
    if col_desc not in gdf.columns:
        print(f"  Columnas disponibles: {gdf.columns.tolist()}")
        raise ValueError(f"Columna '{col_desc}' no encontrada en Serie {nombre_serie}")

    # 2b. Asignar CRS si no está definido (Serie II viene sin CRS explícito)
    if gdf.crs is None:
        gdf = gdf.set_crs("EPSG:6362")

    # 3. Reproyectar
    gdf = gdf.to_crs(CRS_DESTINO)

    # 4. Clip a la cuenca
    gdf = gpd.clip(gdf, cuenca)
    print(f"  {len(gdf):,} polígonos tras clip")

    # 4b. Combinar columna principal con OTROS cuando la principal es "NO APLICABLE"
    if config.get("combinar_otros") and "OTROS" in gdf.columns:
        def columna_efectiva(row):
            if row[col_desc] == "NO APLICABLE" and row["OTROS"] != "NO APLICABLE":
                return row["OTROS"]
            return row[col_desc]

        gdf["_desc_efectiva"] = gdf.apply(columna_efectiva, axis=1)
        col_desc_mapeo = "_desc_efectiva"
    else:
        col_desc_mapeo = col_desc

    # 5. Aplicar mapeo de cobertura (con fallback interno entre nomenclaturas)
    mapeo = gdf[col_desc_mapeo].apply(aplicar_mapeo)
    gdf["clase_cobertura"]       = mapeo.apply(lambda x: x[0])
    gdf["tipo_cobertura"]        = mapeo.apply(lambda x: x[1])
    gdf["etapa_sucesional"]      = mapeo.apply(lambda x: x[2])
    gdf["es_forestal"]           = mapeo.apply(lambda x: x[3])
    gdf["es_vegetacion_nativa"]  = mapeo.apply(lambda x: x[4])

    # 6. Verificar categorías sin clasificar
    sin_cls = gdf[gdf["clase_cobertura"] == "sin_clasificar"][col_desc_mapeo].unique()
    if len(sin_cls) > 0:
        print(f"  ⚠ Categorías sin clasificar: {sin_cls}")

    # 7. Agregar metadatos de serie
    gdf["serie_inegi"]        = nombre_serie
    gdf["anio_imagen"]        = config["anio_imagen"]
    gdf["anio_publicacion"]   = config["anio_publicacion"]
    gdf["descripcion"] = gdf[col_desc_mapeo]

    # 8. Seleccionar columnas finales
    columnas = [
        "serie_inegi", "anio_imagen", "anio_publicacion",
        "descripcion", "clase_cobertura", "tipo_cobertura",
        "etapa_sucesional", "es_forestal", "es_vegetacion_nativa",
        "geometry"
    ]
    return gdf[columnas]

# =================================================================
# MAIN
# =================================================================

def main():
    cuenca = cargar_cuenca()

    resultados = []
    for nombre_serie, config in SERIES.items():
        resultado = procesar_serie(nombre_serie, config, cuenca)
        if resultado is not None:
            resultados.append(resultado)

    print("\nConcatenando todas las series...")
    cobertura = pd.concat(resultados, ignore_index=True)
    cobertura = gpd.GeoDataFrame(cobertura, geometry="geometry", crs=CRS_DESTINO)
    print(f"Total polígonos: {len(cobertura):,}")

    # Chequeo global de polígonos sin clasificar
    n_sin_cls = (cobertura["clase_cobertura"] == "sin_clasificar").sum()
    if n_sin_cls > 0:
        proporcion = n_sin_cls / len(cobertura)
        print(f"\n⚠️  ATENCIÓN: {n_sin_cls:,} polígonos sin clasificar "
              f"({proporcion:.2%} del total)")
        if proporcion > UMBRAL_SIN_CLASIFICAR:
            categorias = sorted(
                cobertura.loc[cobertura["clase_cobertura"] == "sin_clasificar", "descripcion"]
                .unique()
                .tolist()
            )
            raise ValueError(
                f"Demasiados polígonos sin clasificar ({proporcion:.2%} > "
                f"{UMBRAL_SIN_CLASIFICAR:.2%}). Revisa MAPEO_COBERTURA / "
                f"MAPEO_SERIE_II para estas categorías: {categorias}"
            )

    # Guardar como GeoPackage
    SALIDA.parent.mkdir(parents=True, exist_ok=True)
    cobertura.to_file(SALIDA, driver="GPKG")
    print(f"\nGuardado en: {SALIDA}")

    # Resumen por serie y clase
    print("\nResumen por serie y clase de cobertura:")
    print(cobertura.groupby(["anio_imagen", "clase_cobertura"]).size().unstack(fill_value=0))

if __name__ == "__main__":
    main()