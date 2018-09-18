# from function.game import show_info as game_show_info, play_game
import function
from function.shop import show_info as shop_show_info, buy_item
import friends

def turn_on():
    print('= Turn on game =')

    while True:
        choice = input(
        'What would you like to do?\n'
        '1: Go to Shop\n'
        '2: Play Game\n'
        '3: chat\n'
        '0: Exit\n'
        'Input : '
        )
        if choice == '0':
            break
        elif choice == '1':
            shop_show_info()
            buy_item()
        elif choice == '2':
            function.game.show_info()
            function.game.play_game()
        elif choice == '3':
            friends.send_message.send_message()
        else:
            print('Choice not exist')
        print('--------------------')

    print('= Turn off game =')

if __name__ == '__main__':
    turn_on()
