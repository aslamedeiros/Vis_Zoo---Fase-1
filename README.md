# MN_Viz

Visualizações das bases de dados e coleções do Museu Nacional. Esse repositório é constituído por arquivos pertencentes ao [Museu Nacional](http://www.museunacional.ufrj.br/) e todos os códigos e gráficos nele gerados são de propriedade dessa instituição. 

## Requisitos:

Todo o código foi desenvolvido em Python 3, com uma distribuição [Anaconda](https://www.anaconda.com/distribution/). A instalação dessa distribuição é opcional. No entanto, para garantir que todo o código funcionará corretamente, é necessária a instalação das bibliotecas listadas a seguir: 

```
altair - matplotlib - numpy - pandas - pathlib2 - pywaffle
```

Para instalar cada uma delas, basta executar o seguinte comando em uma instância do terminal:

```bash 
pip install nome_da_biblioteca
```

Todas as bibliotecas necessárias, assim como suas versões utilizadas para o desenvolvimento deste projeto, estão listadas no arquivo `requirements.txt`. Para instalar todas elas, basta abrir o terminal (ou Anaconda Prompt) na pasta raiz do projeto e executar o seguinte comando:

```bash
pip install -r requirements.txt
```

-----
**OBS:** Todo o código aqui apresentado foi desenvolvido em Linux (distribuição Ubuntu 19.04) e, para que funcione corretamente no Windows, deve ser feito um ajuste no caminho de pasta de cada gráfico, conforme o exemplo abaixo: 

> Considere o seguinte caminho de pasta para salvar o arquivo denominado `grafico.svg`:
```bash
./caminho/para/pasta/grafico.svg
```

> Este deve ser alterado para: 
```bash
.\\caminho\\para\\pasta\\grafico.svg
```

-----


## Conteúdo:

### Pastas:
> - **depth:** pasta que contém todas as visualizações de profundidade dos animais catalogados.
> - **types:** contém todos os gráficos de tipos (por pesquisador, por espécie e por ano).
> - **waffles:** pasta que armazena os *Waffle Charts* das coleções do Museu por departamento.
> - **viz_old:** essa pasta contém arquivos de visualização criados no início do projeto. Seu objetivo é apenas armazenar o histório de mudanças nos gráficos. As versões mais recentes e aprimoradas de cada um dos seus arquivos estão presentes nas três pastas citadas acima (`depth`, `types` e `waffles`). 

### Arquivos:
> - **Planilha geral Atualizda FINAL com correções.xlsx:** Base de dados `crustacea`.
> - **db.csv:** Base de dados `crustacea` pré-processada (alguns nomes e formatos de colunas foram ajustados). OBS: esse é o arquivo importado nos notebooks de visualização dessa base.
> - **Dados gerais de coleção MN_29_09_19 enviado KELLNER_Asla.xlsx:** Base de dados agregada das coleções do Museu Nacional. 
> - **DB_exploration.ipynb:** IPython notebook com detalhes sobre a exploração e os ajustes realizados na base de dados `crustacea`.
> - **Types_counts_per_year.ipynb:** notebook para criação dos gráficos da contagem de Tipos por ano.
> - **Types_per_researcher.ipynb:** contém o código usado para criação dos gráficos de Tipos por pesquisador.
> - **Types_per_species.ipynb:** notebook com código para criação das visualizações de Tipos por espécie.
> - **Waffle_charts.ipynb:** notebook para criação dos *Waffle Charts* das coleções do Museu por departamento.


-----
**Nota:** Esse projeto ainda é um trabalho em progresso e as visualizações aqui criadas estão em constante aperfeiçoamento. 

-----

