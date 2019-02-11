import os
import time
os.system('cls')

class Board:
    def __init__(self):
        self.cells = [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "]

    def display(self):
        print("%s | %s | %s" % (self.cells[1], self.cells[2], self.cells[3]))
        print("---------")
        print("%s | %s | %s" % (self.cells[4], self.cells[5], self.cells[6]))
        print("---------")
        print("%s | %s | %s" % (self.cells[7], self.cells[8], self.cells[9]))

    def update_cell(self, cell_no, player):
        #Check if the space is empty
        if self.cells[cell_no]==" ":
            self.cells[cell_no] = player
        else:
            print("Sorry this space is already filled.")
            time.sleep(2)

    def reset_cells(self):
        self.cells = [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "]

    def isTie(self):

        for i in range(1,10):
            cells_used = 0
            for cells in self.cells:
                if cells != " ":
                    cells_used += 1
            if cells_used == 9:
                return True
            else:
                return False


    def winner(self):

        if(self.cells[1]=="X" and self.cells[2]=="X" and self.cells[3]=="X" or
        self.cells[4]=="X" and self.cells[5]=="X" and self.cells[6]=="X" or
        self.cells[7]=="X" and self.cells[8]=="X" and self.cells[9]=="X" or
        self.cells[1]=="X" and self.cells[4]=="X" and self.cells[7]=="X" or
        self.cells[3]=="X" and self.cells[6]=="X" and self.cells[9]=="X" or
        self.cells[1]=="X" and self.cells[5]=="X" and self.cells[9]=="X" or
        self.cells[3]=="X" and self.cells[5]=="X" and self.cells[7]=="X" or
        self.cells[2]=="X" and self.cells[5]=="X" and self.cells[8]=="X"):
            return "X"

        elif(self.cells[1]=="X" and self.cells[2]=="X" and self.cells[3]=="X" or
        self.cells[4]=="O" and self.cells[5]=="O" and self.cells[6]=="O" or
        self.cells[7]=="O" and self.cells[8]=="O" and self.cells[9]=="O" or
        self.cells[1]=="O" and self.cells[4]=="O" and self.cells[7]=="O" or
        self.cells[3]=="O" and self.cells[6]=="O" and self.cells[9]=="O" or
        self.cells[1]=="O" and self.cells[5]=="O" and self.cells[9]=="O" or
        self.cells[3]=="O" and self.cells[5]=="O" and self.cells[7]=="O" or
        self.cells[2]=="O" and self.cells[5]=="O" and self.cells[8]=="O"):
            return "O"
        else:
            pass

bb = Board()


def print_header():
    print("Welcome to Tic-Tac-Toe\n")


def refresh_screen():
    # Clear the screen
    os.system('cls')
    # Print the header
    print_header()
    # Display the board
    bb.display()


while True:
    refresh_screen()

    # Get X input
    x_choice = int(input("\n X Player : Choose 1-9. >>"))
    # Update board
    bb.update_cell(x_choice,"X")
    # Updated board
    refresh_screen()

    #Check for tie
    if bb.isTie():
        print("Here is a tie.")

        # for playing again
        again = input("Do you want to play again? (Y/N)").upper()
        if again == "Y":
            bb.reset_cells()
            continue
        else:
            break

    # Check if X is winner
    if bb.winner()=="X":
        refresh_screen()
        print("X is winner")

        #for playing again
        again = input("Do you want to play again? (Y/N)").upper()
        if again == "Y":
            bb.reset_cells()
            continue
        else:
            break


    #Get O input
    o_choice = int(input("\n O Player : Choose 1-9. >>"))
    #Update board
    bb.update_cell(o_choice,"O")
    #Updated Board
    refresh_screen()
    #Check if O is winner
    if bb.winner()=="O":
        refresh_screen()
        print("O is winner")

        #for playing again
        again = input("Do you want to play again? (y/n)").upper()
        if again == "Y":
            bb.reset_cells()
            continue
        else:
            break

    #Check for tie
    if bb.isTie():
        print("Here is a tie.")
        # for playing again
        again = input("Do you want to play again? (Y/N)").upper()
        if again == "Y":
            bb.reset_cells()
            continue
        else:
            break