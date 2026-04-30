# =================================================================
# MAPEO DE CATEGORÍAS INEGI → TAXONOMÍA DEL PROYECTO
# Fuente: Serie VI, categorías presentes en la cuenca RH-28
# =================================================================

MAPEO_COBERTURA = {

    # --- AGRICULTURA ---
    "AGRICULTURA DE HUMEDAD ANUAL":                             ("agricultura", "agricultura_humedad",    None,           False, False),
    "AGRICULTURA DE HUMEDAD ANUAL Y PERMANENTE":                ("agricultura", "agricultura_humedad",    None,           False, False),
    "AGRICULTURA DE HUMEDAD ANUAL Y SEMIPERMANENTE":            ("agricultura", "agricultura_humedad",    None,           False, False),
    "AGRICULTURA DE HUMEDAD PERMANENTE":                        ("agricultura", "agricultura_humedad",    None,           False, False),
    "AGRICULTURA DE HUMEDAD SEMIPERMANENTE Y PERMANENTE":       ("agricultura", "agricultura_humedad",    None,           False, False),
    "AGRICULTURA DE RIEGO ANUAL":                               ("agricultura", "agricultura_riego",      None,           False, False),
    "AGRICULTURA DE RIEGO ANUAL Y PERMANENTE":                  ("agricultura", "agricultura_riego",      None,           False, False),
    "AGRICULTURA DE RIEGO ANUAL Y SEMIPERMANENTE":              ("agricultura", "agricultura_riego",      None,           False, False),
    "AGRICULTURA DE RIEGO PERMANENTE":                          ("agricultura", "agricultura_riego",      None,           False, False),
    "AGRICULTURA DE RIEGO SEMIPERMANENTE":                      ("agricultura", "agricultura_riego",      None,           False, False),
    "AGRICULTURA DE RIEGO SEMIPERMANENTE Y PERMANENTE":         ("agricultura", "agricultura_riego",      None,           False, False),
    "AGRICULTURA DE TEMPORAL ANUAL":                            ("agricultura", "agricultura_temporal",   None,           False, False),
    "AGRICULTURA DE TEMPORAL ANUAL Y PERMANENTE":               ("agricultura", "agricultura_temporal",   None,           False, False),
    "AGRICULTURA DE TEMPORAL ANUAL Y SEMIPERMANENTE":           ("agricultura", "agricultura_temporal",   None,           False, False),
    "AGRICULTURA DE TEMPORAL PERMANENTE":                       ("agricultura", "agricultura_temporal",   None,           False, False),
    "AGRICULTURA DE TEMPORAL SEMIPERMANENTE":                   ("agricultura", "agricultura_temporal",   None,           False, False),
    "AGRICULTURA DE TEMPORAL SEMIPERMANENTE Y PERMANENTE":      ("agricultura", "agricultura_temporal",   None,           False, False),

    # --- ASENTAMIENTOS ---
    "ASENTAMIENTOS HUMANOS":                                    ("asentamiento", "asentamiento_humano",   None,           False, False),

    # --- BOSQUE PRIMARIO ---
    "BOSQUE CULTIVADO":                                         ("bosque",      "bosque_cultivado",        "primaria",     True,  False),
    "BOSQUE DE ENCINO":                                         ("bosque",      "bosque_encino",           "primaria",     True,  True),
    "BOSQUE DE ENCINO-PINO":                                    ("bosque",      "bosque_encino_pino",      "primaria",     True,  True),
    "BOSQUE DE MEZQUITE":                                       ("bosque",      "bosque_mezquite",         "primaria",     True,  True),
    "BOSQUE DE OYAMEL":                                         ("bosque",      "bosque_oyamel",           "primaria",     True,  True),
    "BOSQUE DE PINO":                                           ("bosque",      "bosque_pino",             "primaria",     True,  True),
    "BOSQUE DE PINO-ENCINO":                                    ("bosque",      "bosque_pino_encino",      "primaria",     True,  True),
    "BOSQUE DE TÁSCATE":                                        ("bosque",      "bosque_tascate",          "primaria",     True,  True),
    "BOSQUE MESÓFILO DE MONTAÑA":                               ("bosque",      "bosque_mesofile",         "primaria",     True,  True),

    # --- BOSQUE SECUNDARIO ---
    "VEGETACIÓN SECUNDARIA ARBUSTIVA DE BOSQUE DE ENCINO":      ("bosque",      "bosque_encino",           "sec_arbustiva", True, True),
    "VEGETACIÓN SECUNDARIA ARBUSTIVA DE BOSQUE DE ENCINO-PINO": ("bosque",      "bosque_encino_pino",      "sec_arbustiva", True, True),
    "VEGETACIÓN SECUNDARIA ARBUSTIVA DE BOSQUE DE MEZQUITE":    ("bosque",      "bosque_mezquite",         "sec_arbustiva", True, True),
    "VEGETACIÓN SECUNDARIA ARBUSTIVA DE BOSQUE DE PINO":        ("bosque",      "bosque_pino",             "sec_arbustiva", True, True),
    "VEGETACIÓN SECUNDARIA ARBUSTIVA DE BOSQUE DE PINO-ENCINO": ("bosque",      "bosque_pino_encino",      "sec_arbustiva", True, True),
    "VEGETACIÓN SECUNDARIA ARBUSTIVA DE BOSQUE DE TÁSCATE":     ("bosque",      "bosque_tascate",          "sec_arbustiva", True, True),
    "VEGETACIÓN SECUNDARIA ARBUSTIVA DE BOSQUE MESÓFILO DE MONTAÑA": ("bosque", "bosque_mesofile",         "sec_arbustiva", True, True),
    "VEGETACIÓN SECUNDARIA ARBÓREA DE BOSQUE DE ENCINO":        ("bosque",      "bosque_encino",           "sec_arborea",   True, True),
    "VEGETACIÓN SECUNDARIA ARBÓREA DE BOSQUE DE ENCINO-PINO":   ("bosque",      "bosque_encino_pino",      "sec_arborea",   True, True),
    "VEGETACIÓN SECUNDARIA ARBÓREA DE BOSQUE DE MEZQUITE":      ("bosque",      "bosque_mezquite",         "sec_arborea",   True, True),
    "VEGETACIÓN SECUNDARIA ARBÓREA DE BOSQUE DE PINO":          ("bosque",      "bosque_pino",             "sec_arborea",   True, True),
    "VEGETACIÓN SECUNDARIA ARBÓREA DE BOSQUE DE PINO-ENCINO":   ("bosque",      "bosque_pino_encino",      "sec_arborea",   True, True),
    "VEGETACIÓN SECUNDARIA ARBÓREA DE BOSQUE MESÓFILO DE MONTAÑA": ("bosque",   "bosque_mesofile",         "sec_arborea",   True, True),
    "VEGETACIÓN SECUNDARIA HERBÁCEA DE BOSQUE DE ENCINO":       ("bosque",      "bosque_encino",           "sec_herbacea",  True, True),
    "VEGETACIÓN SECUNDARIA HERBÁCEA DE BOSQUE DE PINO":         ("bosque",      "bosque_pino",             "sec_herbacea",  True, True),
    "VEGETACIÓN SECUNDARIA HERBÁCEA DE BOSQUE MESÓFILO DE MONTAÑA": ("bosque",  "bosque_mesofile",         "sec_herbacea",  True, True),

    # --- SELVA PRIMARIA ---
    "SELVA ALTA PERENNIFOLIA":                                  ("selva",       "selva_alta_perennifolia", "primaria",     True,  True),
    "SELVA BAJA CADUCIFOLIA":                                   ("selva",       "selva_baja_caducifolia",  "primaria",     True,  True),

    # --- SELVA SECUNDARIA ---
    "VEGETACIÓN SECUNDARIA ARBUSTIVA DE SELVA ALTA PERENNIFOLIA":   ("selva",   "selva_alta_perennifolia", "sec_arbustiva", True, True),
    "VEGETACIÓN SECUNDARIA ARBUSTIVA DE SELVA BAJA CADUCIFOLIA":    ("selva",   "selva_baja_caducifolia",  "sec_arbustiva", True, True),
    "VEGETACIÓN SECUNDARIA ARBUSTIVA DE SELVA BAJA SUBCADUCIFOLIA": ("selva",   "selva_baja_subcaducifolia","sec_arbustiva", True, True),
    "VEGETACIÓN SECUNDARIA ARBUSTIVA DE SELVA MEDIANA PERENNIFOLIA":("selva",   "selva_mediana_perennifolia","sec_arbustiva",True, True),
    "VEGETACIÓN SECUNDARIA ARBUSTIVA DE SELVA MEDIANA SUBCADUCIFOLIA":("selva", "selva_mediana_subcaducifolia","sec_arbustiva",True,True),
    "VEGETACIÓN SECUNDARIA ARBÓREA DE SELVA ALTA PERENNIFOLIA":     ("selva",   "selva_alta_perennifolia", "sec_arborea",   True, True),
    "VEGETACIÓN SECUNDARIA ARBÓREA DE SELVA ALTA SUBPERENNIFOLIA":  ("selva",   "selva_alta_subperennifolia","sec_arborea", True, True),
    "VEGETACIÓN SECUNDARIA ARBÓREA DE SELVA BAJA CADUCIFOLIA":      ("selva",   "selva_baja_caducifolia",  "sec_arborea",   True, True),
    "VEGETACIÓN SECUNDARIA ARBÓREA DE SELVA MEDIANA SUBCADUCIFOLIA":("selva",   "selva_mediana_subcaducifolia","sec_arborea",True,True),
    "VEGETACIÓN SECUNDARIA HERBÁCEA DE SELVA ALTA PERENNIFOLIA":    ("selva",   "selva_alta_perennifolia", "sec_herbacea",  True, True),
    "VEGETACIÓN SECUNDARIA HERBÁCEA DE SELVA BAJA CADUCIFOLIA":     ("selva",   "selva_baja_caducifolia",  "sec_herbacea",  True, True),
    "VEGETACIÓN SECUNDARIA HERBÁCEA DE SELVA MEDIANA SUBCADUCIFOLIA":("selva",  "selva_mediana_subcaducifolia","sec_herbacea",True,True),

    # --- MANGLAR ---
    "MANGLAR":                                                  ("manglar",     "manglar",                 "primaria",     True,  True),
    "VEGETACIÓN SECUNDARIA ARBUSTIVA DE MANGLAR":               ("manglar",     "manglar",                 "sec_arbustiva", True, True),

    # --- PASTIZAL ---
    "PASTIZAL CULTIVADO":                                       ("pastizal",    "pastizal_cultivado",      None,           False, False),
    "PASTIZAL INDUCIDO":                                        ("pastizal",    "pastizal_inducido",       None,           False, False),
    "PALMAR INDUCIDO":                                          ("pastizal",    "palmar_inducido",         None,           False, False),
    "SABANA":                                                   ("pastizal",    "sabana",                  "primaria",     False, True),
    "SABANOIDE":                                                ("pastizal",    "sabanoide",               "primaria",     False, True),

    # --- OTRO VEGETACIÓN NATIVA ---
    "CHAPARRAL":                                                ("otro",        "chaparral",               "primaria",     False, True),
    "MATORRAL CRASICAULE":                                      ("otro",        "matorral_crasicaule",     "primaria",     False, True),
    "MATORRAL DESÉRTICO ROSETÓFILO":                            ("otro",        "matorral_desertico",      "primaria",     False, True),
    "POPAL":                                                    ("otro",        "popal",                   "primaria",     False, True),
    "PRADERA DE ALTA MONTAÑA":                                  ("otro",        "pradera_alta_montana",    "primaria",     False, True),
    "TULAR":                                                    ("otro",        "tular",                   "primaria",     False, True),
    "VEGETACIÓN DE DUNAS COSTERAS":                             ("otro",        "dunas_costeras",          "primaria",     False, True),
    "VEGETACIÓN SECUNDARIA ARBUSTIVA DE CHAPARRAL":             ("otro",        "chaparral",               "sec_arbustiva", False, True),
    "VEGETACIÓN SECUNDARIA ARBUSTIVA DE MATORRAL DESÉRTICO ROSETÓFILO": ("otro","matorral_desertico",     "sec_arbustiva", False, True),
    "VEGETACIÓN SECUNDARIA ARBUSTIVA DE VEGETACIÓN DE DUNAS COSTERAS":  ("otro","dunas_costeras",         "sec_arbustiva", False, True),

    # --- AGUA Y SIN VEGETACIÓN ---
    "CUERPO DE AGUA":                                           ("agua",        "cuerpo_agua",             None,           False, False),
    "DESPROVISTO DE VEGETACIÓN":                                ("sin_veg",     "desprovisto",             None,           False, False),
    "SIN VEGETACIÓN APARENTE":                                  ("sin_veg",     "sin_vegetacion",          None,           False, False),
}

# Columnas: (clase_cobertura, tipo_cobertura, etapa_sucesional, es_forestal, es_vegetacion_nativa)




def aplicar_mapeo(descripcion):
    """Convierte descripción original INEGI a campos del schema."""
    return MAPEO_COBERTURA.get(descripcion, ("sin_clasificar", "sin_clasificar", None, False, False))


# =================================================================
# MAPEO SERIE II — nomenclatura diferente (~1993)
# Columna: TIPO (en lugar de DESCRIPCIO)
# =================================================================

MAPEO_SERIE_II = {

    # --- AGRICULTURA (sin la palabra "agricultura") ---
    "temporal":                         ("agricultura", "agricultura_temporal",      None,        False, False),
    "riego":                            ("agricultura", "agricultura_riego",         None,        False, False),
    "humedad":                          ("agricultura", "agricultura_humedad",       None,        False, False),
    "riego eventual":                   ("agricultura", "agricultura_riego",         None,        False, False),
    "riego suspendido":                 ("agricultura", "agricultura_riego",         None,        False, False),

    # --- ASENTAMIENTOS ---
    "Zona Urbana":                      ("asentamiento", "asentamiento_humano",      None,        False, False),
    "Pais Extranjero":                  ("sin_veg",      "sin_vegetacion",           None,        False, False),
    "no aplicable":                     ("sin_veg",      "sin_vegetacion",           None,        False, False),

    # --- BOSQUE PRIMARIO ---
    "Bosque bajo abierto":              ("bosque",  "bosque_bajo_abierto",           "primaria",  True,  True),
    "Bosque cultivado":                 ("bosque",  "bosque_cultivado",              "primaria",  True,  False),
    "Bosque de ayarin":                 ("bosque",  "bosque_ayarin",                 "primaria",  True,  True),
    "Bosque de cedro":                  ("bosque",  "bosque_cedro",                  "primaria",  True,  True),
    "Bosque de encino":                 ("bosque",  "bosque_encino",                 "primaria",  True,  True),
    "Bosque de encino-pino":            ("bosque",  "bosque_encino_pino",            "primaria",  True,  True),
    "Bosque de galeria":                ("bosque",  "bosque_galeria",                "primaria",  True,  True),
    "Bosque de oyamel":                 ("bosque",  "bosque_oyamel",                 "primaria",  True,  True),
    "Bosque de pino":                   ("bosque",  "bosque_pino",                   "primaria",  True,  True),
    "Bosque de pino-encino":            ("bosque",  "bosque_pino_encino",            "primaria",  True,  True),
    "Bosque de tascate":                ("bosque",  "bosque_tascate",                "primaria",  True,  True),
    "Bosque mesofilo de montana":       ("bosque",  "bosque_mesofile",               "primaria",  True,  True),
    "Matorral de coniferas":            ("bosque",  "matorral_coniferas",            "primaria",  True,  True),

    # --- SELVA PRIMARIA ---
    "Selva alta perennifolia":          ("selva",   "selva_alta_perennifolia",       "primaria",  True,  True),
    "Selva alta subperennifolia":       ("selva",   "selva_alta_subperennifolia",    "primaria",  True,  True),
    "Selva baja caducifolia":           ("selva",   "selva_baja_caducifolia",        "primaria",  True,  True),
    "Selva baja espinosa":              ("selva",   "selva_baja_espinosa",           "primaria",  True,  True),
    "Selva baja perennifolia":          ("selva",   "selva_baja_perennifolia",       "primaria",  True,  True),
    "Selva baja subcaducifolia":        ("selva",   "selva_baja_subcaducifolia",     "primaria",  True,  True),
    "Selva baja subperennifolia":       ("selva",   "selva_baja_subperennifolia",    "primaria",  True,  True),
    "Selva de galeria":                 ("selva",   "selva_galeria",                 "primaria",  True,  True),
    "Selva mediana caducifolia":        ("selva",   "selva_mediana_caducifolia",     "primaria",  True,  True),
    "Selva mediana perennifolia":       ("selva",   "selva_mediana_perennifolia",    "primaria",  True,  True),
    "Selva mediana subcaducifolia":     ("selva",   "selva_mediana_subcaducifolia",  "primaria",  True,  True),
    "Selva mediana subperennifolia":    ("selva",   "selva_mediana_subperennifolia", "primaria",  True,  True),

    # --- MANGLAR ---
    "Manglar":                          ("manglar",  "manglar",                      "primaria",  True,  True),

    # --- PASTIZAL ---
    "Pastizal cultivado":               ("pastizal", "pastizal_cultivado",           None,        False, False),
    "Pastizal inducido":                ("pastizal", "pastizal_inducido",            None,        False, False),
    "Palmar":                           ("pastizal", "palmar_inducido",              None,        False, False),
    "Pastizal - huizachal":             ("pastizal", "pastizal_natural",             "primaria",  False, True),
    "Pastizal gipsofilo":               ("pastizal", "pastizal_natural",             "primaria",  False, True),
    "Pastizal halofilo":                ("pastizal", "pastizal_natural",             "primaria",  False, True),
    "Pastizal natural":                 ("pastizal", "pastizal_natural",             "primaria",  False, True),
    "Sabana":                           ("pastizal", "sabana",                       "primaria",  False, True),

    # --- OTRO VEGETACIÓN NATIVA ---
    "Chaparral":                        ("otro",     "chaparral",                    "primaria",  False, True),
    "Huizachal":                        ("otro",     "huizachal",                    "primaria",  False, True),
    "Matorral crasicaule":              ("otro",     "matorral_crasicaule",          "primaria",  False, True),
    "Matorral desertico microfilo":     ("otro",     "matorral_desertico",           "primaria",  False, True),
    "Matorral desertico rosetofilo":    ("otro",     "matorral_desertico",           "primaria",  False, True),
    "Matorral espinoso tamaulipeco":    ("otro",     "matorral_espinoso",            "primaria",  False, True),
    "Matorral rosetofilo costero":      ("otro",     "matorral_rosetofilo",          "primaria",  False, True),
    "Matorral sarco-crasicaule":        ("otro",     "matorral_sarcocrasicaule",     "primaria",  False, True),
    "Matorral sarco-crasicaule de neblina": ("otro", "matorral_sarcocrasicaule",     "primaria",  False, True),
    "Matorral sarcocaule":              ("otro",     "matorral_sarcocaule",          "primaria",  False, True),
    "Matorral submontano":              ("otro",     "matorral_submontano",          "primaria",  False, True),
    "Matorral subtropical":             ("otro",     "matorral_subtropical",         "primaria",  False, True),
    "Mezquital":                        ("otro",     "mezquital",                    "primaria",  False, True),
    "Popal":                            ("otro",     "popal",                        "primaria",  False, True),
    "Pradera de alta montana":          ("otro",     "pradera_alta_montana",         "primaria",  False, True),
    "Tular":                            ("otro",     "tular",                        "primaria",  False, True),
    "Vegetacion de desiertos arenosos": ("otro",     "desiertos_arenosos",           "primaria",  False, True),
    "Vegetacion de dunas costeras":     ("otro",     "dunas_costeras",               "primaria",  False, True),
    "Vegetacion de galeria":            ("otro",     "vegetacion_galeria",           "primaria",  False, True),
    "Vegetacion gipsofila":             ("otro",     "vegetacion_gipsofila",         "primaria",  False, True),
    "Vegetacion halofila":              ("otro",     "vegetacion_halofila",          "primaria",  False, True),

# --- CATEGORÍAS ADICIONALES SERIES III-V ---
    "NO APLICABLE":                             ("sin_veg",  "sin_vegetacion",           None,        False, False),
    "BOSQUE INDUCIDO":                          ("bosque",   "bosque_cultivado",          "primaria",  True,  False),
    "PALMAR NATURAL":                           ("pastizal", "palmar_natural",            "primaria",  False, True),
    "SABANOIDE":                                ("pastizal", "sabanoide",                 "primaria",  False, True),
    "SELVA BAJA ESPINOSA CADUCIFOLIA":          ("selva",    "selva_baja_espinosa",       "primaria",  True,  True),
    "SELVA BAJA ESPINOSA SUBPERENNIFOLIA":      ("selva",    "selva_baja_espinosa",       "primaria",  True,  True),
    "VEGETACION DE PETEN":                      ("otro",     "vegetacion_peten",          "primaria",  False, True),
    "BOSQUE DE ENCINO":                         ("bosque",   "bosque_encino",             "primaria",  True,  True),
    "BOSQUE DE ENCINO-PINO":                    ("bosque",   "bosque_encino_pino",        "primaria",  True,  True),
    "BOSQUE DE AYARIN":                         ("bosque",   "bosque_ayarin",             "primaria",  True,  True),
    "BOSQUE DE CEDRO":                          ("bosque",   "bosque_cedro",              "primaria",  True,  True),
    "BOSQUE DE GALERIA":                        ("bosque",   "bosque_galeria",            "primaria",  True,  True),
    "BOSQUE DE OYAMEL":                         ("bosque",   "bosque_oyamel",             "primaria",  True,  True),
    "BOSQUE DE PINO":                           ("bosque",   "bosque_pino",               "primaria",  True,  True),
    "BOSQUE DE PINO-ENCINO":                    ("bosque",   "bosque_pino_encino",        "primaria",  True,  True),
    "BOSQUE DE TASCATE":                        ("bosque",   "bosque_tascate",            "primaria",  True,  True),
    "BOSQUE MESOFILO DE MONTANA":               ("bosque",   "bosque_mesofile",           "primaria",  True,  True),
    "CHAPARRAL":                                ("otro",     "chaparral",                 "primaria",  False, True),
    "MANGLAR":                                  ("manglar",  "manglar",                   "primaria",  True,  True),
    "MATORRAL CRASICAULE":                      ("otro",     "matorral_crasicaule",       "primaria",  False, True),
    "MATORRAL DE CONIFERAS":                    ("bosque",   "matorral_coniferas",        "primaria",  True,  True),
    "MATORRAL DESERTICO MICROFILO":             ("otro",     "matorral_desertico",        "primaria",  False, True),
    "MATORRAL DESERTICO ROSETOFILO":            ("otro",     "matorral_desertico",        "primaria",  False, True),
    "MATORRAL ESPINOSO TAMAULIPECO":            ("otro",     "matorral_espinoso",         "primaria",  False, True),
    "MATORRAL ROSETOFILO COSTERO":              ("otro",     "matorral_rosetofilo",       "primaria",  False, True),
    "MATORRAL SARCO-CRASICAULE":                ("otro",     "matorral_sarcocrasicaule",  "primaria",  False, True),
    "MATORRAL SARCO-CRASICAULE DE NEBLINA":     ("otro",     "matorral_sarcocrasicaule",  "primaria",  False, True),
    "MATORRAL SARCOCAULE":                      ("otro",     "matorral_sarcocaule",       "primaria",  False, True),
    "MATORRAL SUBMONTANO":                      ("otro",     "matorral_submontano",       "primaria",  False, True),
    "MATORRAL SUBTROPICAL":                     ("otro",     "matorral_subtropical",      "primaria",  False, True),
    "MEZQUITAL":                                ("otro",     "mezquital",                 "primaria",  False, True),
    "PALMAR INDUCIDO":                          ("pastizal", "palmar_inducido",           None,        False, False),
    "PASTIZAL GIPSOFILO":                       ("pastizal", "pastizal_natural",          "primaria",  False, True),
    "PASTIZAL HALOFILO":                        ("pastizal", "pastizal_natural",          "primaria",  False, True),
    "PASTIZAL INDUCIDO":                        ("pastizal", "pastizal_inducido",         None,        False, False),
    "PASTIZAL NATURAL":                         ("pastizal", "pastizal_natural",          "primaria",  False, True),
    "POPAL":                                    ("otro",     "popal",                     "primaria",  False, True),
    "PRADERA DE ALTA MONTANA":                  ("otro",     "pradera_alta_montana",      "primaria",  False, True),
    "SABANA":                                   ("pastizal", "sabana",                    "primaria",  False, True),
    "SELVA ALTA PERENNIFOLIA":                  ("selva",    "selva_alta_perennifolia",   "primaria",  True,  True),
    "SELVA ALTA SUBPERENNIFOLIA":               ("selva",    "selva_alta_subperennifolia","primaria",  True,  True),
    "SELVA BAJA CADUCIFOLIA":                   ("selva",    "selva_baja_caducifolia",    "primaria",  True,  True),
    "SELVA BAJA PERENNIFOLIA":                  ("selva",    "selva_baja_perennifolia",   "primaria",  True,  True),
    "SELVA BAJA SUBCADUCIFOLIA":                ("selva",    "selva_baja_subcaducifolia", "primaria",  True,  True),
    "SELVA BAJA SUBPERENNIFOLIA":               ("selva",    "selva_baja_subperennifolia","primaria",  True,  True),
    "SELVA DE GALERIA":                         ("selva",    "selva_galeria",             "primaria",  True,  True),
    "SELVA MEDIANA CADUCIFOLIA":                ("selva",    "selva_mediana_caducifolia", "primaria",  True,  True),
    "SELVA MEDIANA PERENNIFOLIA":               ("selva",    "selva_mediana_perennifolia","primaria",  True,  True),
    "SELVA MEDIANA SUBCADUCIFOLIA":             ("selva",    "selva_mediana_subcaducifolia","primaria", True, True),
    "SELVA MEDIANA SUBPERENNIFOLIA":            ("selva",    "selva_mediana_subperennifolia","primaria",True, True),
    "SIN VEGETACION APARENTE":                  ("sin_veg",  "sin_vegetacion",            None,        False, False),
    "TULAR":                                    ("otro",     "tular",                     "primaria",  False, True),
    "VEGETACION DE DESIERTOS ARENOSOS":         ("otro",     "desiertos_arenosos",        "primaria",  False, True),
    "VEGETACION DE DUNAS COSTERAS":             ("otro",     "dunas_costeras",            "primaria",  False, True),
    "VEGETACION DE GALERIA":                    ("otro",     "vegetacion_galeria",        "primaria",  False, True),
    "VEGETACION GIPSOFILA":                     ("otro",     "vegetacion_gipsofila",      "primaria",  False, True),
    "VEGETACION HALOFILA":                      ("otro",     "vegetacion_halofila",       "primaria",  False, True),
    # Para Series IV (sin acentos)
    "VEGETACION HALOFILA HIDROFILA"
    "BOSQUE DE MEZQUITE"
    
    # Para Serie V (con acentos — usa DESCRIPCIO, no TIP_VEG)
    "BOSQUE MESÓFILO DE MONTAÑA"
    "SIN VEGETACIÓN APARENTE"
    "BOSQUE DE TÁSCATE"
    "MATORRAL DESÉRTICO ROSETÓFILO"
    "BOSQUE DE MEZQUITE"
    "VEGETACIÓN DE DUNAS COSTERAS"
    "PRADERA DE ALTA MONTAÑA"
    
    # Para Serie VII (con acentos — usa DESCRIPCIO)
    "SELVA DE GALERÍA"
    "VEGETACIÓN SECUNDARIA ARBUSTIVA DE MATORRAL CRASICAULE"
    "VEGETACIÓN SECUNDARIA ARBÓREA DE MANGLAR"
    "VEGETACIÓN SECUNDARIA ARBÓREA DE SELVA DE GALERÍA"
    "VEGETACIÓN SECUNDARIA ARBÓREA DE BOSQUE DE CEDRO"
    # --- AGUA Y SIN VEGETACIÓN ---
    "Cuerpo de agua":                   ("agua",     "cuerpo_agua",                  None,        False, False),
    "CUERPO  DE AGUA":              ("agua",        "cuerpo_agua",      None,  False, False),
    "ZONA URBANA":                  ("asentamiento","asentamiento_humano", None, False, False),
    "ASENTAMIENTOS HUMANOS":        ("asentamiento","asentamiento_humano", None, False, False),
    "DESPROVISTO DE VEGETACION":    ("sin_veg",     "desprovisto",      None,  False, False),
    "PAIS EXTRANJERO":              ("sin_veg",     "sin_vegetacion",   None,  False, False),
}


def aplicar_mapeo_serie_ii(tipo):
    """Convierte columna TIPO de Serie II a campos del schema."""
    return MAPEO_SERIE_II.get(tipo, ("sin_clasificar", "sin_clasificar", None, False, False))