#Nome do usuário
nome = input("Digite seu nome: ")

#Lista para guardar as pontuações
pontuacoes = []

#Leitura das 6 pontuações
for i in range(6):
    ponto = float(input(f"Digite a pontuação da ação {i + 1}: "))
    pontuacoes.append(ponto)
#Total das pontuações
total = sum(pontuacoes)

#Média
media = total / len(pontuacoes)

#Contador de ações com pontuação >= 80
quantidade_destaques = 0

for valor in pontuacoes:
    if valor >= 80:
        quantidade_destaques += 1

#Resultados
print("\n--- RESULTADO ---")
print(f"Usuário: {nome}")
print(f"Pontuações: {pontuacoes}")
print(f"Total: {total}")
print(f"Média: {media:.2f}")
print(f"Ações com pontuação maior ou igual a 80: {quantidade_destaques}")

#Mensagem final personalizada
print(f"\nParabéns, {nome}! Continue praticando ações sustentáveis!")