#Class: CSE210 
#Assignment: Week 2 Tic Tac Toe 
#Author: Teigen Barber

arr =[1,2,3,4,5,6,7,8,9]
player = 1

def win(player):
    if player == 1:
        print("Player 1 Wins!")
    elif player == 0:
        print("Player 2 Wins!")
    elif player ==2:
        print("Draw Game. Try Again.")
    print("Good Game! Thanks for playing!")
    arr=[1,2,3,4,5,6,7,8,9]
    player = 1
    board(player,arr)
    

def check(player, arr):
    draw = 0
    for x in arr:
        if x == "X" or x == "O":
            draw += 1
    if draw == 9:
        win(2)

    if "O" in arr or "X" in arr:
        if arr[0]==arr[1] and arr[1]==arr[2]:
            win(player)
        elif arr[3]==arr[4] and arr[4]==arr[5]:
            win(player)
        elif arr[6]==arr[7]and arr[7]==arr[8]:
            win (player)
        elif arr[0]==arr[3] and arr[3]==arr[6]:
            win (player)
        elif arr[1]==arr[4] and arr[4]==arr[7]:
            win (player)
        elif arr[2]==arr[5] and arr[5]==arr[8]:
            win (player)
        elif arr[0]==arr[4] and arr[4]==arr[8]:
            win (player)
        elif arr[2]==arr[4] and arr[4]==arr[6]:
            win (player)






def turn(player, arr):
    if player == 1:
        sel = int(input("Player 1, make your choice: "))
        for x in arr:
            if sel == x:
                arr[sel-1] = "X"
                break
    elif player == 0:
        sel = int(input("Player 2, make your choice: "))
        for x in arr:
            if sel == x:
                arr[sel-1] = "O"
                break
    check(player, arr)
    if player == 1: player = 0
    else: player = 1
    return player
        



def board(player, arr):
     while True:
        print(arr[0], "|", arr[1],"|", arr[2])
        print("_______")
        print(arr[3], "|", arr[4], "|", arr[5])
        print("_______")
        print(arr[6], "|", arr[7], "|", arr[8])
        
        player = turn(player, arr)
    
       

def main():
    player = 1
    arr = [1,2,3,4,5,6,7,8,9]
    board(player, arr)


if __name__ == "__main__":
    main()