using System.Globalization;
using System.Linq;
public class Person
{
    private string _name = "default";
    private float _income = 0;

    private List<Category> _categories = new List<Category>();

    ////////////////////////////////////////////
    public Person(string name, float income)
    {
        _name = name;
        _income = income;

    }

    public Person(string name)
    {
        _name = name;

    }

    public Person()
    {
    }

    ////////////////////////////////////////////
    public void setName(string name)
    {
        _name = name;
    }

    public string getName()
    {
        return _name;
    }

    public void setIncome(float income)
    {
        _income = income;
    }

    public float returnIncome()
    {
        return _income;
    }

    //////////////////////////////////////////// 





    /////////////////CATEGORIES FUNCTIONS/////////////////////////// 

    public void CreateCategory()
    {

        if (_name == "default")
        {
            Console.WriteLine("There's no profile loaded, please create or load a profile");
        }
        else
        {
            Console.Write("Thing to pay: ");
            string categoryPay = Console.ReadLine();

            Console.Write("Current amount saved: ");
            string currentAmountS = Console.ReadLine();
            float currentAmount = float.Parse(currentAmountS);

            Console.Write("Spend every 15 Days ");
            string IngressAmountS = Console.ReadLine();
            float IngressAmount = float.Parse(IngressAmountS);
            _categories.Add(new(categoryPay, currentAmount, IngressAmount));
        }
    }
    public void SaveBackup()
    {

    }

    public void DisplayCategories()
    {

        bool hasElements = _categories.Any();
        if (!hasElements)
        {
            Console.WriteLine("You don't have any finances");
        }

        else
        {
            foreach (Category caterory in _categories)
            {
                caterory.Display();
            }
        }


    }


    public string saveInfoRepresentation()
    {
        foreach ()
        {

        }

        return $"{_name}, {_income}";
    }

    public void DeleteCategorie()
    {

    }

    public void RecoverDeletedCategorie()
    {

    }

}

