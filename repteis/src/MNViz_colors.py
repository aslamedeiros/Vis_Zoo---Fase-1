# Paletas de cores
## ORDEM
cores_ordem = {   # p.s.: Caudata is an error and should be removed
    'Squamata': '#BF4417',
    'Testudines': '#D9CB0B', 
    'Crocodylia': '#284021'   
}

cores_familia = {
    # known errors treatment
#     '#n/d':'#000000',
#     'nan':'#000000',
    # grupo 1: Crocodylia
    'Alligatoridae':'#142611',
    # grupo 2: Testudines
    'Cheloniidae':'#bafd62',
    'Chelydridae':'#9feb3f',
    'Dermochelyidae':'#85d907',
    'Emydidae':'#6cc700',
    'Geoemydidae':'#52b700',
    'Kinosternidae':'#35a600',
    'Testudinidae':'#0b9700',
    'Trionychidae':'#008800',
    'Chelidae':'#006400',
    'Podocnemididae':'#004100',
    # grupo 4: Amphisbaenia - Amphisbaenia
    'Amphisbaenidae':'#F2CB07',
    # grupo 5: Sauria - Iguania
    'Dactyloidae':'#f8dcf9',
    'Agamidae':'#ebc5ed',
    'Chamaeleonidae':'#ddafe2',
    'Iguanidae':'#ce9ad6',
    'Hoplocercidae':'#bf86cc',
    'Leiosauridae':'#af73c2',
    'Polychrotidae':'#a160b8', 
    'Liolaemidae':'#924fae',
    'Phrynosomatidae':'#833fa4',
    'Tropiduridae':'#803da1',
    # grupo 6: Sauria - Scleroglossa
    'Scincidae':'#c9fff9',
    'Anguidae':'#b3eff2',
    'Lacertidae':'#9cdcea',
    'Gymnophthalmidae':'#83c9e2',
    'Helodermatidae':'#68b7da',
    'Xantusiidae':'#4aa6d2',
    'Gekkonidae':'#2096ca',
    'Phyllodactylidae':'#0087c1',
    'Sphaerodactylidae':'#0079b7',
    'Varanidae':'#226ca2',
    'Teiidae':'#005e98',
    # grupo 7: Serpentes - Scolecophidia
    'Anomalepididae':'#bfbfbf',
    'Leptotyphlopidae':'#8a8a8a',
    'Typhlopidae':'#595959', 
    # grupo 8: Alethinophidia
    'Dipsadidae':'#ffce9f',
    'Natricidae':'#ffb683',
    'Homalopsidae':'#ff9f69',
    'Colubridae':'#ff8851',
    'Lamprophiidae':'#f5723b',
    'Pythonidae':'#e75b25',
    'Boidae':'#d9430d', 
    'Aniliidae':'#cb2800',
    'Loxocemidae':'#bc0000',
    'Elapidae':'#c62f00',
    'Tropidophiidae':'#b41b00',
    'Xenopeltidae':'#a40300',
    'Viperidae':'#930000'
}


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
    "#N/D":"#000000",
    #"nan":"#000000",  # tratei separado, por ora
    "América do Sul":"#40a43b",
    "América Central":"#bbe272",
    "América do Norte":"#255026",
    "Ásia":"#db11ac",
    "África":"#a96370",
    "Europa":"#208eb7"
}


## COUNTRY (different shades of its CONTINENT color - selected using Colorcrafter)
### América do Sul
### ['#bbffd4', '#94efc6', '#57d5c9', '#00b8cc', '#0096c9', '#0071ba', '#004da4', '#002e8b', '#00237a']
### '#a6d2eb', '#9ebdcb'
### América Central
### ['#e3ff63', '#caf94f', '#b2e439', '#9acf1c', '#81ba00', '#69a600', '#519200', '#3a7e00', '#256b00']
### Ásia
### ['#f0c0d7', '#e5aec6', '#d89bb2', '#cb879c', '#bc7386', '#ad6274', '#9e5466', '#8f485a', '#803e4c']
### África
### ['#ffceb2', '#ffba94', '#efaa79', '#d39a5f', '#ba8a47', '#a57b34', '#956c25', '#895d1a', '#815010']
### Europa
### ['#ffcea9', '#ffb996', '#ffa583', '#ff916f', '#ff7d5c', '#eb6949', '#d25638', '#ba4327', '#a52e17']

### p.s.: old approach
# cores_pais = {
#     '#N/D':'#5e4028',
#     'nan':'#000000',  # preto
#     # América do Sul
#     'Brasil':'#00237a',
#     'Uruguai':'#002e8b',
#     'Colômbia':'#004da4',
#     'Peru':'#0071ba',
#     'Paraguai':'#0096c9',
#     'Argentina':'#00b8cc',
#     'Guiana Francesa':'#57d5c9',
#     'Venezuela':'#94efc6',
#     'Guiana':'#9ebdcb',
#     'Chile':'#bbffd4',
#     'Equador':'#a6d2eb',
#     # América Central
#     'Guatemala':'#e3ff63',
#     'Panamá':'#caf94f',
#     'Porto Rico':'#b2e439',
#     'Costa Rica':'#9acf1c',
#     'México':'#256b00',
#     'Nicarágua':'#81ba00',
#     'Honduras':'#69a600',
#     'Cuba':'#519200',
#     'República Dominicana':'#3a7e00',
#     # América do Norte
#     'Estados Unidos':'#80c6b8',
#     # Ásia
#     'Israel':'#803e4c',
#     'Indonésia':'#9e5466',
#     'Índia':'#bc7386',
#     'Filipinas':'#d89bb2',
#     # África
#     'África do Sul':'#ba8a47',
#     'Egito':'#efaa79',
#     # Europa
#     'Bósnia e Herzegovina':'#ffb996',
#     'Romênia':'#ff916f',
#     'Alemanha':'#eb6949',
#     'Kingdom':'#ba4327'
# }


### new approach: inspired on Hans Rosling (countries are colored the same as its continents)
# colors chosen according to the old olympics convention (see https://www.npr.org/sections/thetorch/2012/08/10/158569089/seeing-the-world-through-the-olympic-rings-and-infographicsinfographics#:~:text=The%20Olympic%20Charter%20once%20ascribed,Oceania%2C%20and%20red%20for%20America.)

# Each ring symbolizes one of the five continents competing at the Olympics: Africa (yellow), the Americas (red), Asia (green), Europe (black), and Oceania (blue)
cores_pais = {
    '#N/D':'#000000',
    'nan':'#000000',  # preto
    # América do Sul
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
    # América Central
    'Guatemala':'#bbe272',
    'Panamá':'#bbe272',
    'Porto Rico':'#bbe272',
    'Costa Rica':'#bbe272',
    'México':'#bbe272',
    'Nicarágua':'#bbe272',
    'Honduras':'#bbe272',
    'Cuba':'#bbe272',
    'República Dominicana':'#bbe272',
    # América do Norte
    'Estados Unidos':'#255026',
    # Ásia
    'Israel':'#db11ac',
    'Indonésia':'#db11ac',
    'Índia':'#db11ac',
    'Filipinas':'#db11ac',
    # África
    'África do Sul':'#a96370',
    'Egito':'#a96370',
    # Europa
    'Bósnia e Herzegovina':'#208eb7',
    'Romênia':'#208eb7',
    'Alemanha':'#208eb7',
    'Kingdom':'#208eb7'
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

# SE: ['#f6ccd0', '#eababc', '#dba9a6', '#cb968e', '#bb8377', '#ab7364', '#9c6556', '#8d594b', '#7d4f3f']
# NE: ['#ffc7aa', '#ffb499', '#ffa389', '#ff917a', '#ff7f68', '#f36e5a', '#df5d4b', '#cc4c3e', '#b83b2f']
# S: ['#9bffff', '#72f7fd', '#3be5f4', '#00d3ea', '#00c2e0', '#00b2d6', '#00a2cc', '#0093c1', '#0084b5']
# N: ['#c5e1cf', '#afd2c1', '#97c2b3', '#7db2a6', '#63a098', '#4c908a', '#3d827d', '#337570', '#2a6866']
# CO: ['#fffdfd', '#efeef0', '#d8dee3', '#c1ccd7', '#a8bac9', '#94aabb', '#869bad', '#7b8d9f', '#738093']

## old approach
# cores_estados = {
#     # SE
#     'Rio de Janeiro':'#8d594b',
#     'São Paulo':'#ab7364',
#     'Espírito Santo':'#cb968e',
#     'Minas Gerais':'#eababc',
#     # NE
#     'Pernambuco':'#b83b2f',
#     'Bahia':'#cc4c3e',
#     'Ceará':'#df5d4b',
#     'Paraíba':'#f36e5a',
#     'Alagoas':'#ff7f68',
#     'Piauí':'#ff917a',
#     'Rio Grande do Norte':'#ffa389',
#     'Sergipe':'#ffb499',
#     # S
#     'Paraná':'#0084b5',
#     'Santa Catarina':'#00a2cc',
#     'Rio Grande do Sul':'#00c2e0',
#     'Santa Catarina-Rio Grande do Sul':'#3be5f4',        # ERRO NA BASE
#     # N
#     'Amazonas':'#2a6866',
#     'Roraima':'#337570',
#     'Pará':'#3d827d',
#     'Acre':'#4c908a',
#     'Rondônia':'#63a098',
#     'Maranhão':'#7db2a6',
#     'Amapá':'#97c2b3',
#     'Tocantins':'#afd2c1',
#     # CO
#     'Goiás':'#7b8d9f',
#     'Mato Grosso':'#869bad',
#     'Mato Grosso do Sul':'#94aabb',
#     'Distrito Federal':'#a8bac9',
#     'Brasília':'#c1ccd7',
#     'Minas Gerais/Goiás/Distrito Federal':'#d8dee3',    # ERRO NA BASE
# }

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
    'Brasília':'#69ef7b',
    'Distrito Federal':'#69ef7b',
    'Goiás':'#69ef7b',
    'Mato Grosso':'#69ef7b',
    'Mato Grosso do Sul':'#69ef7b',
    'Minas Gerais/Goiás/Distrito Federal':'#69ef7b',    # ERROR IN DATABASE
    # SE
    'Espírito Santo':'#992a1c',
    'Minas Gerais':'#992a1c',
    'Rio de Janeiro':'#992a1c',
    'São Paulo':'#992a1c',
    # S
    'Paraná':'#7ee7d3',
    'Rio Grande do Sul':'#7ee7d3',
    'Santa Catarina':'#7ee7d3',
    'Santa Catarina-Rio Grande do Sul':'#7ee7d3',        # ERROR IN DATABASE

}
