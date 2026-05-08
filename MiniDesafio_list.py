#Mini Desafio Complementar do CP
#Membros do grupo:
#Tárik Moussa Alma - RM: 571411
#Fabrício Aquiles - RM: 570985

print("------------------------ Menu ------------------------")
#nome do usuário
nome = input("Digite seu nome: ")

#lista
pontuacoes = []

#leitura das 6 pontuações
for i in range(6):
    ponto = float(input(f"Digite o valor da ação {i + 1}: "))
    pontuacoes.append(ponto)
#total
total = sum(pontuacoes)

#média
media = total / len(pontuacoes)

#contador com pontuação >= 80
quantidade_destaques = 0
for valor in pontuacoes:
    if valor >= 80:
        quantidade_destaques += 1

#resultados
print("\n----------------------- RESULTADO --------------------")
print(f"Usuário: {nome}")
print(f"Pontuações: {pontuacoes}")
print(f"Total: {total}")
print(f"Média: {media:.2f}")
print(f"Ações com pontuação maior ou igual a 80: {quantidade_destaques}")

#mensagem final personalizada
print(f"\nParabéns, {nome}! Você acumulou {total} pontos. Sua média foi {media:.2f} e teve {quantidade_destaques} ações de destaque.")
print("\nContinue praticando ações sustentáveis e contribuindo com o planeta!! Vê se não usa canudo, as tartarugas também são importantes...!")