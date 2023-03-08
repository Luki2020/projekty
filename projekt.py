from random import randint

# wprowadzenie do gry
print('Witaj w grze "Wojna w swięta"')

# wybór imienia bohatera
imie_boh = ''
while imie_boh == "":
    imie_boh = input("Wprowadz imie głownego bohatera --> ")
    if imie_boh == "":
        print("Nie wprowadziłes imienia!!!!")

# wybór typu bohatera
pomocnik = ''
typ_boh = ''
hp_boh = 0 
pierniczki = 0
while typ_boh.upper() not in ['S', 'K', 'H']:
    print("Masz 150 pierniczków, wybierz swojego pomocnika w walce:")
    typ_boh = input("( Z: swiety mikolaj = s/S | kevin(-40P) = k/K | Shrek(-40P) = h/H ) ---> ")
    if typ_boh.upper() == 'K':
        hp_boh = 100
        pierniczki = 60
    
    elif typ_boh.upper() == 'H':
        hp_boh = 100 + randint(10,20)
        pierniczki = 60

    elif typ_boh.upper() == 'S':
        hp_boh = 100
        pierniczki = 100
    else:
        print("Nie wybrałes pomocnika!!!!!! spróboj ponownie")


if typ_boh.upper() in ['K']:
    pomocnik = "Kevinem"
elif typ_boh.upper() in ['S']:
    pomocnik = "Swietym mikołajem"
elif typ_boh.upper() in ['H']:
    pomocnik = "Shrekiem"


# atak podstawowy
def normalny_atak():
    return randint(2,8)

# atak specjalny
def specjalny_atak():
    global pierniczki
    global hp_boh
    if typ_boh.upper() == 'S':
        pierniczki = pierniczki - 30
        return randint(5,15)
    elif typ_boh.upper() == 'H':
        pierniczki = pierniczki - 20
        hp_boh = hp_boh + 10
        return randint(5,15)
    else:
        pierniczki = pierniczki - 20
        return randint(10,20)

# wybieranie ataku
def wybieranie_ataku():
    print("\n Wybierz atak: ")

    if typ_boh.upper() == "Z":
        print("wywolaj burze sniezna!(2-8 hp) = b/B")
        print('atak specialny(5-15 hp) = s/S ')
        wbr_atak = input("----> ")
        
        if wbr_atak.upper() == 'B':
            return normalny_atak()
        elif wbr_atak.upper() == 'S':
            if  pierniczki >= 30:
               print("="*40)
               return specjalny_atak()  
            else:
                print("!"*100)
                print("Nie masz wystarczającej ilości pierniczków :( " )
                return 0
        else:
            print("Nie wybrałeś ataku!")
            return 0
    
    elif typ_boh.upper() == "D":
        print("Rzuc rozga!(2-8 hp) = r/R")
        print('Mega atak(5-15 hp) = m/M ')
        wbr_atak = input("----> ")
        if wbr_atak.upper() == 'R':
            return normalny_atak()
        elif wbr_atak.upper() == 'M':
            if pierniczki >= 20:
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
        print("Wystaw armie swiatecznych elfow!(3-15 hp) = a/A")
        print('mega atak(10-20 hp) = m/M ')
        wbr_atak = input("----> ")
        if wbr_atak.upper() == 'P':
            return normalny_atak()
        elif wbr_atak.upper() == 'M':
            if pierniczki >= 20:
                print("="*40)
                return specjalny_atak()  
            else:
                print("!"*100)
                print("Nie masz wystarczającej ilości pieniedzy :( " )
            return 0
        else:
            print("Nie wybrałes ataku! ")
            return 0

# Przeciwnicy 1 poziom
# 0 - imie, 1 - hp, 2 - atak
prze1 = ["Grinch", 10, 10]
prze2 = ["Ebenezer Scrooge", 5, 10]
prze3 = ["Dziadek Mróz", 15, 10]
prze4 = ["El Caganer", 15, 5]
lista_prze = [prze1, prze2, prze3, prze4]

def random_prze():
    przeciwnik = lista_prze[randint(0,3)]
    return przeciwnik

# przeciwnik drugi poziom

boss = ["Wielka Stopa", 25, randint(5,10)]

# nagroda(doładowanie hp)
def nagroda():
    print("Możesz kupić doładowanie 30 hp(-30$)")
    wybr = input("T - tak, N - nie ---> ")
    global hp_boh
    if wybr.upper() == "T":
        hp_boh = hp_boh + 30
        print(f"Doładowano hp | {imie_boh} ma {hp_boh} hp")
    else:
        print(f"Nie doładowano hp  | {imie_boh} ma {hp_boh} hp")


# gra
liczba_pokonanych_przeciwników = 0
liczba_zadanych_obrażeni = 0
while hp_boh > 0:

    if liczba_pokonanych_przeciwników < 3:
        if liczba_pokonanych_przeciwników == 0:
            print("POZIOM 1")

        Opponent = random_prze()
        print("="*40)
        while Opponent[1] > 0 :
            print(f"{imie_boh} ze {pomocnik} walczy teraz z {Opponent[0]}")
            print(f"Przeciwnik ma {Opponent[1]} Hp i zadaje ci {Opponent[2]} obrażeń")
            hp_boh = hp_boh - Opponent[2]
            if hp_boh <= 0:
                break
            print(f"Zostało ci {hp_boh} Hp i {pierniczki} pierniczkow")
            atak  = wybieranie_ataku()
            Opponent[1] = Opponent[1] - atak
            liczba_zadanych_obrażeni += atak
            print(f"{imie_boh} ze {pomocnik} zadaje {atak} obrażeń \n")
            
        if hp_boh > 0:
            print("-"*40)
            print(f'{imie_boh} zabił przeciwnika !!!')
            liczba_pokonanych_przeciwników = liczba_pokonanych_przeciwników + 1
    elif liczba_pokonanych_przeciwników == 3:
        if hp_boh < 60:
            nagroda()
        print("="*40)
        print("POZIOM 2")
        print("="*40)
        while boss[1] > 0 :
            print(f"{imie_boh} ze {pomocnik} walczy teraz z {boss[0]} (boss)")
            print(f"Przeciwnik ma {boss[1]} Hp i zadaje ci {boss[2]} obrażeń")
            hp_boh = hp_boh - boss[2]
            if hp_boh <= 0:
                break
            print(f"Zostało ci {hp_boh} Hp i {pierniczki} pierniczków")
            atak  = wybieranie_ataku()
            boss[1] = boss[1] - atak
            liczba_zadanych_obrażeni += atak
            print(f"{imie_boh} ze {pomocnik} zadaje {atak} obrażeń \n")

        if hp_boh > 0:
            print("="*40)
            print(f'{imie_boh} ze {pomocnik} zabił przeciwnika !!!')
            liczba_pokonanych_przeciwników = liczba_pokonanych_przeciwników + 1

    elif liczba_pokonanych_przeciwników == 4:
        break
if hp_boh > 0:
    print("="*40) 
    print(F"{imie_boh} ze {pomocnik} WYGRAŁ GRE !!!!\n")
else:
    print("="*40)
    print(f"{imie_boh} ZGINĄŁ a {pomocnik} wraz znim !!!! \n")
    
print("Statystyki gry: ")    
print(f"Zabiles {liczba_pokonanych_przeciwników} przeciwników")
print(f"Zadałeś łącznie {liczba_zadanych_obrażeni} hp przeciwniką")
print("\nKONIEC GRY")
