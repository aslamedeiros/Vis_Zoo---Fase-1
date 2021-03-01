# Paletas de cores
## ORDEM
#cores_ordem = {   # p.s.: Caudata is an error and should be removed
#    'Squamata': '#BF4417',
#    'Testudines': '#D9CB0B', 
#    'Crocodylia': '#284021'   
#}

cores_infraordem = {
    'Nan':'#000000',
    'Ascacidae':'#fece5f',
    'Anomura':'#007961',
    'Achelata':'#7a2c39',
    'Axiidea':'#b67262',
    'Brachyura':'#ee4454',
    'Caridea':'#3330b7',
    'Gebiidea':'#d867be',
    'Stenopodidea':'#b8e450',
    'Astacidea':'#a0a3fd',
    'Polychelida':'#deae9e',
    'Grapsoidea':'#58b5e1',
    'Xanthoidea':'#8b9388'
}

cores_familia_naive = {
    # known errors are marked in black
    'Nan':'#000000',
    # infraorder: Ascacidea - #fece5f
    'Cambaridae':'#fece5f',
    'Enoplometopidae':'#fece5f', 
    'Nephropidae':'#fece5f',    
    'Parastacidae':'#fece5f', 
        # p.s.: a cris classificou, mas não são decapoda.
        #'Cambaridae'
        #'Enoplometopidae'
        #'Parastacidae'
    # infraorder: Anomura  - #007961 (obs: Lithodidae e Coenobitidae não foram classificadas pela Cris, mas são decapoda)
    'Aeglidae':'#007961', 
    'Albuneidae':'#007961',
    'Blepharipodidae':'#007961', 
    'Chirostylidae':'#007961', 
    'Coenobitidae':'#007961',
    'Diogenidae':'#007961', 
    'Galatheidae':'#007961', 
    'Hippidae':'#007961', 
    'Lithodidae':'#007961', 
    'Munididae':'#007961', 
    'Munidopsidae':'#007961',
    'Paguridae':'#007961', 
    'Parapaguridae':'#007961', 
    'Porcellanidae':'#007961',
    
    # infraorder: Achelata - #7a2c39
    'Palinuridae':'#7a2c39',
    'Scyllaridae':'#7a2c39',

    # infraorder: Axiidea - #b67262
    'Axiidae':'#b67262',
    'Callianassidae':'#b67262',
    'Ctenochelidae':'#b67262',
    'Micheleidae':'#b67262',

    # infraorder: Brachyura - #ee4454
    'Aethridae':'#ee4454', 
    'Atelecyclidae':'#ee4454',
    'Bythograeidae':'#ee4454', 
    'Calappidae':'#ee4454',
    'Cancridae':'#ee4454', 
    'Carpiliidae':'#ee4454', 
    'Chasmocarcinidae':'#ee4454', 
    'Cryptochiridae':'#ee4454',
    'Cyclodorippidae':'#ee4454', 
    'Dairidae':'#ee4454', 
    'Domeciidae':'#ee4454', 
    'Dorippidae':'#ee4454', 
    'Dromiidae':'#ee4454', 
    'Epialtidae':'#ee4454', 
    'Eriphiidae':'#ee4454', 
    'Ethusidae':'#ee4454',
    'Euryplacidae':'#ee4454', 
    'Gecarcinidae':'#ee4454', 
    'Geryonidae':'#ee4454', 
    'Goneplacidae':'#ee4454',
    'Grapsidae':'#ee4454',
    'Homolidae':'#ee4454', 
    'Homolodromiidae':'#ee4454', 
    'Hymenosomatidae':'#ee4454', 
    'Inachidae':'#ee4454', 
    'Inachoididae':'#ee4454', 
    'Leucosiidae':'#ee4454', 
    'Majidae':'#ee4454', 
    'Menippidae':'#ee4454',
    'Mictyridae':'#ee4454',
    'Mithracidae':'#ee4454', 
    'Ocypodidae':'#ee4454',
    'Ovalipidae':'#ee4454', 
    'Palicidae':'#ee4454', 
    'Panopeidae':'#ee4454', 
    'Parthenopidae':'#ee4454',
    'Percnidae':'#ee4454',
    'Pilumnidae':'#ee4454', 
    'Pilumnoididae':'#ee4454',
    'Pinnotheridae':'#ee4454', 
    'Plagusiidae':'#ee4454', 
    'Platyxanthidae':'#ee4454',
    'Polybiidae':'#ee4454', 
    'Portunidae':'#ee4454', 
    'Pseudorhombilidae':'#ee4454', 
    'Pseudothelphusidae':'#ee4454', 
    'Raninidae':'#ee4454', 
    'Sesarmidae':'#ee4454', 
    'Symethidae':'#ee4454',
    'Trichodactylidae':'#ee4454', 
    'Trichopeltariidae':'#ee4454', 
    'Ucididae':'#ee4454', 
    'Varunidae':'#ee4454', 
    'Xanthidae':'#ee4454', 

    # infraorder: Caridea - #3330b7
    'Acanthephyridae':'#3330b7', 
    'Alpheidae':'#3330b7',
    'Anchistioididae':'#3330b7',
    'Atyidae':'#3330b7', 
    'Bathypalaemonellidae':'#3330b7', 
    'Crangonidae':'#3330b7', 
    'Disciadidae':'#3330b7', 
    'Glyphocrangonidae':'#3330b7',
    'Hippolytidae':'#3330b7', 
    'Lysmatidae':'#3330b7',
    'Nematocarcinidae':'#3330b7', 
    'Ogyrididae':'#3330b7', 
    'Oplophoridae':'#3330b7', 
    'Palaemonidae':'#3330b7',
    'Pandalidae':'#3330b7', 
    'Pasiphaeidae':'#3330b7',
    'Processidae':'#3330b7', 
    'Pseudochelidae':'#3330b7', 
    'Rhynchocinetidae':'#3330b7', 

    # infraorder: Gebiidea - #d867be
    'Upogebiidae':'#d867be',

    # infraorder: Stenopodídea - b8e450
    'Stenopodidae':'#b8e450',
        # OBS: a partir daqui, não foram classificados pela Cris
    # infraorder: Astacidea
        #'Cambaridae':'#a0a3fd',    
        #'Enoplometopidae':'#a0a3fd', 
        #'Nephropidae':'#a0a3fd', 
        #'Parastacidae':'#a0a3fd', 
    
    # infraorder: Polychelida - #deae9e
    'Polychelidae':'#a0a3fd', # aloquei a cor do grupo Astacidea, que não está mais sendo usada (para diferenciar do outro marrom)
    
    # infraorder: Grapsoidea
    # 'Grapsidae': '#d867be',
}

# cores_familia = {
#     # known errors treatment
# #     '#n/d':'#000000',
#     'Nan':'#000000',
#     # grupo 1
    
# }


## CONTINENTE
# cores_continente = {
#     "#N/D":"#5e4028",
#     "América do Sul":"#10b651",
#     "América Central":"#bce091",
#     "América do Norte":"#21638f",
#     "Ásia":"#d963cf",
#     "África":"#52e9e6",
#     "Europa":"#8d102b"
# }

cores_continente= {
    #"#N/D":"#000000",
    "NaN":"#000000",
    "Desconhecido":"#a6a6a6",
    "América do Sul":"#40a43b",
    "América Central":"#bbe272",
    "América do Norte":"#255026",
    "Ásia":"#db11ac",
    "África":"#a96370",
    "Europa":"#208eb7",
    "Oceania": "#feba53"
}


## COUNTRY 
### new approach: inspired on Hans Rosling (countries are colored the same as its continents)
# colors chosen according to the old olympics convention (see https://www.npr.org/sections/thetorch/2012/08/10/158569089/seeing-the-world-through-the-olympic-rings-and-infographicsinfographics#:~:text=The%20Olympic%20Charter%20once%20ascribed,Oceania%2C%20and%20red%20for%20America.)

# Each ring symbolizes one of the five continents competing at the Olympics: Africa (yellow), the Americas (red), Asia (green), Europe (black), and Oceania (blue)
cores_pais = {
    #'#N/D':'#000000',
    'NaN':'#000000',  # preto
    'Desconhecido':'#a6a6a6',
    'Oceano Pacifico':'#a6a6a6',
    # América do Sul
    'Brasil':'#40a43b',
    'Uruguai':'#40a43b',
    #'Colômbia':'#40a43b',
    'Peru':'#40a43b',
    #'Paraguai':'#40a43b',
    'Argentina':'#40a43b',
    #'Guiana Francesa':'#40a43b',
    'Venezuela':'#40a43b',
    #'Guiana':'#40a43b',
    'Chile':'#40a43b',
    'Equador':'#40a43b',
    'Curacao':'#40a43b',
    # América Central
    #'Guatemala':'#bbe272',
    #'Panamá':'#bbe272',
    'Panama':'#bbe272',
    #'Porto Rico':'#bbe272',
    'Costa Rica':'#bbe272',
    'Mexico':'#bbe272',
    #'Nicarágua':'#bbe272',
    #'Honduras':'#bbe272',
    #'Cuba':'#bbe272',
    #'República Dominicana':'#bbe272',
    # América do Norte
    'Estados Unidos':'#255026',
    # Ásia
    #'Israel':'#db11ac',
    'Taiwan':'#db11ac',
    #'Índia':'#db11ac',
    'Filipinas':'#db11ac',
    # África
    #'África do Sul':'#a96370',
    #'Egito':'#a96370',
    'Ilhas Mauricio':'#a96370',
    'Republica das Seicheles':'#a96370',
    # Europa
    #'Bósnia e Herzegovina':'#208eb7',
    #'Romênia':'#208eb7',
    #'Alemanha':'#208eb7',
    #'Kingdom':'#208eb7',
    'Mar Mediterraneo': '#208eb7',
    'Italia':'#208eb7',
    'Franca':'#208eb7',
    'Portugal':'#208eb7',
    'Grecia':'#208eb7',
    # Oceania
    'Indonesia':'#feba53',
    'Australia':'#feba53',
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
    #'nan':'#000000',  # missing value (black)
    'N':'#22695e',   # forest
    'NE':'#ea1349',  # hot
    'CO':'#69ef7b',  # light green vegetation (Cerrado)
    'SE':'#992a1c',  # emphatic color
    'S':'#7ee7d3'    # cold
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
    # N
    'Acre':'#22695e',
    'Amapá':'#22695e',
    'Amazonas':'#22695e',
    'Maranhão':'#22695e',
    'Pará':'#22695e',
    'Rondônia':'#22695e',
    'Roraima':'#22695e',
    'Tocantins':'#22695e',
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
    #'Brasília':'#69ef7b',
    'Distrito Federal':'#69ef7b',
    'Goiás':'#69ef7b',
    'Mato Grosso':'#69ef7b',
    'Mato Grosso do Sul':'#69ef7b',
    #'Minas Gerais/Goiás/Distrito Federal':'#69ef7b',    # ERROR IN DATABASE
    # SE
    'Espírito Santo':'#992a1c',
    'Minas Gerais':'#992a1c',
    'Rio de Janeiro':'#992a1c',
    'São Paulo':'#992a1c',
    # S
    'Paraná':'#7ee7d3',
    'Rio Grande do Sul':'#7ee7d3',
    'Santa Catarina':'#7ee7d3',
    #'Santa Catarina-Rio Grande do Sul':'#7ee7d3',        # ERROR IN DATABASE

}
