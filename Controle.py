radio_status = False
volume = 5
musica = 0
lista_musica = ['Engenheiros do Hawai', 'Legião Urbana', 'Jota Quest', 'The Strokes', 'jack_johnson.mp3']
while True:
    if radio_status == False:
        f = input('Rádio Desligado: ')
        if f == 'l':  # liga/desliga
            if radio_status == False:
                radio_status = True
                print('Rádio ligado')
    else:
        while True:
            f = input('Funções: ')
            if f == 'l':  # liga/desliga
                if radio_status == True:
                    radio_status = False
                    print('Rádio desligado2')
                    break
                else:
                    radio_status = False
                    print(radio_status)

            elif f == '+':  # aumenta volume
                if volume < 10:
                    volume += 1
                    print('Volume está em {}'.format(volume))
                else:
                    print('Volume máximo!')
            elif f == '-':
                if volume > 0:
                    volume -= 1
                    print('Volume está em {}'.format(volume))
                else:
                    print('Volume mínimo!')
            elif f == '<':
                if musica > 0:
                    musica -= 1
                    print('Música: {}'.format(musica + 1))
                    print(lista_musica[musica])
                else:
                    total_lista = len(lista_musica)
                    musica = total_lista - 1
                    print('Música: {}'.format(musica + 1))
                    print(lista_musica[musica])
            elif f == '>':
                total_lista = len(lista_musica)
                if musica < (total_lista - 1):
                    musica += 1
                    print('Música: {}'.format(musica + 1))
                    print(lista_musica[musica])
                    input()
                else:
                    musica = 0
                    print('Música: {}'.format(musica + 1))
                    print(lista_musica[musica])
