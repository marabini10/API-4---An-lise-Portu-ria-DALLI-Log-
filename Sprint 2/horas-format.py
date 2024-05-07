import pandas as pd

# Função para converter números decimais em horas
def converter_para_horas(numero_decimal):
    partes = str(numero_decimal).split(',')
    horas = int(partes[0])
    minutos = 0
    if len(partes) > 1:
        minutos = round(int(partes[1]) * 0.6)
    return f"{horas:02d}:{minutos:02d}"

# Carregar o arquivo CSV
df = pd.read_csv('C:/Users/Usuário/Desktop/ANTAQ-1523.csv', delimiter=';')

# Aplicar a função de conversão às colunas desejadas
colunas_para_converter = ['Espera_Atracação', 'Espera_Operação', 'Operação', 'Espera_Desatracação']
for coluna in colunas_para_converter:
    df[coluna] = df[coluna].apply(converter_para_horas)

# Salvar o DataFrame modificado em um novo arquivo CSV
df.to_csv('C:/Users/Usuário/Desktop/arquivo_modificado.csv', index=False, sep=';', encoding='utf-8')
