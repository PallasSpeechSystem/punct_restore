Restaurador de Pontuações para Texto baseado em N-grams e SentencePiece. 

# Metodología

Usar modelos N-grams em conjunto com SentencePiece para restaurar pontuações de textos. Usar as bibliotecas do [[KenLM]] e SentencePiece em Python, utilizando modelos quantizados.

O SentencePiece é usando no restaurador para lidar com palavras fora do vocabulário utilizando sub-palavras (*sub-words*). O corpus de treinamento vai ser passando para treinar um outro modelo de tokenização e tratar o corpus após a tokenização passar a ser treinado o modelo N-gram utilizando [[KenLM]]. 

# MVP

- O restaurador irá suportar as seguintes pontuações: **!** **?** **,** **.**
- Os modelos de tokenização e de N-grams focará: **Português Brasileiro Informal (Fala Espontânea).** Tendo em vista que terá exemplos do português brasileiro formal para os modelos entendam a estrutura gramática da língua.
- Imprentação e uso do algotitmo **Ganacioso (Guloso)** para escolha de melhor pontuação.

## To-do List 

- [ ] Definir requisitos funcionais e não funcionais;
- [ ] Organizar etapas do desenvolvimento do [[Restaurador de Pontuação]]. 
- [ ] Planejar cronograma de desenvolvimento.
	- [ ] (10/04) - Desenvolver apresentação do projeto.
	- [ ] (14/04) - Desenvolver documentação como instalação, uso e informações dos modelos. Colocar no repositório Git do projeto e no site da organização PallasSpeechSystem. 

## Requisitos 
**Requisitos Funcionais:** 

- Processar frase e retornar a frase pontuada;
- Pontuações Base da Língua Portuguesa: "." "," "!" "?"
- Implementação do Algoritmo Guloso para escolha da melhor pontuação.

**Requisitos Não Funcionais:**

- Entrada para modelos ngram e tokenizador customizados.
- Entrada de texto via linha de comando. 
	- Exemplos:
		- --text "texto" - Entrada do Texto;
		- --ngram_model - Localização do modelo ngram;
		- --token_model - Localização do modelo SentencePiece;
- Saída em txt caso informando
	- --output - Localização do arquivo de saída com texto informando se não informado retorna via **STDIN**. 


# Corpus

- Aya Collection (Portuguese Split)
- OpenSubtitles
- Tatoeba (Portuguese Split)
- BlogSet-BR

## MVP

**Formal (Basíco da Linguagem):**

- tatoeba;
- Aya Collection (Portuguese Split)

**Informal (Foco do MVP)**

- OpenSubtitles; 
- BlogSet-BR

