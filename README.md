
Restaurador de Pontuações para Texto baseado em N-grams e SentencePiece. 

# Metodología

Usar modelos N-grams em conjunto com SentencePiece para restaurar pontuações de textos. Usar as bibliotecas do [[KenLM]] e SentencePiece em Python, utilizando modelos quantizados.

O SentencePiece é usando no restaurador para lidar com palavras fora do vocabulário utilizando sub-palavras (*sub-words*). O corpus de treinamento vai ser passando para treinar um outro modelo de tokenização e tratar o corpus após a tokenização passar a ser treinado o modelo N-gram utilizando [[KenLM]]. 

Implementação do algoritmo **Ganacioso (Guloso)** para maximação de resultados. 

# MVP

- O restaurador irá suportar as seguintes pontuações: **!** **?** **,** **.**
- Os modelos de tokenização e de N-grams focará: **Português Brasileiro Informal (Fala Espontânea).** Tendo em vista que terá exemplos do português brasileiro formal para os modelos entendam a estrutura gramática da língua.

# To-do List 

- [ ] Implementação do [[KenLM]] e teste básico a linguagem C++;
- [ ] Testar implementação do [[KenLM]] com modelo simple e mostrar score da frase;
- [ ] Treinar modelo base sem SentencePiece;
- [ ] Testar implementação do score com *for* para diversas pontuações;
- [ ] Implementação do algoritmo guloso;

## Incluir bibliotecas principais









