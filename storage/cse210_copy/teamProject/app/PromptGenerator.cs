using System;
using System.Collections.Generic;
public class PromptGenerator
{
    public List<string> _prompts = new List<string>
    {
        "What was the best part of my Day?",
        "If I had one thing I could do over today, what would it be?",
        "What are three things I’m grateful for today?",
        "What was a small win I experienced?",
        "What did I learn today about myself?"
    };

    Random _rng = new Random();

    public string GetRandomPrompt()
    {
        int total = _prompts.Count;
        int makeRandom = _rng.Next(total);
        string _chosenPrompt = _prompts[makeRandom];
        return _chosenPrompt;
    }
}

// I used a tutorial of how to make a random in a Youtube tutorial but I don't remember which one.
// I used Gemini to give me more Ideas of prompts in the list _prompts.