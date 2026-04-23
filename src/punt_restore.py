import os

import kenlm
import sentencepiece as spm

puntuacao = ["?", ",", ".", "!"]


def carregar_modelos():
    LM_MODEL = os.path.join(os.getcwd(), "models/ngram/modelo.binary")
    SENTENCE_MODEL = os.path.join(os.getcwd(), "models/tokenizer/m_32k.model")

    if __name__ == "__main__":
        LM_MODEL = os.path.join(os.getcwd(), "models/ngram/modelo.binary")
        SENTENCE_MODEL = os.path.join(os.getcwd(), "models/tokenizer/m_32k.model")

    sp = spm.SentencePieceProcessor(model_file=SENTENCE_MODEL)
    model = kenlm.LanguageModel(LM_MODEL)
    return 0


def restaurar_pontuacao(texto):
    # carregar_modelos()
    return "texto pontuado"
