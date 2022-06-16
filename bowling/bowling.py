# ************************************************************************
# Andrew Yeh
# Bowling
# CompSci30
# 3/15/2022
# This program is my own work - A.Y.

from random import randint
from tkinter import *
from tkinter import ttk


class Window:
    def __init__(self):
        # initialization
        window = Tk()
        window.geometry("500x500")
        window.title("Bowling")

        # starts a bowling game
        self.currentGame = BowlingGame()
        self.totalScore = 0

        # functions frame
        functionFrame = Frame(window)
        functionFrame.pack(side=LEFT, padx=(30, 0))

        # button
        self.rollButton = Button(functionFrame, text="Roll ball", command=self.roll)
        self.rollButton.pack(side=TOP, pady=10)

        self.nextButton = Button(functionFrame, text="Next game", command=self.next, state=DISABLED)
        self.nextButton.pack(side=TOP, pady=10)

        self.resetButton = Button(functionFrame, text="Reset", command=self.reset)
        self.resetButton.pack(side=TOP, pady=10)

        # label
        self.scoreLabel = Label(functionFrame, text="Score: 0")
        self.scoreLabel.pack(side=TOP, pady=10)

        self.hitLabel = Label(functionFrame, text="Hits: 0")
        self.hitLabel.pack(side=TOP, pady=10)

        self.totalScoreLabel = Label(functionFrame, text="Total Score: 0")
        self.totalScoreLabel.pack(side=TOP, pady=10)

        # treeview
        self.itemTreeview = ttk.Treeview(window)
        self.itemTreeview["show"] = 'headings'
        self.itemTreeview["columns"] = ("c1", "c2", "c3")
        self.itemTreeview.column(f"# {1}", anchor=CENTER, minwidth=50, width=75, stretch=NO)
        self.itemTreeview.heading(f"# {1}", text="Try number")
        self.itemTreeview.column(f"# {2}", anchor=CENTER, minwidth=50, width=125, stretch=NO)
        self.itemTreeview.heading(f"# {2}", text="Score")
        self.itemTreeview.column(f"# {3}", anchor=CENTER, minwidth=50, width=125, stretch=YES)
        self.itemTreeview.heading(f"# {3}", text="Hits")
        self.itemTreeview.pack(side=RIGHT, fill=BOTH, expand=TRUE, padx=30, pady=30)

        # starts window
        window.mainloop()

    def roll(self):
        score = self.currentGame.rollBallAndReturnScore()
        self.scoreLabel["text"] = "Score:", score[0]
        self.hitLabel["text"] = "Hits:", score[1]
        if self.currentGame.returnTryNum() == 2:
            self.rollButton["state"] = "disabled"
            self.nextButton["state"] = "active"

    def next(self):
        self.itemTreeview.insert("", "end", values=[self.currentGame.returnLaneNum(), self.scoreLabel["text"][7:],
                                                    self.currentGame.returnTotalHits()])
        self.totalScore += int(self.scoreLabel["text"][7:])
        self.totalScoreLabel["text"] = "Total score: " + str(self.totalScore)
        self.currentGame.nextLane()
        if self.currentGame.returnLaneNum() != 11:
            self.rollButton["state"] = "active"
            self.nextButton["state"] = "disabled"
        else:
            self.rollButton["state"] = "disabled"
            self.nextButton["state"] = "disabled"

    def reset(self):
        self.currentGame = BowlingGame()
        self.rollButton["state"] = "active"
        self.nextButton["state"] = "active"
        for i in self.itemTreeview.get_children():
            self.itemTreeview.delete(i)
        self.scoreLabel["text"] = "Score: 0"
        self.hitLabel["text"] = "Hits: 0"
        self.totalScoreLabel["text"] = "Total Score: 0"
        self.totalScore = 0


class BowlingGame:
    def __init__(self):
        self.currentLane = Lane()
        self.laneNum = 1

    def rollBallAndReturnScore(self):
        return self.currentLane.rollBallAndReturnScore()

    def returnTryNum(self):
        return self.currentLane.returnTryNum()

    def nextLane(self):
        self.currentLane = Lane()
        self.laneNum += 1

    def returnLaneNum(self):
        return self.laneNum

    def returnTotalHits(self):
        return self.currentLane.returnTotalHits()


class Lane:
    def __init__(self):
        self.tryNum = 0
        self.score = 0
        self.pinsLeft = 10

    def rollBallAndReturnScore(self):
        hits = randint(0, self.pinsLeft)
        self.pinsLeft -= hits
        self.score += hits
        self.tryNum += 1
        if self.tryNum == 1:
            if hits == 10:
                self.tryNum += 1
                return [20, hits]
            else:
                return [self.score, hits]
        elif self.tryNum == 2:
            if self.pinsLeft == 0:
                return [15, hits]
            else:
                return [self.score, hits]

    def returnTryNum(self):
        return self.tryNum

    def returnTotalHits(self):
        return 10 - self.pinsLeft


def main():
    Window()

if __name__ == "__main__":
    main()
