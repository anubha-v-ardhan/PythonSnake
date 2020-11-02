import curses
from random import randint

curses.initscr()                    
win = curses.newwin(20, 60, 0, 0)   
win.keypad(1)                       
curses.noecho()                     
curses.curs_set(0)                  
win.border(0)                      
win.nodelay(1) # -1                  

snake = [(4, 10), (4, 9), (4, 8)]   
food = (10, 20)                     

win.addch(food[0], food[1], '#')   

score = 0                           
    
ESC = 27                            
key = curses.KEY_RIGHT              
win.addch(food[0], food[1], 'O')    
while key != ESC:                   
    win.addstr(0, 2, 'Score ' + str(score) + ' ')
    win.timeout(100)               

    prev_key = key                  
    event = win.getch()
    key = event if event != -1 else prev_key    

    if key not in [curses.KEY_LEFT, curses.KEY_RIGHT, curses.KEY_UP, curses.KEY_DOWN, ESC]:
        key = prev_key                          

    y = snake[0][0]
    x = snake[0][1]
    if key == curses.KEY_DOWN:
        y += 1
    if key == curses.KEY_UP:
        y -= 1
    if key == curses.KEY_LEFT:
        x -= 1
    if key == curses.KEY_RIGHT:
        x += 1

    snake.insert(0, (y, x))                     

    if y == 0: break
    if y == 19: break
    if x == 0: break
    if x == 59: break

    if snake[0] in snake[1:]: break

    if snake[0] == food:
        # eat the food
        score += 1
        food = ()
        if food == ():
            food = (randint(1,18), randint(1,58))
            if food in snake:
                food = ()
        win.addch(food[0], food[1], '#')
    else:
        last = snake.pop()
        win.addch(last[0], last[1], ' ')
    
    win.addch(snake[0][0], snake[0][1], '*')

# end curses window on end of game loop
curses.endwin()
print(f"Final score = {score}")     # print final score

# file handling with txt
outfile = open("Scores.txt",'w')    # open Scores.txt
outfile.write(str(score))           # store the final score in Scores.txt
outfile.close() 
