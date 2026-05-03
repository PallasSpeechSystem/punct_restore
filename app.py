# Importa função de restaurar pontuação do moto
from src.punt_restore import restaurar_pontuacao

# Uso Geral:
# A função restaurar_pontuacao é necessário fornecer um texto ou uma string.
# A função retornará uma string com texto pontuado como resposta.
# Caso, ocorra erros a função restaurar_pontuacao retornará qual erro é
resultado = restaurar_pontuacao("oi")

print(resultado)
