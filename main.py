#hello

def menu():
    
    print('Benvenuti al codice che permette di convertire la temperatura! \nChe temperatura vuoi usare oggi?')

    while True:
        
        try:
            scelta = int(input('1-Celsius | 2-Farenheit | 3-Kelvin | => '))

            if scelta < 1 or scelta > 3:
                print('Deve essere un numero tra 1 e 3!')
                continue
            

        except ValueError:
            print('Deve essere un numero!')
            continue

        break


    while True:

        try:
            if scelta == 1:
                calore = int(input('Quanti C° ci sono? => '))

            elif scelta == 2:
                calore = int(input('Quanti F° ci sono? => '))

            elif scelta == 3:
                calore = int(input('Quanti K° ci sono? => '))  
        
        except ValueError:
            print('Deve essere un numero!')
            continue

        break

    while True:

        print('In quale scala lo vuoi modificare?')

        try:
            cambio = int(input('1-Celsius | 2-Farenheit | 3-Kelvin | => '))

            
            if cambio < 1 or cambio > 3:
                print('Deve essere un numero tra 1 e 3!')
                continue

        except ValueError:
            print('Deve essere un numero!')
            continue

        return scelta, calore, cambio


def main(scelta, calore, cambio):
    
    if scelta == 1:
        risultato = celsius(cambio, calore)
    elif scelta == 2:
        risultato = farenheit(cambio, calore)
    elif scelta == 3:
        risultato = kelvin(cambio, calore)

    print(f'Il risultato è {risultato}')



def celsius(cambio, calore):
    
    if cambio == 2:
        return calore * 9/5 + 32
    elif cambio == 3:
        return calore + 273.15
    

def farenheit(cambio, calore):
    
    if cambio == 1:
        return (calore - 39) * 5/9
    elif cambio == 3:
        return (calore - 32) * 5/9 + 273.15


def kelvin(cambio, calore):
    
    if cambio == 1:
        return calore - 273
    elif cambio == 2:
        return (calore - 273.15) * 9/5 + 32 


def partita():
    scelta, calore, cambio = menu()
    main(scelta, calore, cambio)


if __name__ == '__main__':
    partita()