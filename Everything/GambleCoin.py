__author__ = 'jackoliver'
__version__ = "1.0.2"

from tkinter import *
import random
import sys
import os

root = Tk()
root.title("Gamble Coin 2017")
root.geometry("700x360")


class TkinterWhole(object):
    def __init__(self, root):
        # defining frame, vairable

        self.awesomeFrame = Frame(root)
        self.awesomeFrame.pack()

        self.radVal = IntVar()
        self.varLog = "## LOG OUTPUT ##\n"

        self.gambleAmount = 0
        self.coinFlip = 0
        self.numChecker = 0
        self.totalCoins = 100
        self.firstItemHave = 0
        self.firstItemRand = 0

    def quit_program(self):
        root.destroy()

    def restart_program(self):
        python = sys.executable
        os.execl(python, python, * sys.argv)

    def newWindow(self):

        self.window = Toplevel(root)
        self.window.title("GAME OVER")
        self.window.geometry("200x50")

        self.closeButton = Button(
            self.window, text="Restart", command=self.restart_program)
        self.closeButton.pack()

        self.quitButton = Button(
            self.window, text="Quit", command=self.quit_program)
        self.quitButton.pack()

    def purchaseFirst(self):
        if self.firstItemHave == 0:
            if self.totalCoins > 120:
                self.firstItemHave = 1
                print("The user successfully bought the upgrade!")
                self.totalCoins -= 120
                self.firstItemLabel.config(fg="green")
                self.firstItemLabel.config(
                    text="PURCHASED - 50% chance to gain 25% of amount gambled when you lose.")
                self.coinAmountLabel.config(
                    text=("total: $" + str(self.totalCoins)))
                self.scalePicker.config(from_=0.0, to=self.totalCoins)
            elif self.totalCoins < 120:
                self.firstItemHave = 0
                print("The user is not able to afford this item!")
        else:
            print("The user cannot purchase the update as they already have it.")

    def gamble(self):

        # basic gambling function

        self.gambleAmount = self.scalePicker.get()

        if self.gambleAmount < 1:
            print("Gambling < 1 is not allowed.")
        else:
            # calculating win/loss
            print("gambled:" + str(self.gambleAmount))
            self.coinFlip = random.randint(0, 1)
            print("bresult:" + str(self.coinFlip))

            # calculating multipliers / others

            self.firstItemRand = random.randint(0, 1)

            # actual win/lose

            # lose function

            if self.coinFlip == 0:
                print("eresult:loss")
                if self.firstItemHave == 1 and self.firstItemRand == 1:
                    print("Item Effect: +25% Bonus from Loss")
                    self.winOrLose.configure(
                        text=("LOSE, but +$" + str(self.gambleAmount * 0.25)), fg="red")
                    self.totalCoins -= self.gambleAmount
                    print("total without Multiplier: " +
                          str(self.totalCoins))
                    self.totalCoins += (self.gambleAmount * 0.25)
                    print("total after Multiplier & Final: " +
                          str(self.totalCoins) + "\n\n")
                else:
                    self.winOrLose.configure(text="LOSE", fg="red")
                    self.totalCoins -= self.gambleAmount
                    print("total: $" + str(self.totalCoins) + "\n\n")

            # win function

            elif self.coinFlip == 1:
                print("eresult:win")
                self.winOrLose.configure(text="WIN", fg="green")
                self.totalCoins += (self.gambleAmount * 2)
                print("total:$" + str(self.totalCoins) + "\n\n")
            self.coinAmountLabel.configure(
                text="Total Coins: $" + str(self.totalCoins))
            self.scalePicker.configure(from_=0.0, to=self.totalCoins)

            if self.totalCoins <= 1:
                self.newWindow()
            else:
                pass

    # simulate a gamble, used in autoRoll

    def simulateGamble(self, simGamAmount, simRollAmount):
        # TODO: add a warning that states that if you lose all (and show percentage of losing all) you could go negative balance
        # TODO: choose to print it with the radio buttons
        # TODO: put varlog into a file and read it

        self.varLog = "## LOG OUTPUT ##\n"
        self.gambleAmount = simGamAmount
        self.rollAmountInit = simRollAmount
        self.rollAmount = simRollAmount

        while self.totalCoins > 0 and self.rollAmount != 0:
            self.coinFlip = random.randint(0, 1)

            if self.coinFlip == 0:
                self.totalCoins -= self.gambleAmount
                self.varLog += ("Instance " +
                                str((self.rollAmountInit - self.rollAmount) + 1) + ": Loss of " + str(self.gambleAmount) + ", total at $" + str(self.totalCoins) + "\n")
            elif self.coinFlip == 1:
                self.totalCoins += self.gambleAmount
                self.varLog += ("Instance " +
                                str((self.rollAmountInit - self.rollAmount) + 1) + ": Gain of " + str(self.gambleAmount) + ", total at $" + str(self.totalCoins) + "\n")

            self.rollAmount -= 1

            if self.totalCoins <= 1:
                self.newWindow()
            else:
                pass

        self.coinAmountLabel.configure(
            text="Total Coins: $" + str(self.totalCoins))
        self.scalePicker.configure(from_=0.0, to=self.totalCoins)
        print(self.varLog)

    # autoroll function

    def autoRoll(self, rolls, amount):
        # find number of rolls & amount to gamble; if nothing entered, set as 0
        try:
            self.numOfRolls = int(self.numOfRollsVal.get())
        except ValueError:
            self.numOfRolls = 0
        try:
            self.numOfGamble = int(self.amountGambleVal.get())
        except ValueError:
            self.numOfGamble = 0

        if self.numOfGamble > self.totalCoins:
            print("cannot gamble more than user has")
        else:
            self.simulateGamble(self.numOfGamble, self.numOfRolls)

    def clearPrint(self):
        print("\n" * 100)

    def autoRollDisplay(self):

        self.autoWindow = Toplevel(root)
        self.autoWindow.title("New Autoroll...")
        self.autoWindow.geometry("300x500")

        self.topTitle = Label(
            self.autoWindow, text="Create a new autoroll function:")
        self.topTitle.pack()

        self.numOfRolls = Label(self.autoWindow, text="Number of Rolls: ")
        self.numOfRolls.pack()

        self.numOfRollsVal = Entry(self.autoWindow, bd=3)
        self.numOfRollsVal.pack()

        self.amountGamble = Label(self.autoWindow, text="Amount to gamble: ")
        self.amountGamble.pack()

        self.amountGambleVal = Entry(self.autoWindow, bd=3)
        self.amountGambleVal.pack()

        self.radioLogTrue = Radiobutton(
            self.autoWindow, text="View log", variable=self.radVal, value=1)
        self.radioLogTrue.pack()

        self.radioLogFalse = Radiobutton(
            self.autoWindow, text="Don't View Log", variable=self.radVal, value=0)

        self.goButton = Button(
            self.autoWindow, text="Autroll", command=lambda: self.autoRoll(1, 2))
        self.goButton.pack()

        self.clButton = Button(
            self.autoWindow, text="clear", command=self.clearPrint)
        self.clButton.pack()

        # self.cancelButton = Button(self.autoWindow, text = "Cancel", command = self.close_window)
        # self.cancelButton.pack()

    def DisplayAll(self):

        # displays a scale widget and a button that has a command

        # labels at the top, displaying total amount of coins and how to gamble

        self.coinAmountLabel = Label(self.awesomeFrame, text=(
            "Total Coins: $" + str(self.totalCoins)))
        self.coinAmountLabel.pack()

        self.choosingGamble = Label(
            self.awesomeFrame, text="Choose the Amount to Gamble from:")
        self.choosingGamble.pack()

        self.scalePicker = Scale(
            self.awesomeFrame, from_=0.0, to=self.totalCoins, orient=HORIZONTAL)
        self.scalePicker.pack(fill=X)

        self.winOrLose = Label(self.awesomeFrame, text=" ", fg="red")
        self.winOrLose.pack()

        self.scaleWidgetGet = Button(
            self.awesomeFrame, text="Gamble!", command=self.gamble)
        self.scaleWidgetGet.pack()

        self.shopLabel = Label(self.awesomeFrame, text="SHOP:")
        self.shopLabel.pack()

        self.firstItemLabel = Label(
            self.awesomeFrame, text="50% chance to gain 25% of amount gambled when you lose.")
        self.firstItemLabel.pack()

        self.buyFirstItem = Button(
            self.awesomeFrame, text="BUY - $120", command=self.purchaseFirst)
        self.buyFirstItem.pack()

        self.autoRollButton = Button(
            self.awesomeFrame, text="New Autoroll", command=self.autoRollDisplay)
        self.autoRollButton.pack()


# main code / code that makes tkinter run

tkinterwhole = TkinterWhole(root)
tkinterwhole.DisplayAll()

root.mainloop()
