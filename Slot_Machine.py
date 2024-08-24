import random
MAX_LINES = 3
MAX_BET = 110
MIN_BET = 1

ROWS = 3
COLS = 3

symbol_count = {
    "A" : 3,
    "B" : 4,
    "C" : 5,
    "D" : 6
}
symbol_value  = {
    "A": 8,
    "B": 4,
    "C": 2,
    "D": 1
}
def check_winnings(columns,lines,bet,values):
    winnings = 0
    winning_line = []
    for line in range(lines):
        symbol = columns[0][line]

        for column in columns:
            symbol_to_check = column[line]
            if symbol_to_check!=symbol:
                break
        else:
            winnings += values[symbol] * bet
            winning_line.append(line+1)
    
    return winnings,winning_line

def get_slot_machine_spin(rows,cols,symbols):
    all_symbols = [] # Contains all possible symbols available

    for symbol,symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)
    
    columns = []

    for _ in range(cols): # Each column can have any symbol from all_symbols
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)
        
        columns.append(column)

    return columns

def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i,column in enumerate(columns):
            if i != len(column) - 1:
                print(column[row]," |",end=" ")
            else:
                print(column[row])
        

def deposit():
    while True:
        amount = input("How much money would you like to deposit? $")

        if amount.isdigit():
            amount = int(amount)
        
            if amount > 0:
                break
            else:
                print("Amount must be greater than 0")
        else:
            print("Please enter a valid number")
    
    return amount

def get_number_of_lines():
    while True:
        lines = input("Enter the number of lines to bet on (1-"+str(MAX_LINES)+")? ")

        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Enter a valid number of lines")
        else:
            print("Please enter a valid number")
    
    return lines

def get_bet():
    while True:
        amount = input("How much money would you like to bet on each line? $")

        if amount.isdigit():
            amount = int(amount)
        
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"Bet amount must be in between ${MIN_BET} - ${MAX_BET}")
        else:
            print("Please enter a valid number")
        
    return amount

def spin(balance):
    lines = get_number_of_lines()
    bet = 0
    
    while True:
        bet = get_bet()
        total_bet = bet*lines
        if total_bet <= balance:
            break
        else:
            print("You have insufficient balance. Please decrease the bet amount")

    print(f"You are betting ${bet} on {lines} lines. Total bet amount is ${bet*lines}")

    slots = get_slot_machine_spin(ROWS,COLS,symbol_count)

    print_slot_machine(slots)
    
    winnings,winning_lines = check_winnings(slots,lines,bet,symbol_value)

    print(f"You won ${winnings}")
    print("You won on lines:",*winning_lines)

    return winnings - total_bet

def main():
    balance = deposit()
    
    while True:
        print(f"Current balance is ${balance}")

        play = input("Press Enter to play (q to quit)")

        if play == "q":
            break
        
        balance += spin(balance)

        if balance <=0:
            break

    print(f"You left with balance {balance}")
    
main()



        