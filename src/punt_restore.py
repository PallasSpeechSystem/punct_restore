# Copyright (C) 2026 Pallas da Silva Guedes - PallasSpeechSystem
#This file is part of "Punct Restore".
#Punct Restore is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.
#Punct Restore is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.
#You should have received a copy of the GNU General Public License along with Punct Restore. If not, see <https://www.gnu.org/licenses/>. 
import os

from math import inf
import unicodedata
import kenlm
import sentencepiece as spm
import re
pontuacoes = ["?", ",", ".", "!", False]

# Pos-Processar Texto Final da função pontuador(), unir pontuações com a palavra
def pos_processamento(texto_final):
    texto_final_processado = re.sub(r'\s+([?,.!])', r'\1', texto_final).capitalize()
    return texto_final_processado

# Uma função para dar penalidades a pontuações para o modelo não viciar em apenas colocar pontos em tudo ou em nada.
# Valores foram escolhidos aleatóriamente, mas é possível editar para obter outros resultados.
def penalidades(pontuacao):
    if pontuacao == False:
        penalidade = 0
    elif pontuacao == "?":
        penalidade = 0.6
    elif pontuacao == ",":
        penalidade = 0.4
    elif pontuacao == ".":
        penalidade = 0.4
    elif pontuacao == "!":
        penalidade = 0.6
    else:
        penalidade = 0
    return penalidade

def carregar_modelos():
    base_path = os.getcwd()
    LM_MODEL = os.path.join(base_path, "models/ngram/model_order4.binary")
    SENTENCE_MODEL = os.path.join(base_path, "models/tokenizer/m32k.model")
    status_carregar_modelos = 0

    # Os ifs são usados para verificar que os modelos existem, se não informar qual/quais modelos não estão presentes no return da função.
    if not (os.path.exists(LM_MODEL)) and not (os.path.exists(SENTENCE_MODEL)):
        status_carregar_modelos = "Modelos N-Gram e Sentence não encontrado!"
        model = 0
        sp = 0
        return model, sp, status_carregar_modelos
    elif not (os.path.exists(LM_MODEL)) and (os.path.exists(SENTENCE_MODEL)):
        status_carregar_modelos = "Modelo N-Gram não encontrado em: " + LM_MODEL
        model = 0
        sp = 0
        return model, sp, status_carregar_modelos
    elif (os.path.exists(LM_MODEL)) and not (os.path.exists(SENTENCE_MODEL)):
        status_carregar_modelos = "Modelo sentencePiece não encontrado em: " + SENTENCE_MODEL
        model = 0
        sp = 0
        return model, sp, status_carregar_modelos
    else:
        status_carregar_models = 0
        sp = spm.SentencePieceProcessor(model_file=SENTENCE_MODEL)  # pyright: ignore[reportCallIssue]
        model = kenlm.LanguageModel(LM_MODEL)
        return model, sp, status_carregar_modelos


def pontuador(texto_normalizado, model, sp):

    palavras = texto_normalizado.split()
    palavra_anterior = ""
    palavra_posterior = ""
    texto_final = ""
    melhor_pontuacao = ""
    contexto = ""
    melhor_score = -float('inf')
    for palavra_index in range(0, len(palavras)):
        palavra_atual = palavras[palavra_index]
        melhor_pontuacao = ""
        melhor_score = -float('inf')

        # Checar que a palavra_atual não é última palavra, se não definir a próxima palavra.
        if palavra_index + 1 == len(palavras):
            palavra_posterior = False
        else:
            palavra_posterior = palavras[palavra_index + 1]

        # Checar que a palavra_atual não é primeira palavra, se não definir a palavra anterior.
        if palavra_index == 0:
            palavra_anterior = False
        else:
            palavra_anterior = palavras[palavra_index - 1]

        
        for pontuacao in pontuacoes:

            # Informal a palavra_anterior como contexto.
            if not (palavra_anterior == False):
                contexto = palavra_anterior

            # Checar caso a pontuacao for False
            # pontuacao = False (Que dizer que há pontuação).
            # Para o texto_base não ficar cheio de espações em branco desnecessarios, caso a pontuacao for False:
            # Colocar a palavra_atual + palavra_posterior.
            # Caso não houver palavra_posterior apenas colocar a palavra_atual.
            if palavra_posterior == False and pontuacao == False:
                texto_base = contexto + " " + palavra_atual
            elif palavra_posterior == False and not (pontuacao == False):
                texto_base = contexto + " " + palavra_atual + " " + pontuacao
            elif not (palavra_posterior == False) and pontuacao == False:
                texto_base = contexto + " " + palavra_atual + " " + palavra_posterior
            elif palavra_posterior == False and not (pontuacao == False):
                texto_base = contexto + " " + palavra_atual + " " + pontuacao
            else:
                texto_base = contexto + " " + palavra_atual + " " + pontuacao + " " + palavra_posterior


            # Colocar marcações de inicio de frase (<s>) e final de frase (</s>) caso não houver palavra_anterior e/ou palavra posterior
            if palavra_anterior == False and palavra_posterior == False:
                texto_tokenizado = "<s>" + " " + " ".join(sp.EncodeAsPieces(texto_base)) + " " + "</s>"         
            elif palavra_anterior == False and not (palavra_posterior == False):
                texto_tokenizado = "<s>" + " " + " ".join(sp.EncodeAsPieces(texto_base))
            elif not (palavra_anterior == False) and palavra_posterior == False:
                texto_tokenizado = " ".join(sp.EncodeAsPieces(texto_base)) + " " + "</s>"
            elif not (palavra_anterior == False) and not (palavra_posterior == False):
                texto_tokenizado = " ".join(sp.EncodeAsPieces(texto_base))
            
            score_pontuacao = model.score(texto_tokenizado) + penalidades(pontuacao)
            #print(f"Score para \"{texto_base}\" foi: {score_pontuacao}")


            if score_pontuacao > melhor_score:
                melhor_score = score_pontuacao
                melhor_pontuacao = pontuacao

        # Caso a melhor_pontuacao for igual a False ("Sem pontuação"), apenas colocar a palavra_atual
        if melhor_pontuacao == False:
            texto_final = texto_final + " " + palavra_atual
        else:
            texto_final = texto_final + " " + palavra_atual + " " + melhor_pontuacao
        #print(f"Texto final foi: {texto_final}")
    return texto_final

def restaurar_pontuacao(texto):
    model, sp, status = carregar_modelos()

    if not (status == 0):
        return "ERRO: " + status
    else:
        # Uso da função unicodedata.normalize() é garantir que os acertos da palavras sejam processandos corretamente.
        texto_normalizado = unicodedata.normalize("NFC", texto).lower()
        return pos_processamento(pontuador(texto_normalizado, model, sp))
