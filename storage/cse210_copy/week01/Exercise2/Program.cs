using System;

class Program
{
    static void Main(string[] args)
    {
        string finalNote = "A";

        Console.Write("What is your grade percentage? %");
        int percentage = int.Parse(Console.ReadLine());

        if (percentage >= 90)
        {
            finalNote = "A";
        }

        else if (percentage >= 80)
        {
            finalNote = "B";
        }

        else if (percentage >= 70)
        {
            finalNote = "C";
        }

        else if (percentage >= 60)
        {
            finalNote = "D";
        }

        else
        {
            finalNote = "F";
        }

        Console.WriteLine($"Your grade is {finalNote}");

    }
}