# Vis_Zoo   Fase1

Visualizações das bases de dados de algumas coleções de biodiversidade do Museu Nacional. Os dados que serviram de base para as visualizações pertencem ao [Museu Nacional](http://www.museunacional.ufrj.br/) e todos os códigos e gráficos gerados a partir dos dados devem fazer referência a esta instituição. As planilhas originais foram removidas do presente repositório para a finalidade de torná-lo público.

As visualizações foram desenvolvidas como dissertação de Mestrado do aluno Franklin Alves de Oliveira, defendida em março de 2021, orientado pela professora Asla Medeiros e Sá. O documento produzido, intitulado *Visualização de coleções científicas digitais de biodiversidade: um framework em Altair, Python*, está disponível [aqui](https://bibliotecadigital.fgv.br/dspace;handleocy-listommunity-list/handle/10438/30711). 

Adicionalmente dois artigos foram publicados:
* 2022 - Asla Medeiros e Sá, Franklin Alves de Oliveira and Bruno Schneider et al.: [Visually Overviewing Biodiversity Open Data Digital Collections](https://www.scienceopen.com/hosted-document?doi=10.14236/ewic/ODAK22.4), ODAK 2022: Symposium on Open Data and Knowledge for a Post-Pandemic Era, Brighton, UK. 

* 2021 - Asla Medeiros e Sá, Franklin Alves de Oliveira e Cristiana Silveira Serejo: [Visualização de Informação como Ferramenta de Apoio à  Curadoria de Dados em Coleções Biológicas](https://periodicos.unb.br/index.php/museologia/article/view/36709), Revista Museologia & Interdiciplinariedade, v10, n. especial 2021. 

O trabalho foi feito em colaboração com os curadores e técnicos de coleções do Museu Nacional.

## Requisitos:

Todo o código foi desenvolvido em Python 3, com uma distribuição [Anaconda](https://www.anaconda.com/distribution/). A instalação dessa distribuição é opcional. No entanto, para garantir que todo o código funcionará corretamente, é necessária a instalação das bibliotecas listadas a seguir: 

```
altair - matplotlib - numpy - pandas - pathlib2 - pywaffle
```

Para instalar cada uma delas, basta executar o seguinte comando em uma instância do terminal:

```shell
pip install nome_da_biblioteca
```

Todas as bibliotecas necessárias, assim como suas versões utilizadas para o desenvolvimento deste projeto, estão listadas no arquivo `requirements.txt`. Para instalar todas elas, basta abrir o terminal (ou Anaconda Prompt) na pasta raiz do projeto e executar o seguinte comando:

```bash
pip install -r requirements.txt
```

-----
**OBS:** Todo o código aqui apresentado foi desenvolvido em Linux (distribuição Ubuntu 19.04) e, para que funcione corretamente no Windows, deve ser feito um ajuste no caminho de pasta de cada gráfico, conforme o exemplo abaixo: 

> Considere o seguinte caminho de pasta para salvar o arquivo denominado `grafico.svg`:
```shell
./caminho/para/pasta/grafico.svg
```

> Este deve ser alterado para: 
```shell
.\\caminho\\para\\pasta\\grafico.svg
```

-----

## Conteúdo:

### Pastas:
> - **colecoes:** essa pasta contém todas as visualizações de dados agregados para todas as coleções do Museu Nacional (MN).
> - **crustacea e carcinos:** armazena todos os códigos em Python 3 (arquivos `.ipynb`) e arquivos de visualização criados para a base de dados `MN-Crustacea`.
> - **repteis:** esse diretório contém todo o material criado para exploração e visualização da base de dados `MN-Repteis`.
> - **poliqueta:** esse diretório contém todo o material criado para exploração e visualização da base de dados `MN-Polychaeta`.

-----
**Nota:** Este repositório corresponde à Fase 1 do projeto que foi concluída em 2021. Todos os dados que serviram de base para estas visualizações são referentes à bases de dados de 2020. Em breve disponibilizaremos aqui o link para a Fase 2 do projeto. 

-----

