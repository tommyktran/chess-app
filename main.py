import requests
import chess
import json
from tabulate import tabulate

menu_options = {
    1: 'Opening Explorer',
    2: 'Player Opening Tree',
    3: 'Exit',
}

def print_menu():
    print('\n\n')
    for key in menu_options.keys():
        print (key, '--', menu_options[key] )

def opening_explorer():
    moves = input('Please enter a valid sequence of chess moves from the starting position, in UCI notation.\nOr a default value: e2e4')
    response = requests.get("https://explorer.lichess.ovh/masters?play=" + "e2e4")
    if (response.status_code != 200):
        print("There was something wrong with the API request. Did you enter a correct series of moves in UCI notation?")
        return
    else: 
        responseObj = json.loads(response.content)
        print(responseObj)
        moveTable = []
        for move in responseObj['moves']:
            totalGames = move['white'] + move['black'] + move['draws']
            moveTable.append([totalGames, move['uci'], '{percent:.2%}'.format(percent=move['white']/totalGames), '{percent:.2%}'.format(percent=move['draws']/totalGames), '{percent:.2%}'.format(percent=move['black']/totalGames),])
        print(tabulate(moveTable, headers=["Total Games", "Move", "White Win %", "Draw %", "Black Win %"]))
        return

def main():
    while(True):
        print_menu()
        option = input('Enter your choice: ') 
        if option == '1':
            print('Handle option \'Option 1\'')
            opening_explorer()
        elif option == '2':
            print('Handle option \'Option 2\'')
        elif option == '3':
            print('Exiting')
            exit()
        else:
            print('Invalid option. Please enter a number between 1 and 3.')
    return

main()