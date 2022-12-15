from random import randint;
# wprowadzenie do gry
print('Witaj w grze ....')

# wybór imienia bohatera
imie_boh = ''
while imie_boh == "":
    imie_boh = input("Wprowadz imie swojego głównego bohatera --> ")
    if imie_boh == "":
        print("Nie wprowadziłes imienia!!!!")

# wybór typu bohatera
typ_boh = ''
hp_boh = 0
kasa_boh = 0
while typ_boh.upper() not in ['A', 'D', 'Z']:
    print("Twoja kwota w portfelu wynosi 100$ wybierz typ bohatera:")
    typ_boh = input("( ZWYKŁY = z/Z | ATAKUJĄCY(-40$) = a/A | DEFENSOR(-40$) = d/D ) ---> ")
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

# atak specjalny
def specjalny_atak():
    global kasa_boh
    global hp_boh
    if typ_boh.upper() == 'Z':
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
    print("\n Wybierz atak: ")

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
                print("Nie masz wystarczającej ilości pieniędzy :( " )
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

# Przeciwnicy 1 poziom
# 0 - imie, 1 - hp, 2 - atak
prze1 = ["Elfem", 10, 10]
prze2 = ["Gnomem", 5, 10]
prze3 = ["Cyklopem", 15, 10]
prze4 = ["Karłem", 15, 5]
lista_prze = [prze1, prze2, prze3, prze4]

def random_prze():
    przeciwnik = lista_prze[randint(0,3)]
    return przeciwnik

# przeciwnik drugi poziom

boss = ["cyborg", 25, randint(5,10)]

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
            print(f"{imie_boh} walczy teraz z {Opponent[0]}")
            print(f"Przeciwnik ma {Opponent[1]} Hp i zadaje ci {Opponent[2]} obrażeń")
            hp_boh = hp_boh - Opponent[2]
            if hp_boh <= 0:
                break
            print(f"Zostało ci {hp_boh} Hp i {kasa_boh} Many")
            atak  = wybieranie_ataku()
            Opponent[1] = Opponent[1] - atak
            liczba_zadanych_obrażeni += atak
            print(f"{imie_boh} zadaje {atak} obrażeń \n")
            
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
            print(f"{imie_boh} walczy teraz z {boss[0]} (boss)")
            print(f"Przeciwnik ma {boss[1]} Hp i zadaje ci {boss[2]} obrażeń")
            hp_boh = hp_boh - boss[2]
            if hp_boh <= 0:
                break
            print(f"Zostało ci {hp_boh} Hp i {kasa_boh} $")
            atak  = wybieranie_ataku()
            boss[1] = boss[1] - atak
            liczba_zadanych_obrażeni += atak
            print(f"{imie_boh} zadaje {atak} obrażeń \n")

        if hp_boh > 0:
            print("="*40)
            print(f'{imie_boh} zabił przeciwnika !!!')
            liczba_pokonanych_przeciwników = liczba_pokonanych_przeciwników + 1

    elif liczba_pokonanych_przeciwników == 4:
        break
if hp_boh > 0:
    print("="*40) 
    print(F"{imie_boh} WYGRAŁ GRE !!!!\n")
else:
    print("="*40)
    print(f"{imie_boh} ZGINĄŁ !!!! \n")
    
print("Statystyki gry: ")    
print(f"Zabiles {liczba_pokonanych_przeciwników} przeciwników")
print(f"Zadałeś {liczba_zadanych_obrażeni} hp przeciwniką")
print("\nKONIEC GRY")
        
        
        
    
        
