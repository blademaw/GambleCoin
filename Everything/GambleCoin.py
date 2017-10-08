__author__ = 'user 1'

from Tkinter import *
import random, time

#Creates main window

root = Tk()
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
        self.firstItem = 0
        self.firstItemRand = 0

    def quitApplication(self):
        root.destroy
        window.destroy


    def newWindow(self):

        self.window = Toplevel(root)    #Create a new toplevel window, as a child of the 'root' window.
        self.window.title("GAME OVER")
        self.window.geometry("200x50")

        self.WelcomeLabel2 = Label(self.window, text = "Game Over!")
        self.WelcomeLabel2.grid(row = 1, column = 0)

        self.closeButton = Button(self.window, text = "okay...", command = self.quitApplication())
        self.closeButton.grid(row=2, column = 0)

    def activateFirst(self):

        if self.totalCoins > 120:
            self.firstItem = 1
            print("The user successfully bought the upgrade!")
            self.totalCoins -= 120
            self.coinAmountLabel.config(text=("Total Coins: "+str(self.totalCoins)))
            self.scalePicker.config(from_=0.0, to=self.totalCoins)

        elif self.totalCoins < 120:
            self.firstItem = 0
            print("the user cannot afford this item!")

        else:
            pass

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
                if self.firstItem == 1 and self.firstItemRand == 1:
                    print("+50%")
                    self.winOrLose.configure(text="LOSE, but +25%")
                    self.totalCoins -= self.gambleAmount
                    print("The user had multiplier. current = "+str(self.totalCoins))
                    self.totalCoins += (self.gambleAmount*0.25)
                    print("The user just gained 25% of gambleAmount. after = "+str(self.totalCoins))
                else:
                    self.winOrLose.configure(text="LOSE", fg="red")
                    self.totalCoins -= self.gambleAmount
                    print("The user now has $"+str(self.coinFlip)+"\n\n")

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

        self.buyFirstItem = Button(self.awesomeFrame, text = "BUY ($120)", command = self.activateFirst)
        self.buyFirstItem.grid(row=6, column=0)

        self.winOrLose = Label(self.awesomeFrame, text = " ", fg = "red")
        self.winOrLose.grid(row = 3, column = 2)

        self.scaleWidgetGet = Button(self.awesomeFrame, text = "Gamble!", command = self.gamble)
        self.scaleWidgetGet.grid()

        self.shopLabel = Label(self.awesomeFrame, text = "SHOP:")
        self.shopLabel.grid(row=5, column=1)

        self.firstItem = Label(self.awesomeFrame, text = "If you lose, there is a 50% chance you will get 25% of your coins back.")
        self.firstItem.grid(row=6, column=2)

#Main code / code that makes tkinter run

tkinterwhole = TkinterWhole(root)
tkinterwhole.DisplayAll()

root.mainloop()