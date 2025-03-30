import os
import shutil

# Obter caminho da pasta Downloads
def download_to_folder(file):
    home = os.path.expanduser('~')
    downloads_path = os.path.join(home, 'Downloads')
    arquivo_origem = os.path.join(downloads_path, file)

    # Obter diretório atual do script
    diretorio_atual = os.path.dirname(os.path.abspath(__file__))
    arquivo_destino = os.path.join(diretorio_atual, file)

    # Mover arquivo
    try:
        shutil.move(arquivo_origem, arquivo_destino)
        print(f'Arquivo movido com sucesso para {diretorio_atual}')
    except FileNotFoundError:
        print('Arquivo não encontrado na pasta Downloads')
    except PermissionError:
        print('Erro de permissão ao mover arquivo')
    except Exception as e:
        print(f'Erro ao mover arquivo: {str(e)}')