with open("lista.txt", "r") as arquivo:
    for linha in arquivo:
        linha = linha.strip("\n")
        with open(linha, "r") as arq:
                for f in arq.readlines():
                    if(f.find('Name')>-1):
                        print linha
                        print f
