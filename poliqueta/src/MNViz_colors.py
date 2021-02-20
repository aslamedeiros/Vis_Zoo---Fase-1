# Color Palette
import numpy as np

## ORDER
# p.s.: o agrupamento é feito por famílias (ordem daquelas famílias deve assumir certa cor)
cores_ordem = {
    'Spionida':'#41A681',   # verde
    'Sabellida':'#7ACAAB',  # verde claro
    'Canalipalpata':'#78a1a1',  # azul
    'Amphinomida':'#8ABFB0',  # azul claro
    'Eunicida':'#A66C4B', # marrom claro
    'Phyllodocida':'#732C02', # marrom2
    'Terebellida':'#ed845e', # laranja claro1
    'Scolecida':'#D94B18', # laranja 2
    np.NAN:'#0D0D0D',  # preto
    
    # ordens não citadas na planilha:
    'Sipuncula':'#D9C2AD', # bege
    'Crassiclitellata':'#FFB27C', # cor de pele clara
    'Aspidosiphonida':'#F29877',  # cor de pele
    
}


## Family
cores_familia = {
    # grupo 1
    'Magelonidae':'#238762',    # verde escuro 
    'Oweniidae':'#3CA67F',      # verde (centroide)  
    'Chaetopteridae':'#77c8a5', # verde
    'Amphinomidae':'#bbebd3',   # verde claro
    # grupo 2
    'Lumbrineridae':'#e7e5df',  # azul claro 1
    'Dorvilleidae':'#b2c0d0',   # azul claro2
    'Oenonidae':'#7A9FBF',      # azul (centroide)
    'Eunicidae':'#3c81ae',      # azul
    'Onuphidae':'#00669a',      # azul escuro
    # grupo 3
    'Syllidae':'#ffbd84', 
    'Typhloscolecidae':'#ffaa74', 
    'Aphroditidae':'#ff9760', 
    'Acoetidae':'#ff814b', 
    'Chrysopetalidae':'#fc6b36', 
    'Eulepethidae':'#eb5824',
    'Lopadorrhynchidae':'#d94814',  # laranja (centroide)
    'Polynoidae':'#c83b03',
    'Nereididae':'#b73000',
    'Nephtyidae':'#f18e56',
    'Glyceridae':'#D96236',         # laranja 2 (centroide)
    'Tomopteridae':'#bf381b',
    # grupo 4
    'Serpulidae':'#fbd0ad',
    'Sabellidae':'#f2b999', # cor de pele (centroide)
    'Sabellariidae':'#e8a287',
    # grupo 5
    'Spionidae':'#d27666',
    'Ampharetidae':'#b48061',
    'Pectinariidae':'#a66c4b',  # marrom 1 (centroide),
    'Trichobranchidae':'#975b39',
    'Terebellidae':'#874c2c',
    'Cirratulidae':'#774124',
    'Flabelligeridae':'#683720',
    # grupo 6
    'Sternaspidae':'#eebd93',
    'Orbiniidae':'#dfa47a',
    'Opheliidae':'#d28d60',
    'Capitellidae':'#c37746',
    'Arenicolidae':'#b4622f',
    'Cossuridae':'#a3501d',
    'Scalibregmatidae':'#92420e',
    'Paraonidae':'#823606',
    'Maldanidae':'#732c02', # marrom 2 (centroide)

    # erros conhecidos
    'NaN':'#0D0D0D',  # preto
}


## CONTINENTE
cores_continente= {
    "#N/D":"#000000",
    "NaN":"#000000",
    "South America":"#40a43b",
    "Central America":"#bbe272",
    "North America":"#255026",
    "Asia":"#db11ac",
    "Africa":"#a96370",
    "Europe":"#208eb7",
    "Antarctica": "#b4ddd4",
    "Oceania":"#dbaea7",
}


## COUNTRY 
### new approach: inspired on Hans Rosling (countries are colored the same as its continents)
cores_pais = {
    # NaN
    "NaN":"#000000",
    # South America
    "Brazil":"#40a43b",
    "Uruguay":"#40a43b",
    "Venezuela":"#40a43b",
    # Central America
    "Panama":"#bbe272",
    "Belize":"#bbe272",
    # North America
    "United States":"#255026",
    # Asia
    "Japan":"#db11ac",
    "Israel":"#db11ac",
    # Africa
    "Sao Tome and Principe":"#a96370",
    # Europe 
    "England":"#208eb7",
    "Norway":"#208eb7",
    "France":"#208eb7",
    "Croatia":"#208eb7",
    "Italy":"#208eb7",
    # Antarctica
    "Antarctica":"#b4ddd4",
    # Oceania
    "Australia":"#dbaea7",
    "Papua New Guinea":"#dbaea7"
}



### South America countries (only)
cores_AS = {
    'Brasil':'#40a43b',
    'Uruguai':'#40a43b',
    'Colômbia':'#40a43b',
    'Peru':'#40a43b',
    'Paraguai':'#40a43b',
    'Argentina':'#40a43b',
    'Guiana Francesa':'#40a43b',
    'Venezuela':'#40a43b',
    'Guiana':'#40a43b',
    'Chile':'#40a43b',
    'Equador':'#40a43b',
}



### BRAZILIAN REGION
cores_regioes = {
    'N':'#22695e',   # forest
    'NE':'#ea1349',  # hot
    'CO':'#69ef7b',   # light green vegetation (Cerrado)
    'SE':'#992a1c',  # emphatic color
    'S':'#7ee7d3'   # cold
}

cores_regioes2 = {
    'N':'#2a6866',   # forest
    'NE':'#cc4c3e',  # hot
    'CO':'#7fa69d',
    'SE':'#bb8377',
    'S':'#48bf8e'   # cold
}


## new approach: inspired in Hans Rosling (each state is colored after its region)
cores_estados = {
    'NaN':'#000000',
    # N
    'Maranhão':'#22695e',
    # NE
    'Alagoas':'#ea1349',
    'Bahia':'#ea1349',
    'Ceará':'#ea1349',
    'Paraíba':'#ea1349',
    'Pernambuco':'#ea1349',
    'Piauí':'#ea1349',
    'Rio Grande do Norte':'#ea1349',
    'Sergipe':'#ea1349',
    # CO
    # SE
    'Espírito Santo':'#992a1c',
    'Minas Gerais':'#992a1c',
    'Rio de Janeiro':'#992a1c',
    'São Paulo':'#992a1c',
    # S
    'Paraná':'#7ee7d3',
    'Santa Catarina':'#7ee7d3',
}