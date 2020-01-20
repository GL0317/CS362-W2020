"""
Created on Sun Jan 19 21:13:36 2020

@author: Gerson Lindor Jr.
"""

import Dominion

# returns a list of dominion cards in a box
# @params:  victoryCards holds the number of victory cards
#           cardNum is the number of cards for each type of cards (except victory cards)
def defineBox(victoryCards, cardNum):
    box = {}
    box["Woodcutter"] = [Dominion.Woodcutter()] * cardNum
    box["Smithy"] = [Dominion.Smithy()] * cardNum
    box["Laboratory"] = [Dominion.Laboratory()] * cardNum
    box["Village"] = [Dominion.Village()] * cardNum
    box["Festival"] = [Dominion.Festival()] * cardNum
    box["Market"] = [Dominion.Market()] * cardNum
    box["Chancellor"] = [Dominion.Chancellor()] * cardNum
    box["Workshop"] = [Dominion.Workshop()] * cardNum
    box["Moneylender"] = [Dominion.Moneylender()] * cardNum
    box["Chapel"] = [Dominion.Chapel()] * cardNum
    box["Cellar"] = [Dominion.Cellar()] * cardNum
    box["Remodel"] = [Dominion.Remodel()] * cardNum
    box["Adventurer"] = [Dominion.Adventurer()] * cardNum
    box["Feast"] = [Dominion.Feast()] * cardNum
    box["Mine"] = [Dominion.Mine()] * cardNum
    box["Library"] = [Dominion.Library()] * cardNum
    box["Gardens"] = [Dominion.Gardens()] * victoryCards
    box["Moat"] = [Dominion.Moat()] * cardNum
    box["Council Room"] = [Dominion.Council_Room()] * cardNum
    box["Witch"] = [Dominion.Witch()] * cardNum
    box["Bureaucrat"] = [Dominion.Bureaucrat()] * cardNum
    box["Militia"] = [Dominion.Militia()] * cardNum
    box["Spy"] = [Dominion.Spy()] * cardNum
    box["Thief"] = [Dominion.Thief()] * cardNum
    box["Throne Room"] = [Dominion.Throne_Room()] * cardNum
    return box

# Creates a supply pile
def supplyPile(supply, victoryCards, curseCards, playerNames):
    # The supply always has these cards
    copperCount = 60
    silverCount = 40
    goldCount = 30

    supply["Copper"] = [Dominion.Copper()] * (copperCount - len(playerNames) * 7)
    supply["Silver"] = [Dominion.Silver()] * silverCount
    supply["Gold"] = [Dominion.Gold()] * goldCount
    supply["Estate"] = [Dominion.Estate()] * victoryCards
    supply["Duchy"] = [Dominion.Duchy()] * victoryCards
    supply["Province"] = [Dominion.Province()] * victoryCards
    supply["Curse"] = [Dominion.Curse()] * curseCards
