import sys


def leia_numero(prompt, tipo=int):
    """Lê um número (int ou float) com validação de erro."""
    while True:
        try:
            valor = input(prompt).strip().replace(',', '.')
            return tipo(valor)
        except ValueError:
            print(f"ERRO! Digite um valor {tipo.__name__} válido.")


def mostrar_cabecalho():
    print("-" * 50)
    print("COMBETA VERSÃO 2.0".center(50))
    print("DESENVOLVIDO POR: TIAGO A L DE OLIVEIRA".center(50))
    print("-" * 50)


def realizar_calculos(nome, dados, carga, horas_voo, min_alternativo):
    # Constantes e Cálculos de Combustível
    consumo_hora = dados['consumo']
    comb_trecho = horas_voo * consumo_hora * 1.1  # 10% de margem
    comb_alternativo = (min_alternativo / 60) * consumo_hora
    comb_reserva = (45 / 60) * consumo_hora
    taxi = 200

    comb_total = comb_trecho + comb_alternativo + comb_reserva + taxi
    mfod = comb_alternativo + comb_reserva

    # Cálculos de Peso
    zfw = dados['boew'] + carga
    tow = comb_trecho + zfw + mfod
    ppp = zfw + mfod  # Peso planejado de pouso
    taxitow = tow + taxi
    autonomia = (horas_voo * 60 + min_alternativo + 45 + 5) / 60

    # Exibição de Resultados
    print(f"\n=== RELATÓRIO DE VOO: {nome} ===")
    print(f"Combustível Total Previsto: {comb_total:.2f} Kg")
    print(f"ZFW (Peso sem Combustível): {zfw:.2f} Kg")
    print(f"TOW (Peso de Decolagem): {tow:.2f} Kg")
    print(f"Autonomia estimada: {autonomia:.2f} Horas")

    print("\n--- PADRÕES DE VERIFICAÇÃO ---")
    print(f"TOW < MTOW ({dados['mtow']}): {'✅ SIM' if tow <= dados['mtow'] else '❌ ATENÇÃO!!!'}")
    print(f"PPP < MLW ({dados['mlw']}): {'✅ SIM' if ppp <= dados['mlw'] else '❌ ATENÇÃO!!!'}")
    print(f"ZFW < MZFW ({dados['mzfw']}): {'✅ SIM' if zfw <= dados['mzfw'] else '❌ ATENÇÃO!!!'}")
    print("-" * 30)
    input("\nPressione Enter para voltar ao menu...")


# Banco de dados das aeronaves
AERONAVES = {
    1: {
        "nome": "A320",
        "consumo": 2700, "mzfw": 62500, "boew": 42400,
        "mtow": 77000, "mlw": 66000, "tanque": 24325
    },
    2: {
        "nome": "B737",
        "consumo": 2550, "mzfw": 61700, "boew": 41400,
        "mtow": 79000, "mlw": 65300, "tanque": 20800
    }
}

# Loop Principal
while True:
    mostrar_cabecalho()
    print("Escolha o Modelo de AERONAVE:")
    print("[ 1 ] Airbus A320")
    print("[ 2 ] Boeing B737")
    print("[ 3 ] SAIR DO PROGRAMA")

    opcao = leia_numero("Sua opção: ")

    if opcao == 3:
        print("Encerrando programa...")
        break

    if opcao in AERONAVES:
        aviao = AERONAVES[opcao]
        print(f"\nModelo escolhido: {aviao['nome']}")

        # Coleta de dados
        payload = leia_numero("Carga a bordo (Payload em Kg): ")
        tempo = leia_numero("Tempo de voo previsto (horas decimais, ex: 1.5): ", float)
        min_alt = leia_numero("Tempo para aeroporto alternativo (minutos): ")

        realizar_calculos(aviao['nome'], aviao, payload, tempo, min_alt)
    else:
        print("Opção inválida! Tente novamente.")