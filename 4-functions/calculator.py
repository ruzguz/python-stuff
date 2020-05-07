def foreing_exchange_calculator(ammount):
    usd_to_eu = 0.92

    return ammount * usd_to_eu

def run():
    print('Calculadora de divisas')
    print('Convierte dolares a euros.')
    print('')

    ammount = float(input('Ingresa la cantidad de dolares que quieres convertir '))

    result = foreing_exchange_calculator(ammount)

    print('${} euros'.format(result))
    print('')

if __name__ == '__main__':
    run()
