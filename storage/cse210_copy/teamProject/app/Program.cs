using System;
using System.Xml.Linq;


class Program
{
    static void Main(string[] args)
    {
        Console.Write(@"Welcome to the Journal Program!");

        string answer = "";

        Journal diaryPage = new Journal();
        Entry data = new Entry();


        while (answer != "5")
        {
            Console.Write(@"Please select one of the following choices:
        1. Write
        2. Display
        3. Load
        4. Save
        5. Quit
        What would you like to do? ");
            answer = Console.ReadLine() ?? "";



            if (answer == "1")
            {
                data._date = DateTime.Now.ToString("MM/dd/yyyy");
                PromptGenerator theQuestion = new PromptGenerator();
                data._promptText = theQuestion.GetRandomPrompt();
                Console.Write($"{data._promptText} ");
                data._entryText = Console.ReadLine() ?? "";

                diaryPage.AddEntry(data);
            }
            ;

            if (answer == "2")
            {
                diaryPage.DisplayAll();

            }

            if (answer == "3")
            {
                Console.Write("What is the filename? ");
                string existedFile = Console.ReadLine() ?? "";
                diaryPage.LoadFromFile(existedFile);
            }

            if (answer == "4")
            {
                Console.Write("What is the filename? ");
                string newFileName = Console.ReadLine() ?? "";
                diaryPage.SaveToFile(newFileName);
            }

        }
    }

}

//I used Gemini for a recomendation about why the option 2 was not working, the issue was 
//I had the line Journal diaryPage = new Journal(); within the while circle, I used it because I spent 2 hours 
//trying to fix the function display and neverFound the issue.

