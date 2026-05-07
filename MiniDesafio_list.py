#nome do usuário
nome = input("Digite seu nome: ")

#lista para guardar as pontuações
pontuacoes = []

#leitura das 6 pontuações
for i in range(6):
    ponto = float(input(f"Digite o valor da ação {i + 1}: "))
    pontuacoes.append(ponto)
#total das pontuações
total = sum(pontuacoes)

#média
media = total / len(pontuacoes)

#contador de ações com pontuação >= 80
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
print(f"\nParabéns, {nome}! Continue praticando ações sustentáveis!")