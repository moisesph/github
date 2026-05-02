using System.Collections.Generic;
using System.IO;
using System.Security.Cryptography.X509Certificates;
public class FinanceManager
{
    private float _total;
    Person person = new Person();


    /// /////////////////////////////////////////////

    public FinanceManager()
    {

    }



    /// /////////////////////////////////////////////

    public void Run()
    {
        string answer = "-5";

        Console.WriteLine("EcoTails");
        //Show persons

        while (answer != "Exit")
        {

            Console.WriteLine("Enter your finances");

            Console.Write("1. Create Profile\n2. Create Finance\n3. Load\n4. Save\n5. Display Finances");
            answer = Console.ReadLine();

            if (answer == "1")
            {
                CreateProfile();
            }

            else if (answer == "2")
            {
                person.CreateCategory();

            }
            else if (answer == "3")
            {
                LoadDocument();
            }
            else if (answer == "4")
            {
                SaveDocument();
            }

            else if (answer == "5")
            {
                DisplayCategories();
            }
        }

    }

    public void LoadProfiles()
    {
        try
        {
            Console.Write($"What is the filename for the goal file? ");
            string nameFile = Console.ReadLine();

            using (StreamWriter fileNew = new StreamWriter($"../../../{nameFile}.txt"))
            {
                fileNew.WriteLine($"{person}"); //Here get every finance
                                                // foreach (Goal g in _goals)
                {
                    //       fileNew.WriteLine($"{g.GetStringRepresentation()}");

                }
            }
        }

        catch (Exception e)
        {
            Console.WriteLine("Exception: " + e.Message);
        }

        finally
        {
            Console.WriteLine("Executing finally block.");
        }

    }

    public void CreateProfile()
    {
        Console.Write("Enter First and Last name: ");
        string name = Console.ReadLine();
        Console.Write("Income: ");
        string incomeS = Console.ReadLine();
        float income = float.Parse(incomeS);
        Person person1 = new Person(name, income);
        person = person1;

    }


    public void LoadDocument()
    {

    }

    public void SaveDocument()
    {
        Console.Write($"What is the filename for the goal file? ");
        string nameFile = Console.ReadLine();

        using (StreamWriter fileNew = new StreamWriter($"../../../{nameFile}.txt"))
        {
            fileNew.WriteLine($"{_score}");
            foreach (Goal g in _goals)
            {
                fileNew.WriteLine($"{g.GetStringRepresentation()}");

            }
        }



    }

    public void DisplayCategories()
    {
        person.DisplayCategories();
    }

}