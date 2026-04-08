using System;
using System.Collections.Generic;
using System.IO;
using System.IO.Enumeration;


public class Journal
{
    public List<Entry> _entries = new List<Entry>();
    public void AddEntry(Entry newEntry)
    {
        _entries.Add(newEntry);
    }
    public void DisplayAll()
    {
        foreach (Entry a in _entries)
        {
            a.Display();
        }

    }

    public void SaveToFile(string file)
    {
        //Saves the document in a txt maybe

        using (StreamWriter outputFile = new StreamWriter(file))
        {
            foreach (Entry lines in _entries)
            {
                outputFile.WriteLine($"{lines._date} {lines._promptText} {lines._entryText}");
            }
        }

    }

    public void LoadFromFile(string file)
    {
        //Loads one saved file
        using (StreamReader reader = new StreamReader(file))
        {
            string line;
            while ((line = reader.ReadLine()) != null)
            {
                Entry oldDocument = new Entry();
                oldDocument._entryText = line;
                AddEntry(oldDocument);
            }
        }
    }
}

//I used Gemini How to make a for loop