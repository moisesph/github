using System;

class Program
{
    static void Main(string[] args)
    {
        string keepPlaying = "yes";

        while (keepPlaying == "yes")
        {
            int guess = -1;
            Random randomGenerator = new Random();
            int magicNumber = randomGenerator.Next(1, 101);
            int tries = 0;

            while (guess != magicNumber)
            {

                tries += 1;
                Console.Write("What is your guess? ");
                guess = int.Parse(Console.ReadLine());


                if (guess == magicNumber)
                {
                    Console.WriteLine("You guessed it!");
                    Console.WriteLine($"It only took you {tries} tries");
                    Console.Write("Do you want to keep playing? ");
                    keepPlaying = Console.ReadLine();
                }

                else if (guess < magicNumber)
                {
                    Console.WriteLine("Higher");
                }

                else if (guess > magicNumber)
                {
                    Console.WriteLine("Lower");
                }
            }

        }


    }
}