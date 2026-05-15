# Informações sobre os modelos do Restaurador de Pontuação da PallasSpeechSystem

## Modelo de Tokenização

O modelo de tokenização foi treinado usando cerca de 5.000.000 (5 milhões de frases) escolhidas aleatoriamente do corpus de textos construídos nesse trabalho. O tamanho de vocabulário foi fixado em 32.000 (32 mil tokens), a técnica de tokenização e modelo foram "BPE (Byte-Pair Encoding)" usando SentencePiece.
Foram tokenizados cerca de 852 pontuações (A lista de pontuações usadas estão em models/tokenizer/file_symbols), a lista foi criada a partir do toolkit "Icukit".

## Modelo N-gram

O modelo n-gram foi treinado usando os corpus tokenizados pelo modelo anterior, dando cerca de 2 bilhões de tokens e 31 mil tokens unicos.
