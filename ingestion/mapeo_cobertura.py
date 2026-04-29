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