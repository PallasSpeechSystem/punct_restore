# Como instalar o restaurador

1. Clone o repositório do Github do restaurador:

```shell
git clone https://github.com/PallasSpeechSystem/punct_restore
``` 

2. Criação de container:

Para usar o restaurador é necessário criar um container python (.venv) para isolamento e instalação correta das bibliotecas necéssarias.

  **Linux:**

  ```shell
  python3 -m venv .venv
  source .venv/bin/activate
  ``` 

  **Windows: (PowerShell)**

  ```powershell
  python3 -m venv .venv
  Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
  . .venv/bin/Activate.ps1
  ```

3. Instalação das bibliotecas necessárias:

  ```shell
  pip install -r requirements.txt
  ```

4. Rode a interface do restaurador:

  ```shell
  python3 app.py
  ```
