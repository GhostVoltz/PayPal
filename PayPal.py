import time
from tqdm import tqdm
from colorama import Fore, Style, init
import locale

# Inicialize o colorama
init(autoreset=True)

# Configurar a localiza    o para formatar o saldo corretamente
locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

# Saldo inicial
saldo = 1000000.00  # R$1.000.000,00

while True:
    # Exibe o saldo atual em verde com a formata    o desejada
    saldo_formatado = locale.currency(saldo, grouping=True)
    print(f"""{Fore.BLUE}
                               _
 _ __   __ _ _   _ _ __   __ _| |
| '_ \ / _` | | | | '_ \ / _` | |
| |_) | (_| | |_| | |_) | (_| | |
| .__/ \__,_|\__, | .__/ \__,_|_|
|_|          |___/|_|

    """)
    print(f"Saldo atual: {Fore.GREEN}{saldo_formatado}{Style.RESET_ALL}")

    # Captura o valor inserido pelo usu  rio
    valor = float(input("Digite o valor a ser enviado (0 para sair): R$"))

    # Se o valor for 0, saia do loop
    if valor == 0:
        break

    # Captura o nome (Nick)
    nick = input("Digite o nome (Nick): ")

    # Verifica se o saldo    suficiente para enviar o valor
    if valor <= saldo:
        # Simula o processamento com uma barra de carregamento
        print("Processando...")
        for _ in tqdm(range(10), desc="Enviando", ncols=75):
            time.sleep(0.1)
        print("Enviado")

        # Deduz o valor do saldo
        saldo -= valor

        # Formata a mensagem
        mensagem = f"{Style.RESET_ALL}\nValor: {Fore.GREEN}{locale.currency(valor, grouping=True)}{Style.RESET_ALL}\nNome: {nick}"

        # Imprime a mensagem
        print(mensagem)
    else:
        print("Saldo insuficiente para enviar o valor desejado.")

print("Sess  o encerrada.")
