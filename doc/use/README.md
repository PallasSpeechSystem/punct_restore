# Como instalar o restaurador

1. Clone o repositório do Github do restaurador:

```shell
git clone https://github.com/PallasSpeechSystem/punct_restore
``` 

2. Criação de container:

**Aviso:** É necessário ter o Python versão 3.12 instalada, a versão recente (Python 3.14) está sofrendo de incompatilibilidade com a ferramenta KenLM.

Para usar o restaurador é necessário criar um container python (.venv) para isolamento e instalação correta das bibliotecas necéssarias.

  **Linux:**

  ```shell
  python3.12 -m venv .venv
  source .venv/bin/activate
  ``` 

  **Windows: (PowerShell)**

  ```powershell
  python3.12 -m venv .venv
  Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
  . .venv/bin/Activate.ps1
  ```

3. Instalação das bibliotecas necessárias:

  ```shell
  pip install -r requirements_user.txt
  ```

4. Baixar os modelos:

Para usar o restaurador é necessário baixar os modelos, para isso rode o seguinte comando:

  ```shell
  python3.12 src/download_models.py
  ```

Caso houver baixado os modelos antes ou rodar novamente o comando, aparecerá na tela a seguinte mensagem:
 
  ```shell
  Você tem os modelos baixados!
  ```

Isso significar que os modelos estão baixado.

5. Rode a interface do restaurador:

  ```shell
  streamlit app.py
  ```
