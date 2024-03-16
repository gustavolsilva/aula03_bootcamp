#%%
### Exercício 1: Verificação de Qualidade de Dados
# Você está analisando um conjunto de dados de vendas e precisa garantir 
# que todos os registros tenham valores positivos para `quantidade` e `preço`. 
# Escreva um programa que verifique esses campos e imprima "Dados válidos" se ambos 
# forem positivos ou "Dados inválidos" caso contrário.
quantidade = 9
preco = -5

if preco > 0 and quantidade > 0:
    print("Dados válidos")
else:
    print("Dados inválidos")


#%%
### Exercício 2: Classificação de Dados de Sensor
# Imagine que você está trabalhando com dados de sensores IoT. 
# Os dados incluem medições de temperatura. Você precisa classificar cada leitura 
# como 'Baixa', 'Normal' ou 'Alta'. Considerando que:
# Temperatura < 18°C é 'Baixa'
# Temperatura >= 18°C e <= 26°C é 'Normal'
# Temperatura > 26°C é 'Alta'

temperatura = 22

if temperatura < 18:
    print("Baixa")
elif temperatura >=18 and temperatura <= 26:
    print("Normal")
else:
    print("Alta")

#%%

### Exercício 3: Filtragem de Logs por Severidade
# Você está analisando logs de uma aplicação e precisa filtrar mensagens 
# com severidade 'ERROR'. Dado um registro de log em formato de dicionário 
# como `log = {'timestamp': '2021-06-23 10:00:00', 'level': 'ERROR', 'message': 'Falha na conexão'}`, 
# escreva um programa que imprima a mensagem se a severidade for 'ERROR'.

log = {
    'timestamp': '2021-06-23 10:00:00', 
    'level': 'ERROR',
    'message': 'Falha na conexão'
}

if log['level'] == "ERROR":
    msg = log['message']
else:
    msg = "Sucesso!"

print(f"{msg}")

#%%

### Exercício 4: Validação de Dados de Entrada
# Antes de processar os dados de usuários em um sistema de recomendação, 
# você precisa garantir que cada usuário tenha idade entre 18 e 65 anos e tenha 
# fornecido um email válido. Escreva um programa que valide essas condições 
# e imprima "Dados de usuário válidos" ou o erro específico encontrado.

idade = 17
email = 'email@email.com'

if idade >= 18 and ("@" in email and "." in email):
    print("Dados de usuário válidos")
elif idade < 18:
    print("Idade fora do intervalo permitido")
elif "@" in email and "." in email:
    print("Seu e-mail está inválido. Volte e digite novamente")

#%%
    
### Exercício 5: Detecção de Anomalias em Dados de Transações
# Você está trabalhando em um sistema de detecção de fraude e precisa identificar 
# transações suspeitas. Uma transação é considerada suspeita se o valor for superior 
# a R$ 10.000 ou se ocorrer fora do horário comercial (antes das 9h ou depois das 18h). 
# Dada uma transação como `transacao = {'valor': 12000, 'hora': 20}`, verifique se ela é suspeita.

transacao = {'valor': 12000, 'hora': 20}

if transacao["valor"] > 10000 or transacao["hora"] < 9 or transacao["hora"] > 18:
    print("Suspeita de Fraude!")
else:
    print("Transação válida")

#%%

### Exercício 6. Contagem de Palavras em Textos
# Objetivo:** Dado um texto, contar quantas vezes cada palavra única aparece nele.

texto = "Hoje e nossa segunda aula do bootcamp, bootcamp de python"
novo_texto = texto.replace(",","")

palavras = novo_texto.split(" ")
print(palavras)
contagem_de_palavras = {}

for palavra in palavras:
    if palavra in contagem_de_palavras:
        contagem_de_palavras[palavra] += 1
    else:
        contagem_de_palavras[palavra] = 1

print(contagem_de_palavras)
#%%

### Exercício 7. Normalização de Dados
# Objetivo:** Normalizar uma lista de números para que fiquem na escala de 0 a 1.
numeros = [10,20,30,40,50]
minimo = min(numeros)
maximo = max(numeros)
normalizados = [(x - minimo) / (maximo - minimo) for x in numeros]

print(normalizados)

#%%

### Exercício 8. Filtragem de Dados Faltantes
# Objetivo:** Dada uma lista de dicionários representando dados de usuários, filtrar aqueles que têm um campo específico faltando
usuarios = [
    {"nome": "Alice", "email": "alice@example.com"},
    {"nome": "Bob", "email": ""},
    {"nome": "Carol", "email": "carol@example.com"}
]

usuarios_validos = [usuario for usuario in usuarios if usuario["email"]]
print(usuarios_validos)

#%%

### Exercício 9. Extração de Subconjuntos de Dados
# Objetivo:** Dada uma lista de números, extrair apenas aqueles que são pares.
lista = [454,15541,5487,1548,1114879,4568]
pares = [numero for numero in lista if numero % 2 == 0]

print(pares)


#%%

### Exercício 10. Agregação de Dados por Categoria
# Objetivo:** Dado um conjunto de registros de vendas, calcular o total de vendas por categoria.
vendas = [
    {"categoria": "eletronicos","valor": 1200},
    {"categoria": "livros", "valor": 200},
    {"categoria": "eletronicos", "valor": 800}
]

total_por_categoria = {}
for venda in vendas:
    categoria = venda["categoria"]
    valor = venda["valor"]
    if categoria in total_por_categoria:
        total_por_categoria[categoria] += valor
    else:
        total_por_categoria[categoria] = valor

print(total_por_categoria)

#%%

### Exercícios com WHILE

### Exercício 11. Leitura de Dados até Flag
# Ler dados de entrada até que uma palavra-chave específica ("sair") seja fornecida.

palavra_chave = ''

while palavra_chave != "sair":
    palavra_chave = str(input("Digite algo. Caso queira terminar o programa, digite, 'sair': "))

#%%

### Exercício 12. Validação de Entrada
# Solicitar ao usuário um número dentro de um intervalo específico até que a entrada seja válida.

numero = int(input("Digite um numero entre 1 e 10: "))
while numero < 1 or numero >10:
    print("Número fora do intervalo!")
    numero = int(input("Por favor, digite um numero entre 1 e 10: "))

print("Numero válido")

#%%

### Exercício 13. Consumo de API Simulado
# Simular o consumo de uma API paginada, onde cada "página" de dados é processada em loop até que não haja mais páginas.
pagina_atual = 1
paginas_totais = 5 

while pagina_atual <= paginas_totais:
    print(f"Processando página {pagina_atual} de {paginas_totais}")
    # Aqui iria o código para processar os dados da página
    pagina_atual += 1

print("Todas as páginas foram processadas.")

#%%

### Exercício 14. Tentativas de Conexão
# Simular tentativas de reconexão a um serviço com um limite máximo de tentativas.
tentativas_maximas = 5
tentativa = 1

while tentativa <= tentativas_maximas:
    print(f"Tentativa {tentativa} de {tentativas_maximas}")

    if True:
        print("Conexao bem-sucedida!")
        break
    tentativa += 1
else:
    print("Falha ao conectar após várias tentativas")


#%%

### Exercício 15. Processamento de Dados com Condição de Parada
# Processar itens de uma lista até encontrar um valor específico que indica a parada.

itens = [1,2,3,"parar", 4, 5]

i = 0
while i < len(itens):
    if itens[i] == "parar":
        print("Parada encontrada, encerrando o processamento.")
        # Processa o item
    print(f"Processando: item: {itens[i]}")
    i += 1