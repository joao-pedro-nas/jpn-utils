import os
import shutil

def download_to_folder(file):
    home = os.path.expanduser('~')
    downloads_path = os.path.join(home, 'Downloads')
    arquivo_origem = os.path.join(downloads_path, file)

    # ➤ Diretório atual de execução (do script que está rodando)
    diretorio_execucao = os.getcwd()
    arquivo_destino = os.path.join(diretorio_execucao, file)

    try:
        shutil.move(arquivo_origem, arquivo_destino)
        print(f'Arquivo movido com sucesso para {diretorio_execucao}')
    except FileNotFoundError:
        print('Arquivo não encontrado na pasta Downloads')
    except PermissionError:
        print('Erro de permissão ao mover arquivo')
    except Exception as e:
        print(f'Erro ao mover arquivo: {str(e)}')