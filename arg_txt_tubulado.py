# Dados a serem salvos no arquivo
dados = [
    ["Nome", "Idade", "Profissão"],
    ["Alice", "25", "Engenheira"],
    ["Bob", "30", "Designer"],
    ["Carol", "22", "Estudante"]
]

# Criando o arquivo tabulado
with open("arquivo_tabulado.txt", "w") as file:
    for linha in dados:
        file.write("\t".join(linha) + "\n")  # Junta os elementos com tabulação e adiciona uma quebra de linha
