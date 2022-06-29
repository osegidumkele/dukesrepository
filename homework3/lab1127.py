#Dumkele Osegi, PSID 1894081
player_Info = {}
playerjersey_list = []


for p in range(5):
    print(f"Enter player {str(p+1)}'s jersey number:")
    player_jersey = int(input())
    print(f"Enter player {(p+1)}'s rating:\n")
    player_rating = int(input())
    player_Info[player_jersey] = player_rating
    playerjersey_list.append(player_jersey)
playerjersey_list.sort()

print('ROSTER')
for i in range(len(playerjersey_list)):
    print(f'Jersey number: {playerjersey_list[i]}, Rating: {player_Info[playerjersey_list[i]]}')


def menu():
    print()
    print('MENU')
    print('a - Add player')
    print('d - Remove player')
    print('u - Update player rating')
    print('r - Output players above a rating')
    print('o - Output roster')
    print('q - Quit')
    print()
    print('Choose an option:')



    input1 = input()
    if input1 == 'a':
        print(f"Enter a new player's jersey number")
        newplayerumber = int(input())
        print(f"Enter the player's rating")
        newplayerrating = input()

        player_Info[newplayerumber] = newplayerrating
        playerjersey_list.append(newplayerumber)
        playerjersey_list.sort()
        menu()

    if input1 == 'd':
        print(f"Enter a jersey number:")
        newjersey = input()
        if newjersey in playerjersey_list:
            del player_Info[newjersey]
            playerjersey_list.remove(newjersey)
        menu()

    if input1 == 'u':
        print(f"Enter a jersey number:")
        updatejersey = input()
        print(f"enter a new rating for player:")
        updaterating = input()
        player_Info.update({updatejersey:updaterating})
        menu()

    if input1 == 'r':
        print(f"Enter a rating:")
        aboverating = int(input())
        print()
        print('ABOVE',aboverating)
        for i in playerjersey_list:
            if int(i) > int(aboverating):
                print('Jersey number:', playerjersey_list[i], 'Rating:', player_Info[playerjersey_list[i]])
        menu()

    if input1 == 'o':
        print('ROSTER')
        for i in range(len(playerjersey_list)):
            print(f'Jersey number: {playerjersey_list[i]}, Rating: {player_Info[playerjersey_list[i]]}')
        menu()

    if input1 == 'q':
        quit()

if __name__ == '__main__':
    menu()

