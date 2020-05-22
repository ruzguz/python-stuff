class Lamp:
    _LAMPS = ['''
          .
     .    |    ,
      \   '   /
       ` ,-. '
    --- (   ) ---
         \ /
        _|=|_
       |_____|
    ''',
    '''
         ,-.
        (   )
         \ /
        _|=|_
       |_____|
    ''']

    def __init__(self, is_turned_on):
        self._is_turned_on = is_turned_on

    def turn_on(self):
        self._is_turned_on = True
        self._display_image()

    def turn_off(self):
        self._is_turned_on = False
        self._display_image()

    def _display_image(self):
        if self._is_turned_on is True:
            print(self._LAMPS[0])
        else:
            print(self._LAMPS[1])

def print_menu():
    print('[1] - Turn on the lamp')
    print('[2] - Turn off the lamp')
    print('[Whatever] - exit')

if __name__ == '__main__':
    while True:
        print_menu()  
        
        lamp = Lamp(False)

        option = input('Select an option: ')

        if option == '1':
            lamp.turn_on()
        elif option == '2':
            lamp.turn_off()
        else:
            break