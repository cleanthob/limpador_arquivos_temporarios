import os
print("""    __    _                                                 _                 
   / /   (_)___ ___  ____  ____ _   ____ __________ ___  __(_)   ______  _____
  / /   / / __ `__ \/ __ \/ __ `/  / __ `/ ___/ __ `/ / / / / | / / __ \/ ___/
 / /___/ / / / / / / /_/ / /_/ /  / /_/ / /  / /_/ / /_/ / /| |/ / /_/ (__  ) 
/_____/_/_/ /_/ /_/ .___/\__,_/   \__,_/_/   \__, /\__,_/_/ |___/\____/____/  
                 /_/                           /_/                            """)
diretorios = [rf"C:\Users\{os.getlogin()}\AppData\Local\Temp", r"C:\Windows\Prefetch"]
for diretorio in diretorios:
    for arquivo in os.listdir(diretorio):
        caminho_do_arquivo = os.path.join(diretorio, arquivo)
        try:
            os.remove(caminho_do_arquivo)
        except OSError:
            print(f"Não foi possível remover o arquivo {arquivo}")
print("Limpeza concluída!")
fechar = input("Aperte enter para fechar o programa! ")







