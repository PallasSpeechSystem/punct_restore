# Importa função de restaurar pontuação do moto
from src.punt_restore import restaurar_pontuacao
import streamlit as st
# Uso Geral:
# A função restaurar_pontuacao é necessário fornecer um texto ou uma string.
# A função retornará uma string com texto pontuado como resposta.
# Caso, ocorra erros a função restaurar_pontuacao retornará qual erro é
# resultado = restaurar_pontuacao("oi")

#  Função para retornar erro caso não houver texto no campo.
def vericar_texto(texto):
	if texto == None or texto == "":
		st.error("Erro: Por favor, digite um texto no campo de texto!")
	else:
		st.session_state.clicked = True

# Tela Inicial do Restaurador
st.title("Restaurador de Pontuação para :yellow[Português] :green[Brasileiro] Falando")
st.text("Coloque pontuações em suas transcrições de áudio de forma autómatica sem ter muito trabalho!")
texto = st.text_input("Texto sem Pontuação:", "isso é um exemplo de texto sem pontuações", help="Esse campo de texto abaixo serve para colocar seu texto sem pontuações.", icon=":material/text_fields:")
st.button("Processar Texto", help="Esse botão abaixo serve para que execute o processamento do seu texto que foi colocado no campo de texto acima.", on_click=vericar_texto(texto))

st.markdown("**Resultado Final:**")

if st.session_state.clicked == True:
	resultado = restaurar_pontuacao(texto)

st.write(resultado)
