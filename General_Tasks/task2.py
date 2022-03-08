# initializing variables
speed, position, track_length = 0, 0, 150

# track position and speed
while position < track_length:
    
    move = (input("Enter next move: ")).lower()
    position += speed
    
    # check input
    if move == "w":
        speed += 10
    elif move == "s":
        speed -= 10
    else:
        speed += 0
    
    # print check
    print(f"Position: {position}", end=" __ ")
    print(f"Speed: {speed}")


# print results
if position == 150 and speed == 0:
    print("\033[92m CONGRATULATIONS"*5)
else:
    print("\033[91m GAME OVER"*5)


# to win, choose these moves >> w, w, s, w, w, s, s, w, s, s // and to lose, choose on your own