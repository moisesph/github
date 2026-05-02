public class Category
{
    private string _name;
    private double _currentValue;
    private double _valueRequired;
    private List<string> _history = new List<string>();

    ///////////////////////////////

    public Category(string name, double currentValue, double valueRequired)
    {
        _name = name;
        _currentValue = currentValue;
        _valueRequired = valueRequired;
    }





    /// ///////////////////////////////////////////////////////////

    public string GetName()
    {
        return _name;
    }

    public void SetName(string name)
    {
        _name = name;
    }

    public double GetCurrentValue()
    {
        return _currentValue;
    }

    public void SetCurrentValue(double currentValue)
    {
        _currentValue = currentValue;
    }


    public double GetValueRequired()
    {
        return _valueRequired;
    }

    public void SetValueRequired(double valueRequired)
    {
        _valueRequired = valueRequired;
    }


    /// ///////////////////////////////////////////////////////////

    public void Display()
    {
        Console.WriteLine($"{_name}: Current {_currentValue}$ Paying: {_valueRequired}");
    }


    public string saveInfoRepresentation()
    {
        return $"{_name}, {_currentValue}, {_valueRequired}";
    }

    public void WriteHistory()
    {
    }

    public void SaveHistory()
    {
    }
}


