# -*- coding: utf-8 -*-
"""
Created on Mon Dec 25 18:20:57 2017

@author: tdpco
"""
from __future__ import division
import random

class Player(object):
    def __init__(self,money,name,card=0,userbet=0,wins=0,loses=0,busts=0):
        self.money = money;
        self.name = name;
        self.card = card;
        self.userbet = userbet;
        self.wins = wins;
        self.loses = loses;
        self.busts = busts;
    
    def getloses(self):
        return self.loses;
    def getwins(self):
        return self.wins;
    def getbusts(self):
        return self.busts;
    def setbusts(self):
        self.busts += 1;
    def setwins(self):
        self.wins += 1;
    def setloses(self):
        self.loses += 1;
    def getmoney(self):
        return self.money;
    def setmoney(self,money):
        self.money = money;
    def setname(self,name):
        self.name = name;
    def getname(self):
        return self.name;
    def setcardvalue(self,card):
        self.card = card;
    def getcardvalue(self):
        return self.card;
    def getcardvaluecount(self):
        count = 0;
        for value in self.card:
            count += value; 
        return count;      
    def getuserbet(self):
        return self.userbet;
    def setuserbet(self,userbet):
        self.userbet = userbet;
    def user_curr_status(self):
        print ("\n\t\t%s have got : %s and your current count is %s"%(self.getname(),self.getcardvalue(),self.getcardvaluecount()));
    def user_input(self,inp):
        if inp == 1 :
            cardvalplayer.append(random.randrange(1,14));
            player.setcardvalue(cardvalplayer);
            player.user_curr_status();
            if self.getcardvaluecount() > 21 :
                 return True;
            else:
                return False;
        elif inp ==  2:
            #player.user_curr_status();
            #dealer.getcardvalue();
            return True;
        elif inp == 3:
            cardvalplayer.append(random.randrange(1,14));
            player.setcardvalue(cardvalplayer);
            player.user_curr_status();
            dealer.getcardvalue();
            return True;
        else:
            print ("\n\t\tSorry you have entered wrong input.");
            return False;

    
class Dealer(Player):
    def __init__(self,name='Dealer',card=0):
        self.card = card;
        self.name = name;
    def getname(self):
        return self.name;
    def setcardvalue(self,card):
        self.card = card;
    def getcardvalue(self):
        #print ("Dealer have got : %s and your current count is %s"%(self.card,self.getcardvaluecount()));
        return self.card;
    def getcardvaluecount(self):
        count = 0;
        for value in self.card:
            count += value; 
        return count;      
    def getcardvaluefirst(self):
        return self.card[0];

    def dealer_curr_status(self):
        print ("\n\t\tDealer have got [%s] and a hidden card"%(self.getcardvaluefirst()));

    def checkwinlose(self,object):
        for i in range(10):
            if self.getcardvaluecount() < object.getcardvaluecount() and object.getcardvaluecount() <= 21 and self.getcardvaluecount() <= 21:
                cardvaldealer.append(random.randrange(1,14));
                self.setcardvalue(cardvaldealer);
                print ("\n\t\tDealer has now got %s"%self.getcardvalue());
            else:
                break;
        if object.getcardvaluecount() <= 21 and self.getcardvaluecount() <= 21 :
            if object.getcardvaluecount() > self.getcardvaluecount() :
                temp = object.getmoney() + object.getuserbet();
                object.setmoney(temp);
                print ("\n\t\tPlayer %s has won the match and your current balance is %s"%(object.getname(),object.getmoney()));
                object.setwins();
                print ("\n\t\tDealer has lost %s card and count %s"%(self.getcardvalue(),self.getcardvaluecount()));    
            elif object.getcardvaluecount() == self.getcardvaluecount() :
                print ("\n\t\tNo one has won the match");
            else:
                print ("\n\t\tDealer has won the match %s and count %s"%(self.getcardvalue(),self.getcardvaluecount()));    
                #print(object.getmoney())
                #print(object.getuserbet())
                temp = object.getmoney() - object.getuserbet();
                #print(temp)
                object.setmoney(temp);
                print ("\n\t\tPlayer %s have lost %s and your current balance is %s"%(object.getname(),object.getuserbet(),object.getmoney()));
                object.setloses();
        else:
            if object.getcardvaluecount() > 21:
                #print(object.getmoney())
                #print(object.getuserbet())
                temp = object.getmoney() - object.getuserbet();
                #print(temp)
                object.setmoney(temp);
                print ("\n\t\tPlayer %s have lost %s and your current balance is %s"%(object.getname(),object.getuserbet(),object.getmoney()));
                object.setbusts();
            else:
                if len(self.getcardvalue()) > 2:
                    print ("\n\n\t\tYou Won");
                else:
                    print ("\n\t\tDealer has bust %s card and count %s"%(self.getcardvalue(),self.getcardvaluecount()));    
                temp = object.getmoney() + object.getuserbet();
                object.setmoney(temp);
                print ("\n\t\tPlayer %s has won the match and your current balance is %s"%(object.getname(),object.getmoney()));
                object.setwins();


print ("\n\n\t\t\t\t\t\tWelcome to BlackJack");
name = input("\n\n\t\tEnter Your Name: ");
#name = "TDP";
amount = int(input("\n\t\tEnter the total amount to buy chips :  "));
#amount = 10000;
player = Player(amount,name);
dealer = Dealer();
#print obj1.getname();
#print obj1.getmoney();
print ("\n\t\t\t\t\tLet's Start the Game\n\n");
ans = 'Y'
while ans == 'Y' or ans == 'Yes' or ans == 'y' or ans == 'yes':
    count = 0;
    userbet = int(input("\t\tEnter the amount you want to bet : "));
    #userbet = 250;
    if userbet <= player.getmoney():
        player.setuserbet(userbet);
        print ("\n\t\tPlayer %s current bet for this game is %s"%(player.getname(),player.getuserbet()));
    else:
        print ("\n\t\tSorry you dont have that Much amount. Your current balance is : %s"%player.getmoney());
        try:
            temp = input("\n\t\tPlease enter amount to add or Y if u want to change the user bet. ");
            if temp == 'Y':
                userbet = int(input("\n\t\tEnter the amount you want to bet : "));
                player.setuserbet(userbet);        
            else:
                temp = int(temp);
                player.setmoney(player.getmoney() + temp);
        except:
            print ("\n\t\tPlease insert numeric value");
                     
    cardvalplayer = [];
    cardvaldealer = [];
    while count < 2:
        cardvalplayer.append(random.randrange(1,14));
        player.setcardvalue(cardvalplayer);
        cardvaldealer.append(random.randrange(1,14));
        dealer.setcardvalue(cardvaldealer);
        count += 1;
    player.user_curr_status();
    dealer.dealer_curr_status();
    val = False;
    if player.getcardvaluecount() <= 21:
        while val==False:
            print("\n\t\tPlease choose a option : \n\t\t1. Hit \n\t\t2. Stand \n\t\t3. Double \n");
            temp = int(input("\n\t\tEnter Choice : "));
            val = player.user_input(temp);
            #print val;
    dealer.checkwinlose(player);
    print ("\n\t\tPlayer : %s has Won : %s and Lose : %s and Busts : %s"%(player.getname(),player.getwins(),player.getloses(),player.getbusts()));
    if player.getmoney() <=0 :
        print ("\n\t\tSorry You are out of Money.");
        break;
    else:
        ans = input("\n\t\t\tDo you want to play another round (Y/N) ? ");

print ("\n\n\t\t\tThanks for Playing Blackjack Game");
        