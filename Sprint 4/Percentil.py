import pandas as pd
import numpy as np

# Carregar os dados da planilha Excel
file_path = 'C:/Users/DELTA TECNOLOGIA/Desktop/Power BI/antaq_2015_2023.xlsx'  # Substitua pelo caminho do seu arquivo

# Ler a planilha inteira
df = pd.read_excel(file_path)

# Calcular o nono percentil das colunas desejadas
percentil_90_atracacao = np.percentile(df['Espera_Atracação'], 90)
percentil_90_operacao = np.percentile(df['Espera_Operação'], 90)
percentil_90_op = np.percentile(df['Operação'], 90)
percentil_90_desatracacao = np.percentile(df['Espera_Desatracação'], 90)

# Criar um DataFrame para armazenar os resultados
result_df = pd.DataFrame({
    'Métrica': [
        'Nono percentil Espera_Atracação',
        'Nono percentil Espera_Operação',
        'Nono percentil Operação',
        'Nono percentil Espera_Desatracação'
    ],
    'Valor': [
        percentil_90_atracacao,
        percentil_90_operacao,
        percentil_90_op,
        percentil_90_desatracacao
    ]
})

# Salvar os resultados em um novo arquivo Excel
output_file_path = 'C:/Users/DELTA TECNOLOGIA/Desktop/Power BI/resultados.xlsx'
with pd.ExcelWriter(output_file_path) as writer:
    df.to_excel(writer, sheet_name='Dados Originais', index=False)
    result_df.to_excel(writer, sheet_name='Resultados', index=False)

print("Resultados salvos em:", output_file_path)
