import re

def gerar_faixas_versao(requirements_path, output_path):
    with open(requirements_path, "r") as f:
        linhas = f.readlines()

    faixas = []

    for linha in linhas:
        linha = linha.strip()
        if not linha or linha.startswith("#"):
            continue
        if "@" in linha:
            continue  # ignora repositórios git, por enquanto

        # Extrai nome e versão do pacote
        match = re.match(r"([a-zA-Z0-9_\-]+)==(\d+)\.(\d+)", linha)
        if match:
            nome = match.group(1)
            major = int(match.group(2))
            minor = int(match.group(3))
            proxima_major = major + 1
            faixa = f"{nome}>={major}.{minor},<{proxima_major}.0"
            faixas.append(faixa)
        else:
            print(f"⚠️ Ignorado (formato inesperado): {linha}")

    with open(output_path, "w") as f:
        f.write("\n".join(faixas))

    print(f"✅ Arquivo '{output_path}' gerado com sucesso!")

# if __name__ == '__main__':
#     # Caminhos dos arquivos
#     requisitos_congelados = "requirements.txt"
#     saida_faixas = "requirements_setup.txt"

#     # Executa a conversão
#     gerar_faixas_versao(requisitos_congelados, saida_faixas)