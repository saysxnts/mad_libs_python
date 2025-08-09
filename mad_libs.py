# mad_libs.py

# --- Passo 1: Mensagem de boas-vindas ---
print("--- Bem-vindo ao Gerador de Histórias Mad Libs! ---")
print("Por favor, forneça as palavras pedidas abaixo.")
print("-" * 50) # Imprime uma linha para separar

# --- Passo 2: Pedir as palavras ao usuário ---
# Usamos a função input() para pegar o que o usuário digita no terminal.
# Cada palavra digitada é guardada em uma variável.

nome_pessoa = input("Um nome de pessoa: ")
adjetivo = input("Um adjetivo (ex: grande, engraçado): ")
substantivo_plural = input("Um substantivo no plural (ex: cachorros): ")
verbo_terminado_em_ing = input("Um verbo terminado em 'ando' ou 'endo' (ex: correndo): ")
parte_do_corpo = input("Uma parte do corpo: ")
verbo_no_passado = input("Um verbo no passado (ex: comeu): ")
lugar = input("O nome de um lugar: ")
animal = input("O nome de um animal: ")
liquido = input("O nome de um líquido: ")

# --- Passo 3: Montar a história usando as palavras fornecidas ---
# Usamos uma f-string (a letra 'f' antes das aspas) para inserir facilmente
# nossas variáveis dentro do texto. Os nomes das variáveis ficam entre chaves {}.
historia = f"""
Era uma vez, uma pessoa chamada {nome_pessoa}. Ele/ela era extremamente {adjetivo}
e adorava passar o tempo {verbo_terminado_em_ing} com seus {substantivo_plural}.

Um dia, {nome_pessoa} acordou sentindo uma dor estranha em seu/sua {parte_do_corpo}.
Foi então que ele/ela percebeu que um(a) {animal} selvagem tinha entrado em seu quarto!
O(A) {animal} {verbo_no_passado} todo o(a) {liquido} que estava sobre a mesa.

Chocado(a), {nome_pessoa} gritou e correu para fora de casa, indo parar em {lugar}.
Moral da história: nunca deixe um(a) {animal} sozinho(a) com seu/sua {liquido}!
"""

# --- Passo 4: Exibir a história final para o usuário ---
print("\n" + "-" * 50) # \n cria uma linha em branco
print("--- Sua história maluca está pronta! ---")
print("-" * 50)
print(historia)