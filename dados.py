import csv

alturas = []
pesos = []
nomes = []
sobrenomes = []
imc = []

with open('dataset.CSV','r',encoding='ISO-8859-1') as arquivo:
    ler = csv.reader(arquivo, delimiter=';')
    next(ler) 

    
    
    for linha in ler:
        nome = linha[0]
        sobrenome = linha[1]
        peso = linha[2]
        altura = linha[3]
        
        nomes.append(nome)
        sobrenomes.append(sobrenome)

        try:
            alturas.append(float(altura.replace(',', '.')))
            pesos.append(float(peso.replace(',', '.')))
        except Exception as e:
            pass
        else:
            pass
        finally:
            pass
        
    


    for altura, peso in zip(alturas, pesos): 
        imc.append(peso/(altura**2))

    arquivo_out = open('nome_novo_arquivo.txt','w')

    for nome,sobrenome,valor in zip(nomes,sobrenomes,imc):
        
        arquivo_out.write(' '.join([nome.upper().strip(),sobrenome.upper().strip(),str(round(valor,2)),'\n']))
    
    arquivo_out.close()

