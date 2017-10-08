__author__ = 'blademaw'

from Tkinter import *
import random

#Creates main window

root = Tk()
root.title("Gamble Coin 2017")
root.geometry("640x360")

#Creates class for whole program

class TkinterWhole(object):
    def __init__(self, root):

        # defining frame, vairable

        self.awesomeFrame = Frame(root)
        self.awesomeFrame.grid()

        self.gambleAmount = 0
        self.coinFlip = 0
        self.numChecker = 0
        self.totalCoins = 100
        self.firstItemHave = 0
        self.firstItemRand = 0

    def quitApplication(self):
        root.destroy
        window.destroy


    def newWindow(self):

        self.window = Toplevel(root)
        self.window.title("GAME OVER")
        self.window.geometry("200x50")

        self.WelcomeLabel2 = Label(self.window, text="Game Over!")
        self.WelcomeLabel2.grid(row = 1, column = 0)

        self.closeButton = Button(self.window, text = "okay...", command = self.quitApplication())
        self.closeButton.grid(row=2, column = 0)

    def purchaseFirst(self):
        if self.firstItemHave == 0:
            if self.totalCoins > 120:
                self.firstItemHave = 1
                print("The user successfully bought the upgrade!")
                self.totalCoins-=120
                self.firstItemLabel.config(fg="green") 
                self.coinAmountLabel.config(text=("Total Coins: "+str(self.totalCoins)))
                self.scalePicker.config(from_=0.0, to=self.totalCoins)

            elif self.totalCoins < 120:
                self.firstItemHave = 0
                print("The user is not able to afford this item!")
        else:
            print("The user cannot purchase the update as they already have it.")

    def gamble(self):
        
        #Basic Gambling Function
        
        self.gambleAmount = self.scalePicker.get()
        
        if self.gambleAmount < 1:
            print("Gambling < 1 is not allowed.")
        else:
            # calculating win/loss
            print(self.gambleAmount)
            self.coinFlip = random.randint(0,1)
            print("Coinflip Result: "+str(self.coinFlip))

            # calculating multipliers / others

            self.firstItemRand = random.randint(0,1)

            # actual win/lose

            # lose function

            if self.coinFlip == 0:
                print("Coinflip Result: Loss")
                if self.firstItemHave == 1 and self.firstItemRand == 1:
                    print("Item Effect: +25% Bonus from Loss")
                    self.winOrLose.configure(text=("LOSE, but +"+str(self.gambleAmount*0.25)))
                    self.totalCoins -= self.gambleAmount
                    print("Total Coins without Multiplier: "+str(self.totalCoins))
                    self.totalCoins += (self.gambleAmount*0.25)
                    print("Total Coins after Multiplier & Final: "+str(self.totalCoins)+"\n\n")
                else:
                    self.winOrLose.configure(text="LOSE", fg="red")
                    self.totalCoins -= self.gambleAmount
                    print("Total Coins: "+str(self.coinFlip)+"\n\n")

            # win function

            elif self.coinFlip == 1:
                print("Coinflip Result: Win")
                self.winOrLose.configure(text="WIN", fg="green")
                self.totalCoins += (self.gambleAmount*2)
                print("The user now has $"+str(self.totalCoins)+"\n\n")
            self.coinAmountLabel.configure(text="Total Coins: "+str(self.totalCoins))
            self.scalePicker.configure(from_=0.0, to=self.totalCoins)

            if self.totalCoins <= 1:
                self.newWindow()
            else:
                pass




    def DisplayAll(self):

        #Displays a scale widget and a button that has a command

        #Labels at the top, displaying total amount of coins and how to gamble

        self.coinAmountLabel = Label(self.awesomeFrame, text=("Total Coins: "+str(self.totalCoins)))
        self.coinAmountLabel.grid(row = 1, column = 1)

        self.choosingGamble = Label(self.awesomeFrame, text = "Choose the Amount to Gamble from:")
        self.choosingGamble.grid(row = 2, column = 1)

        self.scalePicker = Scale(self.awesomeFrame, from_=0.0, to=self.totalCoins, orient = HORIZONTAL)
        self.scalePicker.grid(row = 2, column = 2)

        self.buyFirstItem = Button(self.awesomeFrame, text = "BUY ($120)", command = self.purchaseFirst)
        self.buyFirstItem.grid(row=6, column=0)

        self.winOrLose = Label(self.awesomeFrame, text = " ", fg = "red")
        self.winOrLose.grid(row = 3, column = 2)

        self.scaleWidgetGet = Button(self.awesomeFrame, text = "Gamble!", command = self.gamble)
        self.scaleWidgetGet.grid()

        self.shopLabel = Label(self.awesomeFrame, text = "SHOP:")
        self.shopLabel.grid(row=5, column=1)

        self.firstItemLabel = Label(self.awesomeFrame, text = "50% chance to gain 25% of gamble when you lose.")
        self.firstItemLabel.grid(row=6, column=2)

#Main code / code that makes tkinter run

tkinterwhole = TkinterWhole(root)
tkinterwhole.DisplayAll()

root.mainloop()