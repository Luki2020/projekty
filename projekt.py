from random import randint, random;
# wprowadzenie do gry
print('Witaj w grze ....')

# pobranie imienia
imie_boh = ''
while imie_boh == "":
    imie_boh = input("Wprowadz imie swojego głównego bohatera --> ")
    if imie_boh == "":
        print("Nie wprowadziłes imienia!!!!")

# pobranie typu
typ_boh = ''
while typ_boh.upper() not in ['A', 'D', 'Z']:
    print("Twoja kwota w portfelu wynosi 100$ wybierz typ bohatera:")
    typ_boh = input("( Zwykły = z/Z | Atakujący(-40$) = a/A | Defensor(-40$) = d/D ) ---> ")
    if typ_boh.upper() == 'A':
        hp_boh = 100
        kasa_boh = 60
    
    elif typ_boh.upper() == 'D':
        hp_boh = 100 + randint(10,20)
        kasa_boh = 60

    elif typ_boh.upper() == 'Z':
        hp_boh = 100
        kasa_boh = 100
    else:
        print("Nie wybrałes typu bohatera !!!!!! spróboj ponownie")

# atak podstawowy

def normalny_atak():
    if typ_boh.upper() in ['Z', 'D']:
        return randint(2,8)
    else:
        return randint(3, 15)
# atak specialny

def specjalny_atak():
    if typ_boh.upper() == 'Z':
        global kasa_boh
        kasa_boh = kasa_boh - 30
        return randint(5,15)
    elif typ_boh.upper() == 'D':
        kasa_boh = kasa_boh - 20
        hp_boh = hp_boh + 10
        return randint(5,15)
    else:
        kasa_boh = kasa_boh - 20
        return randint(10,20)
# wybieranie ataku

def wybieranie_ataku():
    print("Wybierz atak: ")
    if typ_boh.upper() == "Z":
        print("Atak podstawowy(2-8 hp) = p/P")
        print('Super atak(5-15 hp) = s/S ')
        wbr_atak = input("----> ")
        if wbr_atak.upper() == 'P':
            return normalny_atak()
        elif wbr_atak.upper() == 'S':
            if  kasa_boh >= 30:
               print("="*40)
               return specjalny_atak()  
            else:
                print("!"*100)
                print("Nie masz wystarczającej ilość pieniędzy :( " )
                return 0
        else:
            print("Nie wybrałeś ataku!")
            return 0
    
    elif typ_boh.upper() == "D":
        print("Atak podstawowy(2-8 hp) = p/P")
        print('Mega atak(5-15 hp) = m/M ')
        wbr_atak = input("----> ")
        if wbr_atak.upper() == 'P':
            return normalny_atak()
        elif wbr_atak.upper() == 'M':
            if kasa_boh >= 20:
                print("="*40)
                return specjalny_atak()  
            else:
                print("!"*100)
                print("Nie masz wystarczającej ilość pieniędzy :( " )
                return 0
        else:
            print("Nie wybrałeś ataku! ")
            return 0
    else:
        print("Atak podstawowy(3-15 hp) = p/P")
        print('Turbo atak(10-20 hp) = t/T ')
        wbr_atak = input("----> ")
        if wbr_atak.upper() == 'P':
            return normalny_atak()
        elif wbr_atak.upper() == 'T':
            if kasa_boh >= 20:
                print("="*40)
                return specjalny_atak()  
            else:
                print("!"*100)
                print("Nie masz wystarczającej ilości pieniedzy :( " )
            return 0
        else:
            print("Nie wybrałes ataku! ")
            return 0
# Przeciwnicy
goblin = ["Mały Goblin",20,3,0]
nymph = ["Nimfa Wodna",15,3,0]
list_Opponents = [goblin,nymph]

# gra
def random_oponent():
    Opponent =  list_Opponents[randint(0,1)].copy()
    return Opponent
liczba_pokonanych_przeciwników = 0
while hp_boh > 0:
    Opponent = random_oponent()
    print("-"*40)
    while Opponent[1] > 0 :
        print(f"{imie_boh} walczy teraz z {Opponent[0]}")
        print(f"Przeciwnik ma {Opponent[1]} Hp i zadaje ci {Opponent[2]} obrażeń")
        hp_boh = hp_boh - Opponent[2]
        if hp_boh < 0:
            break
        print(f"Zostało ci {hp_boh} Hp i {kasa_boh} Many")
        atak  = wybieranie_ataku()
        Opponent[1] = Opponent[1] - atak
        print(f"Zadałeś {atak} obrażeń")
    print("-"*40)
    print('Zabiłeś przeciwnika !!!')
    liczba_pokonanych_przeciwników = liczba_pokonanych_przeciwników + 1

print("-"*40)
print("YOU LOST !!!!")
print(f"Zabiles {liczba_pokonanych_przeciwników} przeciwników")
    
        
    
        


    

   



