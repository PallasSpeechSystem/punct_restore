import os
import gdown

base_path = os.getcwd()
LM_MODEL = os.path.join(base_path, "models/ngram/model_order4.binary")
SENTENCE_MODEL = os.path.join(base_path, "models/tokenizer/m32k.model")

LM_MODEL_DIR = os.path.join(base_path, "models/ngram/")
SENTENCE_MODEL_DIR = os.path.join(base_path, "models/tokenizer/")

# Track download progress
# Fonte: https://github.com/wkentaro/gdown#python
def on_progress(bytes_so_far: int, bytes_total: int| None) -> None:
    if bytes_total is not None:
        print(f"\rProgresso de Download: {bytes_so_far / bytes_total * 100:.1f}%", end="")

def verificar_modelos():    
	# Os ifs são usados para verificar que os modelos existem, se não informar qual/quais modelos não estão presentes no return da função.
	if not (os.path.exists(LM_MODEL)) and not (os.path.exists(SENTENCE_MODEL)):
		os.makedirs(LM_MODEL_DIR, exist_ok=True)
		os.makedirs(SENTENCE_MODEL_DIR, exist_ok=True)
		status_carregar_modelos = "Modelos N-Gram e Sentence não encontrado!"
		model = 1
		sp = 1
		return model, sp, status_carregar_modelos
	elif not (os.path.exists(LM_MODEL)) and (os.path.exists(SENTENCE_MODEL)):
		os.makedirs(LM_MODEL_DIR, exist_ok=True)
		status_carregar_modelos = "Modelo N-Gram não encontrado em: " + LM_MODEL
		model = 1
		sp = 0
		return model, sp, status_carregar_modelos
	elif (os.path.exists(LM_MODEL)) and not (os.path.exists(SENTENCE_MODEL)):
		os.makedirs(SENTENCE_MODEL_DIR, exist_ok=True)
		status_carregar_modelos = "Modelo sentencePiece não encontrado em: " + SENTENCE_MODEL
		model = 0
		sp = 1
		return model, sp, status_carregar_modelos
	else:
		status_carregar_modelos = "Modelos Localizados com Sucesso"
		model = 0
		sp = 0
		return model, sp, status_carregar_modelos

model, sp, status_carregar_modelos = verificar_modelos()
model_ngram_id = "https://drive.google.com/file/d/1k_SlXdCMrzyl1zPnu7bAREvlXLoB4tQg/view?usp=sharing"
model_sentencepiece_id = "https://drive.google.com/file/d/1kQLlnhZ7A6YyaW2ICjWOhfuGiWCAdqsd/view?usp=sharing"
hash_ngram_model = "sha256:f592ea0cbe15d3b5722d5b03d69e86a1e779a1150e9f514c916a81b53632c367"
hash_sentencepiece_model = "sha256:532ac70c7b92af307c0a7617998c2df4fa451de0c6bcb4b11199f97d3f022791"

if model == 1 and sp == 1:
	print(status_carregar_modelos)
	print("Baixando Modelos N-Gram e SentencePiece")
	print("Baixando Modelo N-Gram:")
	gdown.download(url=model_ngram_id, quiet=True, progress=on_progress, output=LM_MODEL)
	print()
	print("Baixando Modelo SentencePiece:")
	gdown.download(url=model_sentencepiece_id, quiet=True, progress=on_progress, output=SENTENCE_MODEL)
	print()
elif model == 0 and sp == 1:
	print(status_carregar_modelos)
	print("Baixando Modelo SentencePiece:")
	gdown.download(url=model_sentencepiece_id, quiet=True, progress=on_progress, output=SENTENCE_MODEL)
	print()
elif model == 1 and sp == 0:
	print(status_carregar_modelos)
	print("Baixando Modelo N-Gram:")
	print()
	gdown.download(id=model_ngram_id, quiet=True, progress=on_progress, output=LM_MODEL)
	print()
else:
	print(status_carregar_modelos)
	print("Você tem os modelos baixados!")