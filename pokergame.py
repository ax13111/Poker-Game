#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 20 15:40:41 2023

@author: sunyenpeng
"""
import random
import itertools

def poker_deck():
    color=["♠", "♣", "♥", "♦"]
    number=[i+1 for i in range(13)]
    poker=[]
    for i in color:
        for j in number:
            poker.append((i,j))
    return poker

mydeck=poker_deck()

random.shuffle(mydeck)
player1_hand = mydeck[:2]
player2_hand = mydeck[2:4]
community_cards = mydeck[4:9]

p1=player1_hand
p2=player2_hand
for i in community_cards:
    p1.append(i)
    p2.append(i)
    p1=sorted(p1, key=lambda x: x[1])
    p2=sorted(p2, key=lambda x: x[1])


def has_straight_flush(cards): #Note, the cards input should be in tuple!
    
    cards_by_suit = {}
    for card in cards:
        suit, rank = card
        if suit not in cards_by_suit:
            cards_by_suit[suit] = []
        cards_by_suit[suit].append(rank)

    for suit in cards_by_suit:
        ranks = sorted(cards_by_suit[suit])
        if ranks == [1, 10, 11, 12, 13]:
            return True
        for i in range(len(ranks) - 4):
            if ranks[i:i+5] == list(range(ranks[i], ranks[i]+5)):
                return True
    return False

def has_flush(cards):
    color=[]
    for c in cards:
        color.append(c[0])
    if color.count(color[0])==5:
        return True
    return False

def has_fourofakind(cards):
    number=[]
    check=[]
    for c in cards:
        number.append(c[-1])
    for n in number:
        check.append(number.count(n))
    if check.count(4)==4:
        return True
    return False

def has_fullhouse(cards):
    number=[]
    for c in cards:
        number.append(c[-1])
    if number.count(number[0])==2 and number.count(number[-1])==3:
        return True
    elif number.count(number[0])==3 and number.count(number[-1])==2:
        return True
    
    return False

def has_triple(cards):
    number=[]
    for c in cards:
        number.append(c[-1])
    for n in number:
        if number.count(n)==3:
            return True
    return False

def has_twopair(cards):
    number=[]
    check=[]
    for c in cards:
        number.append(c[-1])
    for n in number:
        check.append(number.count(n))
    if check.count(1)==1 and check.count(2)==4:
        return True
    return False

def has_pair(cards):
    number=[]
    check=[]
    for c in cards:
        number.append(c[-1])
        
    for n in number:
        check.append(number.count(n))
    
    if check.count(2)==2:
        return True
    return False
    
player1=list(itertools.combinations(p1,5))
player2=list(itertools.combinations(p2,5))

def rank(player):
    for i in range(len(player)):
        if has_straight_flush(player[i]):
            print("The player has a straight flush!\n")
            print("Show cards:",player[i])
            return 7,player[i]
            break
    for i in range(len(player)):        
        if has_fourofakind(player[i]):
            print("The player has a four of a kind!")
            print("Show cards:",player[i])
            return 5,player[i]
            break
    for i in range(len(player)):      
        if has_flush(player[i]):
            print("The player has a flush!")
            print("Show cards:",player[i])
            return 6,player[i]
            break
    for i in range(len(player)):
        if has_fullhouse(player[i]):
            print("The player has a full house!")
            print("Show cards:",player[i])
            return 4,player[i]
            break
    for i in range(len(player)):
        if has_triple(player[i]):
            print("The player has a triple!")
            print("Show cards:",player[i])
            return 3,player[i]
            break
    for i in range(len(player)):
        if has_twopair(player[i]):
            print("The player has two pairs!")
            print("Show cards:",player[i])
            return 2,player[i]
            break
    for i in range(len(player)):
        if has_pair(player[i]):
            print("The player has a pair!")
            print("Show cards:",player[i])
            return 1,player[i]
            break
            
    else:
        print("The player has no special combination!")
        print("Show cards:",player[-1])
        return 0,player[-1]
    
def winner(x,y):
    p1=rank(x)
    p2=rank(y)
    if p1[0]>p2[0]:
        print("Player1 with\n",p1,"\nPlayer 1 wins the game!\n")
    elif p2[0]>p1[0]:
        print("Player2 with\n",p2[-1],"\nPlayer 2 wins the game!\n")
    else:
        print("Check players cards!")
        print("Community cards:", community_cards)
        print("Player1's biggest combination:",rank(x)[-1])
        print("Player2's biggest combination:",rank(y)[-1])
        
        
        
    
        

    
    
        



        
    
    
    

    




































