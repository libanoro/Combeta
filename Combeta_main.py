def leiaInt(texto):

    carga= input(texto)

    if carga.isdecimal():
        return carga

    else:

        print('Valor inválido. Digite um número inteiro!')

        return leiaInt(texto)

def leiaFloat(texto):
    hora = input(texto)
    while True:
        try:
            tente= float(input(texto))
        except (ValueError, TypeError):
            print('ERRO! Informe um valor de tempo em horas decimais...')
            continue
        else:
            return tente


def leiaInt(texto):

    voo= input(texto)

    if voo.isdecimal():
        return voo

    else:

        print('Valor inválido. Digite um número inteiro!')

        return leiaInt(texto)


def leiaInt(texto):

            menu = input(texto)

            if menu.isdecimal():
                return menu

            else:

                print('Valor inválido. Digite um número inteiro!')

                return leiaInt(texto)

print ('COMBETA VERSÃO 1.0 ',
       'DATA: 06/2021'
       'DESENVOLVIDO POR: TIAGO A L DE OLIVEIRA '
       'E-MAIL: libanoro@gmail.com  ')
loop = 0
choice = 3
while loop == 0:
    menu = leiaInt('''Escolha o Modelo de AERONAVE
    [ 1 ] A320;
    [ 2 ] B737; 
    [ 3 ] SAIR DO PROGRAMA: ''')
    menu=int(menu)

    if menu == 3:
        quit()

    if menu == 2:
        print('O modelo escolhido foi: B737')
        carga = leiaInt('Digite o valor da Carga a bordo , Considerar média de 104 kg por pessoa já com bagagem - Payload em Kg :   ')
        carga= int(carga)
        hora= leiaFloat('Digite o tempo de voo previsto em  horas decimais (Exemplo 1.5 ):  ')
        hora=float(hora)
        voo= leiaInt ('Digite o tempo de voo previsto para aeroporto alternativo em minutos:  ')
        voo= int(voo)

       ###B737###
        air = 2550
        cons = float(hora) * 2550 * (1.1)
        alt = ((voo) / 60) * 2550
        alti = (45 / 60) * 2550
        mzfw = 61700
        boew = 41400
        taxi = 200
        mtow = 79000
        mlw = 65300
        tanque = 20800
        aeronavetotal = ((cons) + (alt) + (alti) + (taxi))
        # Zero fuel weight
        ZFW = ((boew) + (carga))
        # minimal combus
        mfod = ((alt) + (alti))
        # peso de decolagem TOW
        tow = ((cons) + (ZFW) + (mfod))
        # peso planejado pouso
        ppp = ((taxi) + (tow))
        # peso de decolagem taxi
        taxitow = ((cons) + (ZFW) + (mfod) + (taxi))
        auto = (((((hora) * 60) + (voo) + 45 + 5)) / 60)

        input("Pressione Enter para continuar")

        print('Combustível')
        print('A Capacidade Máxima de Combustível é: {} Kg'.format(tanque))
        print('Consumo de combustível da aeronave é: {} Kg/h'.format(air))
        print('Combustível necessário para o voo é: {} Kg'.format(cons))
        print('Combustível necessário para aeroporto alternativo é: {} Kg'.format(alt))
        print('Combustível reserva (equivalente a 45 min de voo) é: {} Kg'.format(alti))
        print('Combustível para taxi (valor médio) é: {} kg'.format(taxi))
        print('Combustível total previsto para o voo é {} Kg'.format((cons) + (alt) + (alti) + (taxi)))
        print('Minimum Fuel Over Destination (MFOD) é: {} Kg'.format((alt) + (alti)))
        print('Zero fuel weight (ZFW) é: {} Kg'.format(ZFW))

        input("Pressione Enter para continuar")
        print('Peso')
        print('Peso máx.operacional da aeronave sem combustível(MZFW) é: {} Kg'.format(mzfw))
        print('Peso máximo operacional para decolagem (MTOW) é: {} Kg'.format(mtow))
        print('Peso máximo operacional para pouso (MLW)é: {} Kg'.format(mlw))
        print('Peso de Decolagem TOW é: {} Kg'.format(tow))
        print('Peso de Decolagem antes de taxiar é: {} Kg'.format(taxitow))
        print('Peso planejado pouso é: {} Kg'.format((ZFW) + (mfod)))


        input("Pressione Enter para continuar")
        print('Autonomia de voo')
        print('Autonomia de voo é: {} H'.format(auto))

        input("Pressione Enter para continuar")
        print('PADRÕES DE VERIFICAÇÃO')
        input("Pressione Enter para continuar")
        if tow <= mtow:
            print('TOW < MTOW = Sim')
        if tow > mtow:
            print('TOW > MTOW = ATENÇÃO!!!')
        if ppp < mlw:
            print('Peso planejado para pouso < Peso máximo operacional para pouso (MLW) = SIM')
        if ppp > mlw:
            print('Peso planejado para pouso > Peso máximo operacional para pouso (MLW), = ATENÇÃO!!!')
        if ZFW < mzfw:
            print('ZFW < MZFW = Sim')
        if ZFW > mzfw:
            print('ZFW > MZFW = ATENÇÃO!!!')

        input("Pressione Enter para sair")
        break




    if menu == 1:
        print('O modelo escolhido foi: A320')
        carga = leiaInt('Digite o valor da Carga a bordo, Considerar média de 104 kg por pessoa já com bagagem - Payload em Kg :   ' )
        carga=int(carga)
        hora  = leiaFloat('Digite o tempo de voo previsto em  horas decimais (Exemplo 1.5 ):  ')
        hora = float(hora)
        voo= leiaInt ('Digite o tempo de voo previsto para aeroporto alternativo em minutos:  ')
        voo =int(voo)


        ###A320###
        air = 2700
        cons = float (hora) * 2700 * (1.1)
        alt = ((voo) / 60) * 2700
        alti = (45 / 60) * 2700
        mzfw = 62500
        boew = 42400
        taxi = 200
        mtow = 77000
        mlw = 66000
        tanque = 24325
        aeronavetotal = ((cons) + (alt) + (alti) + (taxi))
        # Zero fuel weight
        ZFW = ((boew) + (carga))
        # minimal combus
        mfod = ((alt) + (alti))
        # peso de decolagem TOW
        tow = ((cons) + (ZFW) + (mfod))
        # peso planejado pouso
        ppp = ((taxi) + (tow))
        # peso de decolagem taxi
        taxitow = ((cons) + (ZFW) + (mfod) + (taxi))
        auto = (((((hora)*60) + (voo)+45+5))/60)



        input("Pressione Enter para continuar")

        print('Combustível')
        print('A Capacidade Máxima de Combustível é: {} Kg'.format (tanque))
        print('Consumo de combustível da aeronave é: {} Kg/h'.format(air))
        print('Combustível necessário para o voo é: {} Kg'.format(cons))
        print('Combustível necessário para aeroporto alternativo é: {} Kg'.format(alt))
        print('Combustível reserva (equivalente a 45 min de voo) é: {} Kg'.format(alti))
        print('Combustível para taxi (valor médio) é: {} kg'.format(taxi))
        print('Combustível total previsto para o voo é {} Kg'.format((cons) + (alt) + (alti) + (taxi)))
        print('Minimum Fuel Over Destination (MFOD) é: {} Kg'.format((alt) + (alti)))
        print('Zero fuel weight (ZFW) é: {} Kg'.format(ZFW))

        input("Pressione Enter para continuar")
        print('Peso')
        print('Peso máx.operacional da aeronave sem combustível(MZFW) é: {} Kg'.format(mzfw))
        print('Peso máximo operacional para decolagem (MTOW) é: {} Kg'.format(mtow))
        print('Peso máximo operacional para pouso (MLW)é: {} Kg'.format(mlw))
        print('Peso de Decolagem TOW é: {} Kg'.format(tow))
        print('Peso de Decolagem antes de taxiar é: {} Kg'.format(taxitow))
        print('Peso planejado pouso é: {} Kg'.format((ZFW) + (mfod)))


        input("Pressione Enter para continuar")
        print('Autonomia de voo')
        print('Autonomia de voo é: {} H'.format(auto))

        input("Pressione Enter para continuar")
        print('PADRÕES DE VERIFICAÇÃO')
        input("Pressione Enter para continuar")
        if tow <= mtow:
            print('TOW < MTOW = Sim')
        if tow > mtow:
            print('TOW > MTOW = ATENÇÃO!!!')
        if ppp < mlw:
            print('Peso planejado para pouso < Peso máximo operacional para pouso (MLW) = SIM')
        if ppp > mlw:
            print('Peso planejado para pouso > Peso máximo operacional para pouso (MLW), = ATENÇÃO!!!')
        if ZFW < mzfw:
            print('ZFW < MZFW = Sim')
        if ZFW > mzfw:
            print('ZFW > MZFW = ATENÇÃO!!!')

        input("Pressione Enter para sair")
        break
