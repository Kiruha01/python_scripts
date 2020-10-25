from random import shuffle, randint
from time import sleep
from colorama import init, Fore, Back, Style
from termcolor import colored
import os

init()


class Card(object):
    """docstring for card"""
    def __init__(self, mast, card, value):
        self.mast = mast
        self.card = card
        self.color = 'black' if mast in ('♣', '♠') else 'red'
        self.value = value

    def compare(self, card):      # Может ли эта карта побить карту "card"
        if (self.value > card.value) and (self.mast == card.mast or self.mast == kozyr):
            return True
        return False

    def get(self):
        return self.card + self.mast

    def __str__(self):
        if self.color == 'black':
            return Fore.BLACK + Back.WHITE + self.get() + Style.RESET_ALL
        return Fore.RED + Back.WHITE + self.get() + Style.RESET_ALL
        

class Player(object):
    """docstring for Player"""
    def __init__(self, coloda):
        self.card = coloda

    def go(self, index):

        return self.card.pop(index)

    def beat(self, index_of_my_card, card):
        if self.card[index_of_my_card].compare(card):
            return self.go(index_of_my_card)
        return False # Незьзя

    def throw(self, list_of_cards, index_of_my_card):
        masts = [i.card for i in list_of_cards]
        if self.card[index_of_my_card].card in masts:
            return self.go(index_of_my_card)
        return False # Нельзя

    def got(self, list_of_cards):
        self.card.extend(list_of_cards)

    def get(self):
        return len(self.card)

    def make_full(self, coloda):
        if len(self.card) < 6:
            num = 6-len(self.card)
            self.card.extend(coloda[:num])
            return coloda[num:]
        else:
            return coloda
    def Ineed(self):
        if len(self.card) < 6:
            return True
    def get_card(self, newCard):
        self.card.append(newCard)

    #------------------------------------------------------

    def next_step(self, events):  # Для бота
        self.card.sort(key=lambda card: card.value) 
        if len(events):
            if len(events) % 2 == 0: # Если карты покрыты 
                for index in range(len(self.card)):
                    card = self.throw(events, index) # То подкидываем
                    if card:
                        return card
                return False # Нечем, если цикл прошёл без успешно
            else:                                                   # Иначе
                for index, _card_ in enumerate(self.card):
                    if (_card_.mast == events[-1].mast) or _card_.mast == kozyr:
                        card = self.beat(index, events[-1])         # Бъём
                        if card:
                            return card
                return False # Беру, если цикл прошёл без успешно
        else:
            return self.go(0)

class People(Player):

    def next_step(self, events, index):  # Для человека
        if len(events):
            if len(events) % 2 == 0:  # Если карты покрыты 
                card = self.throw(events, index)  # То подкидываем
                if card:
                    return card
                return False # Нельзя
            else:                                   # Иначе
                card = self.beat(index, events[-1])  # Бъём
                if card:
                    return card
                return False # Нельзя
        else:
            return self.go(index)



def blit(kozyr, card1, card2, events=None):
    os.system('cls')
    print('\t', len(coloda),'\t', 'Козырь: ', Fore.BLACK + Back.WHITE + kozyr + Style.RESET_ALL)
    print('\n\n', str(Fore.BLACK + Back.WHITE + ' * ' + Style.RESET_ALL + ' ')*len(card2), '\n\n')
    
    if events:
        for i in range(round(len(events)/2+0.2)):
            print(events[2*i], end = '  ') # Карты ходящего
        print()

        if len(events) > 1:
            for i in range(len(events)//2):
                print(events[2*i + 1], end = '  ') # Карты бъющего
        print()
    else:
        print('\n\n', end='')
    print('\n')

    for i in card1:
        # if i.color == 'black':
        #     print(Fore.BLACK + Back.WHITE, '|', i, end='| ' + Style.RESET_ALL, sep='')
        # if i.color == 'red':
        #     print(Fore.RED + Back.WHITE, '|', i, end='| ' + Style.RESET_ALL, sep='')
        print( i, end = ' ', sep='')
    print('\n1  2  3  4  5  6  7  8  9  10  12  13  14  15  16  17  18  19')


def go_for_real_person(self, events):
    while True:
        try:
            hod = int(input())
        except:
            hod = 9999
        if hod == 0:
            return 1
        hod -= 1
        if hod > len(self.card):
            print('No no no no no')
            continue
        break
    return self.next_step(events, hod)

#===================================================================

mast = ['♦', '♣', '♠', '♥']
card = ['6', '7', '8', '9', '10', 'J', 'Q', 'К', 'Т']

        
kozyr = mast[randint(0, 3)]

coloda = []
for _mast_ in mast:
    for value, _card_ in enumerate(card):
        if _mast_ == kozyr:
            coloda.append(Card(_mast_, _card_, value+len(card)))
        else:
            coloda.append(Card(_mast_, _card_, value))

shuffle(coloda)

per1 = People(coloda[:6])
coloda = coloda[6:]
per2 = Player(coloda[:6])
coloda = coloda[6:]

players = [per1, per2]

events = []
i = 0

win = True
while win: # Основной цикл

    while (players[0].Ineed() or players[1].Ineed()) and coloda:
        if players[0].Ineed():
            players[0].get_card(coloda.pop(-1))
        if players[1].Ineed() and coloda:
            players[1].get_card(coloda.pop(-1))
    # coloda = players[0].make_full(coloda)
    
    # active = players[i % 2]
    # coloda = players[1].make_full(coloda)
    


    while True:
        if players[0].get() == 0:
            blit(kozyr, players[0].card, players[1].card, events)
            print('----Human-Win------')
            win = False
            break
        if players[1].get() == 0:
            blit(kozyr, players[0].card, players[1].card, events)
            print('-----Bot-Win-------')
            win = False
            break
        blit(kozyr, players[0].card, players[1].card, events)
        if i % 2 == 0:  # Если человек
            answer = go_for_real_person(players[i % 2], events)
            if answer:
                if answer == 1:
                    if len(events) % 2 == 0: # Если он должен был идти
                        print('--------Бито--------')
                        sleep(2)
                        events = []
                        i +=1
                        break
                    else:  # Если должен был крыть
                        print('--------Беру--------')
                        sleep(2)
                        players[i % 2].got(events)
                        events = []
                        i += 1
                        break
                events.append(answer)
                i += 1
                continue
            else:
                print('-!-!-!-Нельзя-!-!-!-!-')
                continue
        else:  # Если бот
            answer = players[i % 2].next_step(events)
            if len(events) % 2 == 0: # Если он ходил
                if answer:
                    events.append(answer)
                    i += 1
                    continue
                else:
                    print('-------Бито!-------')
                    sleep(2)
                    events = []
                    i += 1
                    break 
            else: # Если он крыл
                if answer:
                    events.append(answer)
                    i += 1
                    continue
                else:
                    print('----Беру-----')
                    sleep(2)
                    players[i % 2].got(events)
                    events=[]
                    i += 1
                    break





input()
