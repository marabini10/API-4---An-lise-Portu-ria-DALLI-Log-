import csv

def txt_to_csv(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as txtfile:
        lines = txtfile.readlines()
    
    with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile, delimiter=';')
        for line in lines:
            # Remove espaços em branco extras e quebras de linha
            line = line.strip()
            # Divide a linha em colunas com base no ponto e vírgula como delimitador
            columns = line.split(';')
            writer.writerow(columns)

# Substitua 'input.txt' pelo caminho do seu arquivo de texto de entrada e 'output.csv' pelo nome do arquivo CSV de saída
txt_to_csv('C:/Users/Usuário/Desktop/API 4/Dados Atracacao/2015Atracacao.txt', 'C:/Users/Usuário/Desktop/2015atracacao.csv')
txt_to_csv('C:/Users/Usuário/Desktop/API 4/Dados Carga/2015Carga.txt', 'C:/Users/Usuário/Desktop/2015carga.csv')