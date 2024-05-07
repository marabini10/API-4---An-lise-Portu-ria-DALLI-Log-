import pandas as pd
import os

def merge_csv_files(folder_path, output_file):
    # Lista todos os arquivos CSV no diretório fornecido
    csv_files = [file for file in os.listdir(folder_path) if file.endswith('.csv')]
    
    # Verifica se há arquivos CSV para processar
    if not csv_files:
        print("Nenhum arquivo CSV encontrado no diretório.")
        return
    
    # Lista para armazenar os DataFrames de cada arquivo CSV
    dfs = []
    
    # Loop pelos arquivos CSV
    for file in csv_files:
        # Extrai o ano do nome do arquivo
        year = file[:4]
        # Lê o arquivo CSV
        df = pd.read_csv(os.path.join(folder_path, file), delimiter=';')
        # Adiciona uma coluna com o ano
        df['Ano'] = year
        # Adiciona o DataFrame à lista
        dfs.append(df)
    
    # Concatena todos os DataFrames em um único DataFrame
    merged_df = pd.concat(dfs, ignore_index=True)
    
    # Salva o DataFrame combinado em um novo arquivo CSV
    merged_df.to_csv(output_file, index=False, sep=';')

# Caminho para o diretório contendo os arquivos CSV
folder_path = "C:/Users/Usuário/Desktop/ARQUIVOS"
# Nome do arquivo de saída combinado
output_file = "C:/Users/Usuário/Desktop/arquivo_combinado.csv"

# Chama a função para fazer o merge dos arquivos CSV
merge_csv_files(folder_path, output_file)
