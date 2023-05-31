using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace projekt
{
    internal class Program
    {
        static void Main(string[] args)
        {
           
            // Przywitanie uzytkownika
            Console.WriteLine("Witaj w grze");

            // Wybor imienia bohatera
            string imie_boh = "";
            while (imie_boh == "")
            {
                Console.WriteLine("Wprowadz imie swojego bohatera");
                imie_boh = Console.ReadLine();
            }

            // wybor bohatera
            Console.WriteLine("Wybierz z ktorego plemiona ma byc twoj bohater");
            Console.WriteLine("Wojownikow ----> wpisz '1'");
            Console.WriteLine("Magow ----> wpisz '2'");

            int plem_boh = int.Parse(Console.ReadLine());
            int hp_boh = 0;
            int zloto_boh = 0;
            int demage_bron = 0;
            string nazwa_plem = "";
        

            Random random = new Random();
            switch (plem_boh)
            {
                case 1:
                    nazwa_plem = "Wojownik";
                    hp_boh = 100;
                    zloto_boh = 50;
                    demage_bron = random.Next(5, 16);
                    break;
                case 2:
                    nazwa_plem = "Mag";
                    hp_boh = 80;
                    zloto_boh = 100;
                    demage_bron = random.Next(5, 16);
                    break;
                default:
                    Console.WriteLine("Nie wybrales bohatera :(");
                    return; // Zakończenie działania programu
            }
            Console.WriteLine($"Twój bohater to {nazwa_plem} o imieniu {imie_boh}.");
            
            // kilka zmiennych
            bool sklep_otwar = true;
            int licbza_prze = 0;
            int max_liczba_prze = 4;
            int cena_sklepu = 30;
            
            // głowna petla
            while (true)
            {
                // sklep
                if (sklep_otwar && licbza_prze > 1)
                {
                    Console.WriteLine("Odwiedzasz sklep. Możesz kupić lepszą broń.");
                    Console.WriteLine($"Koszt: {sklep_otwar} złota. Posiadasz {zloto_boh}");
                    Console.WriteLine("Czy chcesz kupić nową broń? (Tak - 't', Nie - dowolny klawisz)");

                    if (Console.ReadKey().KeyChar == 't')
                    {
                        if (zloto_boh >= cena_sklepu)
                        {
                            demage_bron += random.Next(1, 6);
                            zloto_boh -= cena_sklepu;
                            Console.WriteLine("Kupiłeś nową broń!");
                            Console.WriteLine($"Twój aktualny atak: {demage_bron}");
                        }
                        else
                        {
                            Console.WriteLine("Nie masz wystarczającej ilości złota!");
                        }
                    }

                    sklep_otwar = false;
                }

                // Walka z przeciwnikami
                if (licbza_prze < max_liczba_prze)
                {
                    Console.WriteLine($"Spotykasz przeciwnika {licbza_prze + 1}!");

                    string imie_prze = $"Przeciwnik {licbza_prze + 1}";
                    int hp_prze = random.Next(20, 60);
                    int gold_prze = random.Next(10, 30);
                    int atak_prze = random.Next(3, 10);

                    Console.WriteLine($"Zaczynasz walkę z {imie_prze}!");

                    while (hp_boh > 0 && hp_prze > 0)
                    {
                        Console.WriteLine("Co chcesz zrobić?");
                        Console.WriteLine("1. Atakuj");
                        Console.WriteLine("2. Uciekaj");

                        int wbr_akcji = int.Parse(Console.ReadLine());

                        switch (wbr_akcji)
                        {
                            case 1:
                                Console.WriteLine($"{imie_boh} atakuje {imie_prze} za {demage_bron} obrażeń.");
                                hp_prze -= demage_bron;

                                if (hp_prze >= 0)
                                {
                                    Console.WriteLine($"{imie_prze} atakuje {imie_boh} za {atak_prze} obrażeń.");
                                    hp_boh -= atak_prze;
                                }
                                break;
                            case 2:
                                Console.WriteLine("Uciekasz z walki.");
                                hp_boh = 0;
                                break;
                            default:
                                Console.WriteLine("Niepoprawny wybór. Tracisz turę.");
                                break;
                        }

                        Console.WriteLine($"Stan twojego bohatera:| Zdrowie: {hp_boh} | Złoto: {zloto_boh}");
                        Console.WriteLine($"Stan przeciwnika:| Zdrowie: {hp_prze} | Złoto: {gold_prze}");
                    }

                    if (hp_boh <= 0)
                    {
                        Console.WriteLine("Twój bohater zginął. Koniec gry.");
                        return;
                    }
                    else
                    {
                        Console.WriteLine($"Pokonałeś {imie_prze}! Zdobywasz {gold_prze} złota.");
                        zloto_boh += gold_prze;
                        licbza_prze++;
                        sklep_otwar = true;
                    }

                    Console.WriteLine("Naciśnij dowolny klawisz, aby kontynuować.");
                    Console.ReadKey();
                }
                else
                {
                    Console.WriteLine("Pokonałeś wszystkich przeciwników! Gratulacje!");
                    return;
                }
            }
        }
    }
}

















