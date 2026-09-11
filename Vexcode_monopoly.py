screen_precision = 0
console_precision = 0
FWD = Event()
LT = Event()
RT = Event()
myVariable = 0
dice1 = 0
dice2 = 0
spaces_to_move = 0
current_space_number = 0

def play_game():
    global FWD, LT, RT, my_event, myVariable, dice1, dice2, spaces_to_move, current_space_number, screen_precision, console_precision
    while True:
        roll_dice()
        move()
        complete_task()
        wait(5, MSEC)

def roll_dice():
    global FWD, LT, RT, my_event, myVariable, dice1, dice2, spaces_to_move, current_space_number, screen_precision, console_precision
    dice1 = int(round(urandom.uniform(1, 4), 2))
    brain.screen.print(str("rolled a:") + str(dice1))
    brain.screen.next_row()
    dice1 = int(round(urandom.uniform(1, 4), 2))
    brain.screen.print(str("Rolled a:") + str(dice2))
    brain.screen.next_row()
    spaces_to_move = dice1 + dice2

def complete_task():
    global FWD, LT, RT, my_event, myVariable, dice1, dice2, spaces_to_move, current_space_number, screen_precision, console_precision
    pass

def move():
    global FWD, LT, RT, my_event, myVariable, dice1, dice2, spaces_to_move, current_space_number, screen_precision, console_precision
    brain.screen.print(str("Moving ") + str(str(spaces_to_move) + str("spaces!")))
    for repeat_count in range(int(current_space_number)):
        wait(5, MSEC)

def when_started1():
    global FWD, LT, RT, my_event, myVariable, dice1, dice2, spaces_to_move, current_space_number, screen_precision, console_precision
    current_space_number = 1
    play_game()

def FWD_callback_0():
    global FWD, LT, RT, my_event, myVariable, dice1, dice2, spaces_to_move, current_space_number, screen_precision, console_precision
    pass

def FWD_callback_1():
    global FWD, LT, RT, my_event, myVariable, dice1, dice2, spaces_to_move, current_space_number, screen_precision, console_precision
    pass

def when_started2():
    global FWD, LT, RT, my_event, myVariable, dice1, dice2, spaces_to_move, current_space_number, screen_precision, console_precision
    pass

def RT_callback_0():
    global FWD, LT, RT, my_event, myVariable, dice1, dice2, spaces_to_move, current_space_number, screen_precision, console_precision
    pass

def RT_callback_1():
    global FWD, LT, RT, my_event, myVariable, dice1, dice2, spaces_to_move, current_space_number, screen_precision, console_precision
    pass

def LT_callback_0():
    global FWD, LT, RT, my_event, myVariable, dice1, dice2, spaces_to_move, current_space_number, screen_precision, console_precision
    pass

def LT_callback_1():
    global FWD, LT, RT, my_event, myVariable, dice1, dice2, spaces_to_move, current_space_number, screen_precision, console_precision
    pass

# system event handlers
FWD(FWD_callback_0)
FWD(FWD_callback_1)
RT(RT_callback_0)
RT(RT_callback_1)
LT(LT_callback_0)
LT(LT_callback_1)
# add 15ms delay to make sure events are registered correctly.
wait(15, MSEC)

ws2 = Thread( when_started2 )
when_started1()