import csv

arquivo = open('emails.csv','r')

linhas = csv.reader(arquivo)
for linha in linhas:
    print(linha)

arquivo.close()
